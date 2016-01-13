from . import stage_db, StageInfo


class Stage:
    def __init__(self, stage_info):
        assert isinstance(stage_info, StageInfo)
        self._stage_info = stage_info