import collections
from xml.etree import ElementTree as ET


class BaseXMLSource:
    _xml_fields = tuple()
    _xml_fields_type = tuple()

    @classmethod
    def create_from_xml_element(cls, element):
        assert isinstance(element, ET.Element)
        # assert element.tag == 'DeviceSettingsDefinition'

        type_mapper = {
            bool: lambda x: x.lower() == 'true'
        }

        parameters = dict()
        for field_name, xml_field_name, xml_field_type in zip(cls._fields, cls._xml_fields, cls._xml_fields_type):
            field_element = element.find(xml_field_name)

            if hasattr(xml_field_type, 'create_from_xml_element'):
                value = xml_field_type.create_from_xml_element(field_element)
            else:
                text_value = field_element.text if field_element is not None else element.attrib[xml_field_name]
                value = type_mapper.get(xml_field_type, xml_field_type)(text_value)

            parameters[field_name] = value

        return cls(**parameters)


class StageInfoMisc(collections.namedtuple('DeviceMisc', ['backslash_dist', 'move_factor', 'rest_factor']),
                    BaseXMLSource):
    _xml_fields = 'BacklashDist', 'MoveFactor', 'RestFactor'
    _xml_fields_type = float, float, float


class StageInfoControl(collections.namedtuple('DeviceControl', ['def_min_vel', 'def_accn', 'def_max_vel']),
                       BaseXMLSource):
    _xml_fields = 'DefMinVel', 'DefAccn', 'DefMaxVel'
    _xml_fields_type = float, float, float


class StageInfoLimits(collections.namedtuple('DeviceLimits', ['cw_hard_limit', 'ccw_hard_limit',
                                                              'cw_soft_limit', 'ccw_soft_limit',
                                                              'soft_limit_mode']), BaseXMLSource):
    _xml_fields = 'CWHardLimit', 'CCWHardLimit', 'CWSoftLimit', 'CCWSoftLimit', 'SoftLimitMode'
    _xml_fields_type = float, float, float, float, int


class StageInfoPhysical(collections.namedtuple('DevicePhysical', ['unit', 'pitch', 'steps_per_rev', 'gearbox_ratio',
                                                                  'dir_sense', 'min_pos', 'max_pos', 'max_accn',
                                                                  'max_vel']), BaseXMLSource):
    _xml_fields = 'Units', 'Pitch', 'StepsPerRev', 'GearboxRatio', 'DirSense', 'MinPos', 'MaxPos', 'MaxAccn', 'MaxVel'
    _xml_fields_type = lambda unit: {1: 'mm', 2: '°'}[int(unit)], float, int, float, int, float, float, float, float

    @property
    def encoder_count(self):
        return self.steps_per_rev * self.gearbox_ratio / self.pitch


class StageInfoJog(
        collections.namedtuple('DeviceJog', ['mode', 'step_size', 'min_vel', 'accn', 'max_vel', 'stop_mode']),
        BaseXMLSource):
    _xml_fields = 'JogMode', 'JogStepSize', 'JogMinVel', 'JogAccn', 'JogMaxVel', 'JogStopMode'
    _xml_fields_type = int, float, float, float, float, int


class StageInfoHome(collections.namedtuple('DeviceHome', ['dir', 'limit_switch', 'vel', 'zero_offset']), BaseXMLSource):
    _xml_fields = 'HomeDir', 'HomeLimitSwitch', 'HomeVel', 'HomeZeroOffset'
    _xml_fields_type = int, int, float, float


class StageInfo(collections.namedtuple('Device',
                                       ['name', 'stage_id', 'axis_id',
                                        'encoder_fitted',
                                        'home', 'jog', 'physical', 'limits', 'control', 'misc']), BaseXMLSource):
    _xml_fields = 'Name', 'StageID', 'AxisID', 'EncoderFitted', 'Home', 'Jog', 'Physical', 'Limits', 'Control', 'Misc'
    _xml_fields_type = str, int, int, bool, StageInfoHome, StageInfoJog, StageInfoPhysical, StageInfoLimits, StageInfoControl, StageInfoMisc


class StageDB:
    def __init__(self):
        self._stages = dict()

    def populate_by_xml(self, xml_buffer):
        root = ET.fromstring(xml_buffer)

        # Read in all devices
        devices = {}
        for device_def_element in root.findall('DeviceSettingsList')[0].iter('DeviceSettingsDefinition'):
            device = StageInfo.create_from_xml_element(device_def_element)
            devices[device.name] = device


def main():
    import pkgutil

    stage_db = StageDB()
    stage_db.populate_by_xml(pkgutil.get_data('pyThorlabApt.devices',
                                              'ThorlabsDefaultSettings.xml').decode('ascii'))


if __name__ == '__main__':
    main()
