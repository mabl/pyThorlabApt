from .impl import Message

class MGMSG_HW_DISCONNECT(Message):
    id = 0x2

class MGMSG_HW_REQ_INFO(Message):
    id = 0x5

class MGMSG_HW_GET_INFO(Message):
    id = 0x6
    is_long_cmd = True
    parameters = [('serial_number', 'I'), ('model_number', '8s'), ('type', 'H'), ('firmware_version', '4s'), ('notes', '48s'), ('empty_space', '12s'), ('hw_version', 'H'), ('mod_state', 'H'), ('nchs', 'H')]


class MGMSG_HW_START_UPDATEMSGS(Message):
    id = 0x11
    parameters = [('update_rate', 'B'), (None, 'B')]


class MGMSG_HW_STOP_UPDATEMSGS(Message):
    id = 0x12

class MGMSG_HW_YES_FLASH_PROGRAMMING(Message):
    id = 0x17

class MGMSG_HW_NO_FLASH_PROGRAMMING(Message):
    id = 0x18

class MGMSG_RACK_REQ_BAYUSED(Message):
    id = 0x60
    parameters = [('bay_ident', 'B'), (None, 'B')]


class MGMSG_RACK_GET_BAYUSED(Message):
    id = 0x61
    parameters = [('bay_ident', 'B'), ('bay_state', 'B')]


class MGMSG_HUB_REQ_BAYUSED(Message):
    id = 0x65

class MGMSG_HUB_GET_BAYUSED(Message):
    id = 0x66
    parameters = [('bay_ident', 'B'), (None, 'B')]


class MGMSG_HW_RESPONSE(Message):
    id = 0x80

class MGMSG_HW_RICHRESPONSE(Message):
    id = 0x81
    is_long_cmd = True
    parameters = [('msg_ident', 'H'), ('code', 'H'), ('notes', '64s')]


class MGMSG_MOD_SET_CHANENABLESTATE(Message):
    id = 0x210
    parameters = [('chan_ident', 'B'), ('state', 'B')]


class MGMSG_MOD_REQ_CHANENABLESTATE(Message):
    id = 0x211
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOD_GET_CHANENABLESTATE(Message):
    id = 0x212
    parameters = [('chan_ident', 'B'), ('state', 'B')]


class MGMSG_MOD_SET_DIGOUTPUTS(Message):
    id = 0x213
    parameters = [('bits', 'B'), (None, 'B')]


class MGMSG_MOD_REQ_DIGOUTPUTS(Message):
    id = 0x214
    parameters = [('bits', 'B'), (None, 'B')]


class MGMSG_MOD_GET_DIGOUTPUTS(Message):
    id = 0x215
    parameters = [('bits', 'B'), (None, 'B')]


class MGMSG_MOD_IDENTIFY(Message):
    id = 0x223

class MGMSG_RACK_REQ_STATUSBITS(Message):
    id = 0x226
    parameters = [('status_bits', 'B'), (None, 'B')]


class MGMSG_RACK_GET_STATUSBITS(Message):
    id = 0x227
    is_long_cmd = True
    parameters = [('sstatus_bits', 'I')]


class MGMSG_RACK_SET_DIGOUTPUTS(Message):
    id = 0x228
    parameters = [('bits', 'B'), (None, 'B')]


class MGMSG_RACK_REQ_DIGOUTPUTS(Message):
    id = 0x229

class MGMSG_RACK_GET_DIGOUTPUTS(Message):
    id = 0x230
    parameters = [('bits', 'B'), (None, 'B')]

class MGMSG_MOT_SET_ENCCOUNTER(Message):
    id = 0x409
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('encoder_count', 'i')]


class MGMSG_MOT_REQ_ENCCOUNTER(Message):
    id = 0x40a
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_ENCCOUNTER(Message):
    id = 0x40b
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('encoder_count', 'i')]


class MGMSG_MOT_SET_POSCOUNTER(Message):
    id = 0x410
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('position', 'i')]


class MGMSG_MOT_REQ_POSCOUNTER(Message):
    id = 0x411
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_POSCOUNTER(Message):
    id = 0x412
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('position', 'i')]


class MGMSG_MOT_SET_VELPARAMS(Message):
    id = 0x413
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('min_velocity', 'I'), ('acceleration', 'I'), ('max_velocity', 'I')]


class MGMSG_MOT_REQ_VELPARAMS(Message):
    id = 0x414
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_VELPARAMS(Message):
    id = 0x415
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('min_velocity', 'I'), ('acceleration', 'I'), ('max_velocity', 'I')]


class MGMSG_MOT_SET_JOGPARAMS(Message):
    id = 0x416
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('jog_mode', 'H'), ('jog_step_size', 'I'), ('jog_min_velocity', 'I'), ('jog_acceleration', 'I'), ('jog_max_velocity', 'I'), ('jog_stop_mode', 'H')]


class MGMSG_MOT_REQ_JOGPARAMS(Message):
    id = 0x417
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_JOGPARAMS(Message):
    id = 0x418
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('jog_mode', 'H'), ('jog_step_size', 'I'), ('jog_min_velocity', 'I'), ('jog_acceleration', 'I'), ('jog_max_velocity', 'I'), ('jog_stop_mode', 'H')]


class MGMSG_MOT_SET_LIMSWITCHPARAMS(Message):
    id = 0x423
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('cw_hard_limit', 'H'), ('ccw_hard_limit', 'H'), ('cw_soft_limit', 'I'), ('ccw_soft_limit', 'I'), ('software_limit_mode', 'H')]


class MGMSG_MOT_REQ_LIMSWITCHPARAMS(Message):
    id = 0x424
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_LIMSWITCHPARAMS(Message):
    id = 0x425
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('cw_hard_limit', 'H'), ('ccw_hard_limit', 'H'), ('cw_soft_limit', 'I'), ('ccw_soft_limit', 'I'), ('software_limit_mode', 'H')]


class MGMSG_MOT_SET_POWERPARAMS(Message):
    id = 0x426
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('rest_factor', 'H'), ('move_factor', 'H')]


class MGMSG_MOT_REQ_POWERPARAMS(Message):
    id = 0x427
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_POWERPARAMS(Message):
    id = 0x428
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('rest_factor', 'H'), ('move_factor', 'H')]


class MGMSG_MOT_REQ_STATUSBITS(Message):
    id = 0x429
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_STATUSBITS(Message):
    id = 0x42a
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('status_bits', 'I')]


class MGMSG_MOT_REQ_ADCINPUTS(Message):
    id = 0x42b
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_ADCINPUTS(Message):
    id = 0x42c
    is_long_cmd = True
    parameters = [('adc_input1', 'H'), ('adc_input2', 'H')]


class MGMSG_MOT_SET_GENMOVEPARAMS(Message):
    id = 0x43a
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('backlash_distance', 'i')]


class MGMSG_MOT_REQ_GENMOVEPARAMS(Message):
    id = 0x43b
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_GENMOVEPARAMS(Message):
    id = 0x43c
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('backlash_distance', 'i')]


class MGMSG_MOT_SET_HOMEPARAMS(Message):
    id = 0x440
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('home_direction', 'H'), ('limit_switch', 'H'), ('home_velocity', 'I'), ('offset_distance', 'I')]


class MGMSG_MOT_REQ_HOMEPARAMS(Message):
    id = 0x441
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_HOMEPARAMS(Message):
    id = 0x442
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('home_direction', 'H'), ('limit_switch', 'H'), ('home_velocity', 'I'), ('offset_distance', 'I')]


class MGMSG_MOT_MOVE_HOME(Message):
    id = 0x443
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_MOVE_HOMED(Message):
    id = 0x444
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_SET_MOVERELPARAMS(Message):
    id = 0x445
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('relative_distance', 'i')]


class MGMSG_MOT_REQ_MOVERELPARAMS(Message):
    id = 0x446
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_MOVERELPARAMS(Message):
    id = 0x447
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('relative_distance', 'i')]


class MGMSG_MOT_MOVE_RELATIVE_long(Message):
    id = 0x448
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('relative_distance', 'i')]


class MGMSG_MOT_MOVE_RELATIVE_short(Message):
    id = 0x448
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_SET_MOVEABSPARAMS(Message):
    id = 0x450
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('absolute_position', 'i')]


class MGMSG_MOT_REQ_MOVEABSPARAMS(Message):
    id = 0x451
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_MOVEABSPARAMS(Message):
    id = 0x452
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('absolute_position', 'i')]


class MGMSG_MOT_MOVE_ABSOLUTE_long(Message):
    id = 0x453
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('absolute_distance', 'i')]


class MGMSG_MOT_MOVE_ABSOLUTE_short(Message):
    id = 0x453
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_MOVE_VELOCITY(Message):
    id = 0x457
    parameters = [('chan_ident', 'B'), ('direction', 'B')]


class MGMSG_MOT_MOVE_COMPLETED(Message):
    id = 0x464
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('position', 'i'), (None, 'I'), ('status_bits', 'I')]


class MGMSG_MOT_MOVE_STOP(Message):
    id = 0x465
    parameters = [('chan_ident', 'B'), ('stop_mode', 'B')]


class MGMSG_MOT_MOVE_STOPPED(Message):
    id = 0x466
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('position', 'i'), (None, 'I'), ('status_bits', 'I')]


class MGMSG_MOT_MOVE_JOG(Message):
    id = 0x46a
    parameters = [('chan_ident', 'B'), ('direction', 'B')]


class MGMSG_MOT_SUSPEND_ENDOFMOVEMSGS(Message):
    id = 0x46b

class MGMSG_MOT_RESUME_ENDOFMOVEMSGS(Message):
    id = 0x46c

class MGMSG_MOT_REQ_STATUSUPDATE(Message):
    id = 0x480
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_STATUSUPDATE(Message):
    id = 0x481
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('position', 'i'), ('enc_count', 'I'), ('status_bits', 'I')]


class MGMSG_MOT_REQ_DCSTATUSUPDATE(Message):
    id = 0x490
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_DCSTATUSUPDATE(Message):
    id = 0x491
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('position', 'i'), ('velocity', 'h'), (None, 'H'), ('status_bits', 'I')]


class MGMSG_MOT_ACK_DCSTATUSUPDATE(Message):
    id = 0x492

class MGMSG_MOT_SET_DCPIDPARAMS(Message):
    id = 0x4a0
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('proportional', 'I'), ('integral', 'I'), ('differential', 'I'), ('integral_limit', 'I'), ('filter_control', 'H')]


class MGMSG_MOT_REQ_DCPIDPARAMS(Message):
    id = 0x4a1
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_DCPIDPARAMS(Message):
    id = 0x4a2
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('proportional', 'I'), ('integral', 'I'), ('differential', 'I'), ('integral_limit', 'I'), ('filter_control', 'H')]


class MGMSG_MOT_SET_POTPARAMS(Message):
    id = 0x4b0
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('zero_wnd', 'H'), ('vel1', 'I'), ('wnd1', 'H'), ('vel2', 'I'), ('wnd2', 'H'), ('vel3', 'I'), ('wnd3', 'H'), ('vel4', 'I')]


class MGMSG_MOT_REQ_POTPARAMS(Message):
    id = 0x4b1
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_POTPARAMS(Message):
    id = 0x4b2
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('zero_wnd', 'H'), ('vel1', 'I'), ('wnd1', 'H'), ('vel2', 'I'), ('wnd2', 'H'), ('vel3', 'I'), ('wnd3', 'H'), ('vel4', 'I')]


class MGMSG_MOT_SET_AVMODES(Message):
    id = 0x4b3
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('mode_bits', 'H')]


class MGMSG_MOT_REQ_AVMODES(Message):
    id = 0x4b4
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_AVMODES(Message):
    id = 0x4b5
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('mode_bits', 'H')]


class MGMSG_MOT_SET_BUTTONPARAMS(Message):
    id = 0x4b6
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('mode', 'H'), ('position1', 'i'), ('position2', 'i'), ('timeout', 'H'), (None, 'H')]


class MGMSG_MOT_REQ_BUTTONPARAMS(Message):
    id = 0x4b7
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_BUTTONPARAMS(Message):
    id = 0x4b8
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('mode', 'H'), ('position1', 'i'), ('position2', 'i'), ('timeout', 'H'), (None, 'H')]


class MGMSG_MOT_SET_EEPROMPARAMS(Message):
    id = 0x4b9
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('msg_id', 'H')]


class MGMSG_MOT_SET_SOL_OPERATINGMODE(Message):
    id = 0x4c0
    parameters = [('chan_ident', 'B'), ('mode', 'B')]


class MGMSG_MOT_REQ_SOL_OPERATINGMODE(Message):
    id = 0x4c1
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_SOL_OPERATINGMODE(Message):
    id = 0x4c2
    parameters = [('chan_ident', 'B'), ('mode', 'B')]


class MGMSG_MOT_SET_SOL_CYCLEPARAMS(Message):
    id = 0x4c3
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('on_time', 'I'), ('off_time', 'I'), ('num_cycles', 'I')]


class MGMSG_MOT_REQ_SOL_CYCLEPARAMS(Message):
    id = 0x4c4
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_SOL_CYCLEPARAMS(Message):
    id = 0x4c5
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('on_time', 'I'), ('off_time', 'I'), ('num_cycles', 'I')]


class MGMSG_MOT_SET_SOL_INTERLOCKMODE(Message):
    id = 0x4c6
    parameters = [('chan_ident', 'B'), ('mode', 'B')]


class MGMSG_MOT_SET_SOL_STATE(Message):
    id = 0x4cb
    parameters = [('chan_ident', 'B'), ('state', 'B')]


class MGMSG_MOT_REQ_SOL_INTERLOCKMODE(Message):
    id = 0x4c7
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_SOL_INTERLOCKMODE(Message):
    id = 0x4c8
    parameters = [('chan_ident', 'B'), ('mode', 'B')]


class MGMSG_MOT_REQ_SOL_STATE(Message):
    id = 0x4cc
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_SOL_STATE(Message):
    id = 0x4cd
    parameters = [('chan_ident', 'B'), ('state', 'B')]


class MGMSG_MOT_SET_PMDCURRENTLOOPPARAMS(Message):
    id = 0x4d4
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('phase', 'H'), ('kp_current', 'H'), ('ki_current', 'H'), ('i_lim_current', 'H'), ('i_dead_band', 'H'), ('kff', 'H'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_REQ_PMDCURRENTLOOPPARAMS(Message):
    id = 0x4d5
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_PMDCURRENTLOOPPARAMS(Message):
    id = 0x4d6
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('phase', 'H'), ('kp_current', 'H'), ('ki_current', 'H'), ('i_lim_current', 'H'), ('i_dead_band', 'H'), ('kff', 'H'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_SET_PMDPOSITIONLOOPPARAMS(Message):
    id = 0x4d7
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('kp_pos', 'H'), ('integral', 'H'), ('i_lim_pos', 'I'), ('differential', 'H'), ('kd_time_pos', 'H'), ('k_out_pos', 'H'), ('k_vff_pos', 'H'), ('k_aff_pos', 'H'), ('pos_err_limit', 'I'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_REQ_PMDPOSITIONLOOPPARAMS(Message):
    id = 0x4d8
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_PMDPOSITIONLOOPPARAMS(Message):
    id = 0x4d9
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('kp_pos', 'H'), ('integral', 'H'), ('i_lim_pos', 'I'), ('differential', 'H'), ('kd_time_pos', 'H'), ('k_out_pos', 'H'), ('k_vff_pos', 'H'), ('k_aff_pos', 'H'), ('pos_err_limit', 'I'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_SET_PMDMOTOROUTPUTPARAMS(Message):
    id = 0x4da
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('cont_current_lim', 'H'), ('energy_lim', 'H'), ('motor_lim', 'H'), ('motor_bias', 'H'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_REQ_PMDMOTOROUTPUTPARAMS(Message):
    id = 0x4db
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_PMDMOTOROUTPUTPARAMS(Message):
    id = 0x4dc
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('cont_current_lim', 'H'), ('energy_lim', 'H'), ('motor_lim', 'H'), ('motor_bias', 'H'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_SET_PMDTRACKSETTLEPARAMS(Message):
    id = 0x4e0
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('time', 'H'), ('settle_window', 'H'), ('track_window', 'H'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_REQ_PMDTRACKSETTLEPARAMS(Message):
    id = 0x4e1
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_PMDTRACKSETTLEPARAMS(Message):
    id = 0x4e2
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('time', 'H'), ('settle_window', 'H'), ('track_window', 'H'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_SET_PMDPROFILEMODEPARAMS(Message):
    id = 0x4e3
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('mode', 'H'), ('jerk', 'I'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_REQ_PMDPROFILEMODEPARAMS(Message):
    id = 0x4e4
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_PMDPROFILEMODEPARAMS(Message):
    id = 0x4e5
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('mode', 'H'), ('jerk', 'I'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_SET_PMDJOYSTICKPARAMS(Message):
    id = 0x4e6
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('js_gear_low_max_vel', 'I'), ('js_gear_high_max_vel', 'I'), ('js_gear_low_accn', 'I'), ('js_gear_high_accn', 'I'), ('dir_sense', 'H')]


class MGMSG_MOT_REQ_PMDJOYSTICKPARAMS(Message):
    id = 0x4e7
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_PMDJOYSTICKPARAMS(Message):
    id = 0x4e8
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('js_gear_low_max_vel', 'I'), ('js_gear_high_max_vel', 'I'), ('js_gear_low_accn', 'I'), ('js_gear_high_accn', 'I'), ('dir_sense', 'H')]


class MGMSG_MOT_SET_PMDSETTLEDCURRENTLOOPPARAMS(Message):
    id = 0x4e9
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('phase', 'H'), ('kp_settled', 'H'), ('ki_settled', 'H'), ('i_lim_settled', 'H'), ('dead_band_set', 'H'), ('kff_settled', 'H'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_REQ_PMDSETTLEDCURRENTLOOPPARAMS(Message):
    id = 0x4ea
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_PMDSETTLEDCURRENTLOOPPARAMS(Message):
    id = 0x4eb
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('phase', 'H'), ('kp_settled', 'H'), ('ki_settled', 'H'), ('i_lim_settled', 'H'), ('dead_band_set', 'H'), ('kff_settled', 'H'), (None, 'H'), (None, 'H')]


class MGMSG_MOT_SET_PMDSTAGEAXISPARAMS(Message):
    id = 0x4f0
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('stage_id', 'H'), ('axis_id', 'H'), ('part_no_axis', '16s'), ('serial_num', 'I'), ('cnts_per_unit', 'I'), ('min_pos', 'I'), ('max_pos', 'I'), ('max_accn', 'I'), ('max_dec', 'I'), ('max_vel', 'I'), (None, 'H'), (None, 'H'), (None, 'H'), (None, 'H'), (None, 'I'), (None, 'I'), (None, 'I'), (None, 'I')]


class MGMSG_MOT_REQ_PMDSTAGEAXISPARAMS(Message):
    id = 0x4f1
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_PMDSTAGEAXISPARAMS(Message):
    id = 0x4f2
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('stage_id', 'H'), ('axis_id', 'H'), ('part_no_axis', '16s'), ('serial_num', 'I'), ('cnts_per_unit', 'I'), ('min_pos', 'I'), ('max_pos', 'I'), ('max_accn', 'I'), ('max_dec', 'I'), ('max_vel', 'I'), (None, 'H'), (None, 'H'), (None, 'H'), (None, 'H'), (None, 'I'), (None, 'I'), (None, 'I'), (None, 'I')]


class MGMSG_MOT_SET_BOWINDEX(Message):
    id = 0x4f4
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('bow_index', 'H')]


class MGMSG_MOT_REQ_BOWINDEX(Message):
    id = 0x4f5
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_BOWINDEX(Message):
    id = 0x4f6
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('bow_index', 'H')]


class MGMSG_MOT_SET_TSTACTUATORTYPE(Message):
    id = 0x4fe
    parameters = [('actuator_ident', 'B'), (None, 'B')]


class MGMSG_MOT_SET_TRIGGER(Message):
    id = 0x500
    parameters = [('chan_ident', 'B'), ('mode', 'B')]


class MGMSG_MOT_REQ_TRIGGER(Message):
    id = 0x501
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_TRIGGER(Message):
    id = 0x502
    parameters = [('chan_ident', 'B'), ('mode', 'B')]


class MGMSG_MOT_SET_MFF_OPERPARAMS(Message):
    id = 0x510
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('i_transit_time', 'I'), ('i_transit_time_adc', 'I'), ('oper_mode_1', 'H'), ('sig_mode_1', 'H'), ('pulse_width_1', 'I'), ('oper_mode_2', 'H'), ('sig_mode_2', 'H'), ('pulse_width_2', 'I'), (None, 'I'), (None, 'H')]


class MGMSG_MOT_REQ_MFF_OPERPARAMS(Message):
    id = 0x511
    parameters = [('chan_ident', 'B'), (None, 'B')]


class MGMSG_MOT_GET_MFF_OPERPARAMS(Message):
    id = 0x512
    is_long_cmd = True
    parameters = [('chan_ident', 'H'), ('i_transit_time', 'I'), ('i_transit_time_adc', 'I'), ('oper_mode_1', 'H'), ('sig_mode_1', 'H'), ('pulse_width_1', 'I'), ('oper_mode_2', 'H'), ('sig_mode_2', 'H'), ('pulse_width_2', 'I'), (None, 'I'), (None, 'H')]
