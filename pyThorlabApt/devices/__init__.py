import pkgutil
from .stage_db import StageDB, StageInfo, StageInfoHome, StageInfoJog, StageInfoPhysical, StageInfoLimits, \
    StageInfoControl, StageInfoMisc


stage_db = StageDB()
stage_db.populate_by_xml(pkgutil.get_data('pyThorlabApt.devices',
                                          'ThorlabsDefaultSettings.xml').decode('ascii'))
