import pyThorlabApt.messages.hw_messages as msgs


def main():
    from pprint import pprint
    msgs_dict = dict(map(lambda name: (name, getattr(msgs, name)), filter(lambda x: x.startswith('MGMSG_'), dir(msgs))))

    #pprint(msgs_dict)

    unique_calls = list()
    parameter_calls = dict()

    for name, cls in msgs_dict.items():
        split_name = name.split('_')
        assert split_name[0] == 'MGMSG'

        category = cls.category
        if cls.is_property:
            call_type = split_name[2]
            parameter_name = '_'.join(split_name[3:])

            key = (category, parameter_name)
            if key not in parameter_calls:
                parameter_calls[key] = dict()

            parameter_calls[key][call_type] = cls

    for key in parameter_calls.keys():

        if 'GET' in parameter_calls[key] and 'SET' in parameter_calls[key]:
            if not parameter_calls[key]['GET'].parameters == parameter_calls[key]['SET'].parameters:
                print(parameter_calls[key]['GET'], parameter_calls[key]['SET'])

    pprint(parameter_calls)

if __name__ == '__main__':
    main()