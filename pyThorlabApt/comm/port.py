import serial
import select
import threading
import time
import queue
import weakref
import struct
import collections

from pyThorlabApt.messages import Message, create_from_data_buffer, get_all_messages_of_category
import pyThorlabApt.messages as msgs


class Port:
    def __init__(self, port, debug=False):
        super().__init__()

        self._debug = debug
        self._serial = serial.Serial(port,
                                     baudrate=115200,
                                     bytesize=serial.EIGHTBITS,
                                     parity=serial.PARITY_NONE,
                                     stopbits=serial.STOPBITS_ONE,
                                     rtscts=True,
                                     timeout=0.1)
        self._serial.setRTS(0)
        time.sleep(0.05)
        self._serial.reset_input_buffer()
        self._serial.reset_output_buffer()

        time.sleep(0.05)
        self._serial.setRTS()

        self._lock = threading.RLock()

        # We can now already write but not read. We use this to send commands
        # which stop the unit from auto-reporting its current state.
        #
        # We can then flush the input buffer and hope that we are then message aligned.
        self.send_message(msgs.MGMSG_HW_NO_FLASH_PROGRAMMING(destination=0x50))
        self.send_message(msgs.MGMSG_HW_STOP_UPDATEMSGS(destination=0x50))
        time.sleep(0.5)
        self._serial.reset_input_buffer()

        self._buffer = b''
        self._queues = list()
        self._keep_running = True

        self._thread_main = threading.current_thread()
        self._thread_worker = threading.Thread(target=Port.run, args=(weakref.proxy(self),))
        self._thread_worker.start()

    def raw_send(self, data):
        #print('>', ['%02x' % _ for _ in data])
        with self._lock:
            self._serial.write(data)

    def send_message(self, message):
        if self._debug:
            print('>', message)
        self.raw_send(bytes(message))

    @staticmethod
    def run(self):
        assert isinstance(self, Port)
        self._keep_running = True

        try:
            while self._keep_running and self._thread_main.is_alive():
                r, w, e = select.select([self._serial], [], [], 1)
                with self._lock:
                    new_data = self._serial.read(1)
                if len(new_data):
                    self._buffer += new_data
                    self._parse_messages()

        except ReferenceError as e:
            # The self object was deleted! Shutting down the thread.
            pass

    def _parse_messages(self):
        base_package = struct.Struct('<HHBB')
        base_package_length = base_package.size
        while len(self._buffer) >= base_package_length:
            message_id, length, dest, source = base_package.unpack(self._buffer[:base_package_length])
            # Is this a long message?
            long_message = (dest & 0x80) == 0x80

            if len(self._buffer) < base_package_length + (length if long_message else 0):
                break

            if not long_message:
                short_msg_package = struct.Struct('<HBBBB')
                msg = collections.OrderedDict(zip(('message_id', 'param1', 'param2', 'dest', 'source'),
                                                  short_msg_package.unpack(self._buffer[:short_msg_package.size])))
                msg['raw_data'] = self._buffer[:short_msg_package.size]
                self._buffer = self._buffer[short_msg_package.size:]
            else:
                long_msg_package = struct.Struct('<HHBBB')
                msg = collections.OrderedDict(zip(('message_id', 'length', 'dest', 'source'),
                                                  long_msg_package.unpack(self._buffer[:long_msg_package.size])))
                msg['data'] = self._buffer[long_msg_package.size:long_msg_package.size+length]
                msg['raw_data'] = self._buffer[:long_msg_package.size+length]
                self._buffer = self._buffer[long_msg_package.size+length:]

            if message_id == 0:
                continue

            try:
                parsed_msg = create_from_data_buffer(msg['raw_data'])
                if self._debug:
                    print('<', parsed_msg)

                # Push message to all registered queues where optional filtering applies.
                for msg_queue, msg_queue_filter_fun in self._queues:
                    if msg_queue_filter_fun is None or msg_queue_filter_fun(parsed_msg):
                        msg_queue.put(parsed_msg)

            except KeyError:
                if self._debug:
                    print('Unhandled message: ', msg)

    def add_queue(self, queue, filter_fun=None):
        #self._queues.append((weakref.proxy(queue), weakref.proxy(filter_fun)))
        self._queues.append((queue, filter_fun))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._keep_running = False


class Device:
    class _CmdTree:
        MSG_DICT = dict(map(lambda name: (name, getattr(msgs, name)), filter(lambda x: x.startswith('MGMSG_'), dir(msgs))))

        def __init__(self, device, path=[]):
            self.__device = device
            self.__path = path

        def __getattr__(self, item):
            if item.startswith('_'):
                raise AttributeError

            # Filter all commands with match this path
            current_path = self.__path + [item, ]

            possible_cls_candidates_dict = {_.name: _ for _ in get_all_messages_of_category(current_path[0])}
            if len(current_path) == 1 and possible_cls_candidates_dict:
                return Device._CmdTree(self.__device, path=current_path)

            else:
                # If this is a getter of a poperty, there must be propper reply somewhere here
                getter_message = 'MGMSG_{0}_GET_{1}'.format(*current_path[:2]).upper()
                request_message = 'MGMSG_{0}_REQ_{1}'.format(*current_path[:2]).upper()

                if getter_message in possible_cls_candidates_dict \
                        and request_message in possible_cls_candidates_dict:
                    request_message_cls = possible_cls_candidates_dict[request_message]
                    getter_message_cls = possible_cls_candidates_dict[getter_message]

                    if 'chan_ident' in request_message_cls.parameter_names:
                        # We still need the right channel
                        if len(current_path) < 3:
                            return Device._CmdTree(self.__device, path=current_path)

                        channel_str = current_path[2]
                        if not channel_str.startswith('channel_'):
                            raise KeyError('Requires channel description starting with channel_')
                        channel = int(channel_str.split('_', 1)[1])

                        self.__device._port.send_message(request_message_cls(self.__device.destination_id,
                                                                             chan_ident=channel))
                        reply_msg = self.__device.wait_for_message(lambda msg: isinstance(msg, getter_message_cls)
                                                                               and msg.parameter_dict['chan_ident'] == channel)
                        result = reply_msg.parameter_dict
                        del result['chan_ident']

                    else:
                        self.__device._port.send_message(request_message_cls(self.__device.destination_id))
                        reply_msg = self.__device.wait_for_message(lambda msg: isinstance(msg, getter_message_cls))
                        result = reply_msg.parameter_dict

                    assert isinstance(result, dict)
                    if len(result) > 1:
                        return result
                    else:
                        return list(result.values())[0]

                else:
                    #TODO: implement commands etc
                    pass

            raise AttributeError

    def __init__(self, port, destination_id=0x50):
        assert isinstance(port, Port)
        self._port = port
        self.destination_id = destination_id
        self._incoming_message_queue = queue.Queue()
        self._port.add_queue(self._incoming_message_queue, lambda msg: msg.source == destination_id)

    @property
    def comm(self):
        return self._CmdTree(self)

    def _recv_message(self, block=True, timeout=None):
        try:
            return self._incoming_message_queue.get(block, timeout)
        except queue.Empty:
            return None

    def wait_for_message(self, filter_fun, timeout=1.0):
        start_time = time.time()

        while True:
            remaining_time = timeout - (time.time() - start_time)
            if remaining_time <= 0:
                raise TimeoutError('No matching reply found')

            new_msg = self._recv_message(timeout=remaining_time)
            if new_msg is not None and filter_fun(new_msg):
                return new_msg

    @property
    def model_number(self):
        return self.comm.hw.info['model_number'].decode('ascii')

    @property
    def hardware_notes(self):
        return self.comm.hw.info['notes'].decode('ascii')


def _test_tree():
    with Port('/dev/thorlabs_tsc001') as p:
        device = Device(p, destination_id=0x50)
        print(device.comm.mot.sol_operatingmode.channel_1)  # MGMSG_MOT_SET_SOL_OPERATINGMODE, chan_ident=1
        print(device.model_number, device.hardware_notes)



def _test():
    with Port('/dev/thorlabs_tsc001') as p:
        p.send_message(msgs.MGMSG_HW_NO_FLASH_PROGRAMMING(destination=0x50))
        p.send_message(msgs.MGMSG_HW_STOP_UPDATEMSGS(destination=0x50))

        p.send_message(msgs.MGMSG_HW_REQ_INFO(destination=0x50))
        time.sleep(0.2)


        p.send_message(msgs.MGMSG_MOT_SET_SOL_OPERATINGMODE(destination=0x50, chan_ident=0x01, mode=0x01))


        p.send_message(msgs.MGMSG_MOT_SET_SOL_INTERLOCKMODE(destination=0x50, chan_ident=0x01, mode=0x02))


        # p.send_message(msgs.MGMSG_HW_START_UPDATEMSGS(destination=0x50, update_rate=1))
        p.send_message(msgs.MGMSG_MOT_REQ_STATUSBITS(destination=0x50, chan_ident=0x01))


        time.sleep(0.5)

        # time.sleep(5.5)
        # return
        # for i in range(6):
        #
        #     shutter_open = i%2==0
        #     state = 0x01 if shutter_open else 0x02
        #
        #     print()
        #     print('Opening shutter:' if shutter_open else 'Closing shutter:')
        #     time.sleep(0.5)
        #     p.send_message(msgs.MGMSG_MOD_SET_CHANENABLESTATE(destination=0x50, chan_ident=0x01, state=state))
        #     # p.send_message(msgs.MGMSG_MOT_SET_SOL_STATE(destination=0x50, chan_ident=0x01, state=state))
        #     time.sleep(1.5)
        #     p.send_message(msgs.MGMSG_MOT_REQ_SOL_STATE(destination=0x50, chan_ident=0x01))
        #     p.send_message(msgs.MGMSG_MOT_REQ_SOL_INTERLOCKMODE(destination=0x50, chan_ident=0x01))
        #     # p.send_message(msgs.MGMSG_MOD_REQ_CHANENABLESTATE(destination=0x50, chan_ident=0x01))
        #     # p.send_message(msgs.MGMSG_MOT_REQ_STATUSUPDATE(destination=0x50, chan_ident=0x01))
        #     time.sleep(0.5)

        # shutter_open = False
        # while True:
        #     shutter_open = not shutter_open
        #     state = 0x01 if shutter_open else 0x02
        #
        #     p.send_message(msgs.MGMSG_MOD_SET_CHANENABLESTATE(destination=0x50, chan_ident=0x01, state=state))
        #
        #     while True:
        #         msg = p.receive_message()
        #         if not isinstance(msg, msgs.MGMSG_MOT_GET_STATUSUPDATE):
        #             continue
        #         if bool(dict(msg.parameter_items)['status_bits'] & 0x1) == shutter_open:
        #             break

if __name__ == '__main__':
    _test_tree()