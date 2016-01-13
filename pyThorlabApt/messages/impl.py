import struct

from ..helpers import classproperty


class Message:
    id = 0x0
    is_long_cmd = False
    parameters = [(None, 'B'), (None, 'B')]

    def __init__(self, destination, *args, source=0x01, **kwargs):
        self.destination, self.source = int(destination), int(source)
        parameter_values = [None, ] * len(self.parameters)

        # Set parameters by position
        for i, value in enumerate(args):
            parameter_values[i] = value

        # Set parameter by name
        parameter_mapping = {name: position for position, (name, encoding)
                             in enumerate(self.parameters)}
        for name, value in kwargs.items():
            try:
                position = parameter_mapping[name]
            except KeyError:
                raise KeyError('{0} not a valid parameter. Must be one of {1}'.format(name, self.parameter_names))

            if parameter_values[position] is not None:
                raise ValueError('Parameter {0} "{1}" was already set by positional argument.'.format(position, name))
            parameter_values[position] = value

        for position, ((name, encoding), value) in enumerate(zip(self.parameters, parameter_values)):
            if name is not None and value is None:
                raise ValueError('Parameter {0} "{1}" ({2}) was not set.'.format(position, name, encoding))
        self._parameter_values = parameter_values

    @classproperty
    def name(self):
        return self.__name__

    @classproperty
    def category(self):
        split_name = self.__name__.split('_')
        assert split_name[0] == 'MGMSG', 'Class name has to start with MGMSG_'
        return split_name[1].lower()

    @classproperty
    def is_property(self):
        split_name = self.__name__.split('_')
        return split_name[2] in ('REQ', 'SET', 'GET')

    @classproperty
    def parameter_names(self):
        return [name for name, encoding in self.parameters if name is not None]

    @property
    def parameter_items(self):
        return ((name, value) for ((name, encoding), value)
                in zip(self.parameters, self._parameter_values) if name is not None)

    @property
    def parameter_dict(self):
        return dict(self.parameter_items)

    @classproperty
    def struct_description(self):
        if not self.is_long_cmd:
            full_struct_desc = [('message_id', 'H'), ] + self.parameters + [('destination', 'B'), ('source', 'B')]
        else:
            full_struct_desc = ([('message_id', 'H'), ('length', 'H'), ('destination', 'B'), ('source', 'B')]
                                + self.parameters)
        names, encodings = zip(*full_struct_desc)
        return names, '<' + ''.join(encodings)

    @classproperty
    def binary_length(self):
        return struct.Struct(self.struct_description[1]).size

    @classmethod
    def create_from_data_buffer(cls, buffer):
        fields, struct_desc = cls.struct_description
        descr = dict(zip(fields, struct.Struct(struct_desc).unpack(buffer)))

        if 'length' in descr:
            assert descr['length'] == len(buffer) - 6
            del descr['length']

        assert descr['message_id'] == cls.id
        del descr['message_id']
        descr['destination'] &= 0x7f

        if None in descr:
            del descr[None]

        return cls(**descr)

    def __bytes__(self):
        fields, struct_desc = self.struct_description
        s = struct.Struct(struct_desc)

        descr = dict(self.parameter_items)
        descr['message_id'] = self.id
        descr['length'] = self.binary_length - 6
        descr['source'] = self.source
        descr['destination'] = self.destination | (0x80 if descr['length'] else 0)
        descr[None] = 0

        values = map(lambda x: descr[x], fields)


        type_mapping = {
            str: lambda x: x.encode('ascii')
        }
        encoded_values = map(lambda x: type_mapping.get(type(x), type(x))(x), values)
        return s.pack(*encoded_values)

    def __repr__(self):
        return "<%s>(dest=0x%x, src=0x%x, %s)" % (self.__class__.__name__,
                                                self.destination, self.source,
                                                ', '.join('{0}={1}'.format(name, repr(value)) for name, value in
                                                          self.parameter_items))
