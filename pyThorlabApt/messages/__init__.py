import struct

from .hw_messages import *
from .impl import Message

MSG_DICT = dict(map(lambda name: (globals()[name].id, globals()[name]), filter(lambda x: x.startswith('MGMSG_'), dir())))


def get_message_class_by_id(message_id):
    return MSG_DICT[message_id]


def create_from_data_buffer(buffer):
    message_id, = struct.Struct('<H').unpack(buffer[:2])
    cls = get_message_class_by_id(message_id)
    #assert isinstance(cls, Message)

    message_length = cls.binary_length
    if len(buffer) < cls.binary_length:
        return None, buffer

    return cls.create_from_data_buffer(buffer[:message_length])


def get_all_messages_of_category(category):
    return [cls for cls in MSG_DICT.values() if cls.category == category]