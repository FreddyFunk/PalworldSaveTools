import os
from i18n import t
try:
    from palworld_aio import constants
    from palworld_aio.utils import are_equal_uuids, as_uuid, sav_to_json, json_to_sav
    from palworld_aio.data_manager import delete_player
except ImportError:
    from . import constants
    from .utils import are_equal_uuids, as_uuid, sav_to_json, json_to_sav
    from .data_manager import delete_player
def rename_player(player_uid, new_name):
    if not constants.loaded_level_json:
        return False
    p_uid_clean = str(player_uid).replace('-', '')
    wsd = constants.loaded_level_json['properties']['worldSaveData']['value']
    for g in wsd['GroupSaveDataMap']['value']:
        raw = g['value']['RawData']['value']
        found = False
        for p in raw.get('players', []):
            uid = str(p.get('player_uid', '')).replace('-', '')
            if uid == p_uid_clean:
                p.setdefault('player_info', {})['player_name'] = new_name
                found = True
                break
        if found:
            break
    char_map = wsd.get('CharacterSaveParameterMap', {}).get('value', [])
    for entry in char_map:
        raw = entry.get('value', {}).get('RawData', {}).get('value', {})
        sp_val = raw.get('object', {}).get('SaveParameter', {}).get('value', {})
        if sp_val.get('IsPlayer', {}).get('value'):
            uid_obj = entry.get('key', {}).get('PlayerUId', {})
            uid = str(uid_obj.get('value', '')).replace('-', '') if isinstance(uid_obj, dict) else ''
            if uid == p_uid_clean:
                sp_val.setdefault('NickName', {})['value'] = new_name
                break
    return True
def get_player_info(player_uid):
    if not constants.loaded_level_json:
        return None
    uid_clean = str(player_uid).replace('-', '').lower()
    wsd = constants.loaded_level_json['properties']['worldSaveData']['value']
    tick = wsd['GameTimeSaveData']['value']['RealDateTimeTicks']['value']
    for g in wsd['GroupSaveDataMap']['value']:
        if g['value']['GroupType']['value']['value'] != 'EPalGroupType::Guild':
            continue
        gid = str(g['key'])
        gname = g['value']['RawData']['value'].get('guild_name', 'Unknown Guild')
        for p in g['value']['RawData']['value'].get('players', []):
            uid = str(p.get('player_uid', '')).replace('-', '').lower()
            if uid == uid_clean:
                name = p.get('player_info', {}).get('player_name', 'Unknown')
                last = p.get('player_info', {}).get('last_online_real_time')
                from .utils import format_duration_short
                lastseen = 'Unknown' if last is None else format_duration_short((tick - last) / 10000000.0)
                level = constants.player_levels.get(uid, '?')
                pals = constants.PLAYER_PAL_COUNTS.get(uid, 0)
                return {'uid': player_uid, 'name': name, 'level': level, 'pals': pals, 'lastseen': lastseen, 'guild_id': gid, 'guild_name': gname}
    return None
def get_player_pal_count(player_uid):
    uid = str(player_uid).replace('-', '').lower()
    return constants.PLAYER_PAL_COUNTS.get(uid, 0)
def unlock_viewing_cage(player_uid):
    if not constants.current_save_path:
        return False
    uid_clean = str(player_uid).replace('-', '')
    sav_file = os.path.join(constants.current_save_path, 'Players', f'{uid_clean}.sav')
    if not os.path.exists(sav_file):
        return False
    try:
        p_json = sav_to_json(sav_file)
        save_data = p_json.get('properties', {}).get('SaveData', {}).get('value', {})
        if 'bIsViewingCageCanUse' not in save_data:
            return False
        save_data['bIsViewingCageCanUse']['value'] = True
        json_to_sav(p_json, sav_file)
        return True
    except Exception as e:
        print(f'Error unlocking viewing cage: {e}')
        return False
EXP_DATA = {'1': {'DropEXP': 7, 'NextEXP': 0, 'PalNextEXP': 0, 'TotalEXP': 0, 'PalTotalEXP': 0}, '2': {'DropEXP': 9, 'NextEXP': 8, 'PalNextEXP': 25, 'TotalEXP': 8, 'PalTotalEXP': 25}, '3': {'DropEXP': 11, 'NextEXP': 30, 'PalNextEXP': 31, 'TotalEXP': 38, 'PalTotalEXP': 56}, '4': {'DropEXP': 13, 'NextEXP': 98, 'PalNextEXP': 37, 'TotalEXP': 136, 'PalTotalEXP': 93}, '5': {'DropEXP': 15, 'NextEXP': 180, 'PalNextEXP': 45, 'TotalEXP': 316, 'PalTotalEXP': 138}, '6': {'DropEXP': 17, 'NextEXP': 278, 'PalNextEXP': 69, 'TotalEXP': 593, 'PalTotalEXP': 207}, '7': {'DropEXP': 20, 'NextEXP': 395, 'PalNextEXP': 99, 'TotalEXP': 988, 'PalTotalEXP': 306}, '8': {'DropEXP': 23, 'NextEXP': 536, 'PalNextEXP': 134, 'TotalEXP': 1524, 'PalTotalEXP': 440}, '9': {'DropEXP': 26, 'NextEXP': 705, 'PalNextEXP': 176, 'TotalEXP': 2229, 'PalTotalEXP': 616}, '10': {'DropEXP': 38, 'NextEXP': 908, 'PalNextEXP': 227, 'TotalEXP': 3138, 'PalTotalEXP': 843}, '11': {'DropEXP': 45, 'NextEXP': 1152, 'PalNextEXP': 288, 'TotalEXP': 4290, 'PalTotalEXP': 1131}, '12': {'DropEXP': 52, 'NextEXP': 1444, 'PalNextEXP': 361, 'TotalEXP': 5734, 'PalTotalEXP': 1492}, '13': {'DropEXP': 58, 'NextEXP': 1795, 'PalNextEXP': 449, 'TotalEXP': 7529, 'PalTotalEXP': 1941}, '14': {'DropEXP': 66, 'NextEXP': 2216, 'PalNextEXP': 554, 'TotalEXP': 9745, 'PalTotalEXP': 2495}, '15': {'DropEXP': 74, 'NextEXP': 2721, 'PalNextEXP': 680, 'TotalEXP': 12467, 'PalTotalEXP': 3175}, '16': {'DropEXP': 84, 'NextEXP': 3328, 'PalNextEXP': 832, 'TotalEXP': 15795, 'PalTotalEXP': 4007}, '17': {'DropEXP': 97, 'NextEXP': 4055, 'PalNextEXP': 1014, 'TotalEXP': 19850, 'PalTotalEXP': 5021}, '18': {'DropEXP': 110, 'NextEXP': 4928, 'PalNextEXP': 1232, 'TotalEXP': 24778, 'PalTotalEXP': 6253}, '19': {'DropEXP': 124, 'NextEXP': 5976, 'PalNextEXP': 1494, 'TotalEXP': 30754, 'PalTotalEXP': 7747}, '20': {'DropEXP': 138, 'NextEXP': 7233, 'PalNextEXP': 1808, 'TotalEXP': 37988, 'PalTotalEXP': 9555}, '21': {'DropEXP': 153, 'NextEXP': 8742, 'PalNextEXP': 2185, 'TotalEXP': 46730, 'PalTotalEXP': 11740}, '22': {'DropEXP': 171, 'NextEXP': 10552, 'PalNextEXP': 2638, 'TotalEXP': 57282, 'PalTotalEXP': 14378}, '23': {'DropEXP': 194, 'NextEXP': 12725, 'PalNextEXP': 3181, 'TotalEXP': 70007, 'PalTotalEXP': 17559}, '24': {'DropEXP': 217, 'NextEXP': 15332, 'PalNextEXP': 3833, 'TotalEXP': 85338, 'PalTotalEXP': 21392}, '25': {'DropEXP': 241, 'NextEXP': 18460, 'PalNextEXP': 4615, 'TotalEXP': 103799, 'PalTotalEXP': 26007}, '26': {'DropEXP': 267, 'NextEXP': 22214, 'PalNextEXP': 5554, 'TotalEXP': 126013, 'PalTotalEXP': 31561}, '27': {'DropEXP': 300, 'NextEXP': 26719, 'PalNextEXP': 6680, 'TotalEXP': 152732, 'PalTotalEXP': 38241}, '28': {'DropEXP': 337, 'NextEXP': 32125, 'PalNextEXP': 8031, 'TotalEXP': 184856, 'PalTotalEXP': 46272}, '29': {'DropEXP': 374, 'NextEXP': 38612, 'PalNextEXP': 9653, 'TotalEXP': 223468, 'PalTotalEXP': 55925}, '30': {'DropEXP': 417, 'NextEXP': 46396, 'PalNextEXP': 11599, 'TotalEXP': 269864, 'PalTotalEXP': 67524}, '31': {'DropEXP': 467, 'NextEXP': 55737, 'PalNextEXP': 13934, 'TotalEXP': 325601, 'PalTotalEXP': 81458}, '32': {'DropEXP': 518, 'NextEXP': 66947, 'PalNextEXP': 16737, 'TotalEXP': 392548, 'PalTotalEXP': 98195}, '33': {'DropEXP': 580, 'NextEXP': 80398, 'PalNextEXP': 20099, 'TotalEXP': 472946, 'PalTotalEXP': 118294}, '34': {'DropEXP': 647, 'NextEXP': 96540, 'PalNextEXP': 24135, 'TotalEXP': 569485, 'PalTotalEXP': 142429}, '35': {'DropEXP': 719, 'NextEXP': 115909, 'PalNextEXP': 28977, 'TotalEXP': 685395, 'PalTotalEXP': 171406}, '36': {'DropEXP': 806, 'NextEXP': 139153, 'PalNextEXP': 34788, 'TotalEXP': 824548, 'PalTotalEXP': 206194}, '37': {'DropEXP': 896, 'NextEXP': 167046, 'PalNextEXP': 41761, 'TotalEXP': 991594, 'PalTotalEXP': 247955}, '38': {'DropEXP': 1003, 'NextEXP': 200517, 'PalNextEXP': 50129, 'TotalEXP': 1192111, 'PalTotalEXP': 298084}, '39': {'DropEXP': 1118, 'NextEXP': 240683, 'PalNextEXP': 60171, 'TotalEXP': 1432794, 'PalTotalEXP': 358255}, '40': {'DropEXP': 1249, 'NextEXP': 288881, 'PalNextEXP': 72220, 'TotalEXP': 1721675, 'PalTotalEXP': 430475}, '41': {'DropEXP': 1394, 'NextEXP': 346719, 'PalNextEXP': 86680, 'TotalEXP': 2068394, 'PalTotalEXP': 517155}, '42': {'DropEXP': 1554, 'NextEXP': 416125, 'PalNextEXP': 104031, 'TotalEXP': 2484520, 'PalTotalEXP': 621186}, '43': {'DropEXP': 1736, 'NextEXP': 499412, 'PalNextEXP': 124853, 'TotalEXP': 2983932, 'PalTotalEXP': 746039}, '44': {'DropEXP': 1940, 'NextEXP': 599357, 'PalNextEXP': 149839, 'TotalEXP': 3583289, 'PalTotalEXP': 895878}, '45': {'DropEXP': 2168, 'NextEXP': 719290, 'PalNextEXP': 179823, 'TotalEXP': 4302579, 'PalTotalEXP': 1075701}, '46': {'DropEXP': 2422, 'NextEXP': 863210, 'PalNextEXP': 215803, 'TotalEXP': 5165789, 'PalTotalEXP': 1291504}, '47': {'DropEXP': 2704, 'NextEXP': 1035914, 'PalNextEXP': 258979, 'TotalEXP': 6201703, 'PalTotalEXP': 1550483}, '48': {'DropEXP': 3018, 'NextEXP': 1243159, 'PalNextEXP': 310790, 'TotalEXP': 7444862, 'PalTotalEXP': 1861273}, '49': {'DropEXP': 3374, 'NextEXP': 1491853, 'PalNextEXP': 372963, 'TotalEXP': 8936715, 'PalTotalEXP': 2234236}, '50': {'DropEXP': 3774, 'NextEXP': 1790285, 'PalNextEXP': 447571, 'TotalEXP': 10727001, 'PalTotalEXP': 2681807}, '51': {'DropEXP': 4218, 'NextEXP': 2148405, 'PalNextEXP': 537101, 'TotalEXP': 12875405, 'PalTotalEXP': 3218908}, '52': {'DropEXP': 4718, 'NextEXP': 2578147, 'PalNextEXP': 644537, 'TotalEXP': 15453553, 'PalTotalEXP': 3863445}, '53': {'DropEXP': 5271, 'NextEXP': 3093839, 'PalNextEXP': 773460, 'TotalEXP': 18547392, 'PalTotalEXP': 4636905}, '54': {'DropEXP': 5897, 'NextEXP': 3712669, 'PalNextEXP': 928167, 'TotalEXP': 22260061, 'PalTotalEXP': 5565072}, '55': {'DropEXP': 6592, 'NextEXP': 4455265, 'PalNextEXP': 1113816, 'TotalEXP': 26715325, 'PalTotalEXP': 6678888}, '56': {'DropEXP': 7374, 'NextEXP': 5346379, 'PalNextEXP': 1336595, 'TotalEXP': 32061705, 'PalTotalEXP': 8015483}, '57': {'DropEXP': 8248, 'NextEXP': 6415717, 'PalNextEXP': 1603929, 'TotalEXP': 38477422, 'PalTotalEXP': 9619412}, '58': {'DropEXP': 9227, 'NextEXP': 7698923, 'PalNextEXP': 1924731, 'TotalEXP': 46176345, 'PalTotalEXP': 11544143}, '59': {'DropEXP': 12227, 'NextEXP': 9238769, 'PalNextEXP': 2309692, 'TotalEXP': 55415114, 'PalTotalEXP': 13853835}, '60': {'DropEXP': 15227, 'NextEXP': 11086585, 'PalNextEXP': 2771646, 'TotalEXP': 66501699, 'PalTotalEXP': 16625481}, '61': {'DropEXP': 18227, 'NextEXP': 13303964, 'PalNextEXP': 3325991, 'TotalEXP': 79805663, 'PalTotalEXP': 19951472}, '62': {'DropEXP': 21227, 'NextEXP': 15964819, 'PalNextEXP': 3991205, 'TotalEXP': 95770482, 'PalTotalEXP': 23942677}, '63': {'DropEXP': 24227, 'NextEXP': 19157845, 'PalNextEXP': 4789461, 'TotalEXP': 114928327, 'PalTotalEXP': 28732138}, '64': {'DropEXP': 27227, 'NextEXP': 22989476, 'PalNextEXP': 5747369, 'TotalEXP': 137917803, 'PalTotalEXP': 34479507}, '65': {'DropEXP': 30227, 'NextEXP': 27587433, 'PalNextEXP': 6896858, 'TotalEXP': 165505236, 'PalTotalEXP': 41376365}}
def get_level_from_exp(exp):
    for level in range(65, 0, -1):
        if exp >= EXP_DATA[str(level)]['TotalEXP']:
            return level
    return 1
def set_player_level(player_uid, new_level):
    if not constants.loaded_level_json:
        return False
    if new_level < 1 or new_level > 65:
        return False
    uid_clean = str(player_uid).replace('-', '')
    wsd = constants.loaded_level_json['properties']['worldSaveData']['value']
    char_map = wsd.get('CharacterSaveParameterMap', {}).get('value', [])
    for entry in char_map:
        raw = entry.get('value', {}).get('RawData', {}).get('value', {})
        sp_val = raw.get('object', {}).get('SaveParameter', {}).get('value', {})
        if sp_val.get('IsPlayer', {}).get('value'):
            uid_obj = entry.get('key', {}).get('PlayerUId', {})
            uid = str(uid_obj.get('value', '')).replace('-', '') if isinstance(uid_obj, dict) else ''
            if uid == uid_clean:
                sp_val['Level']['value']['value'] = new_level
                sp_val['Exp']['value'] = EXP_DATA[str(new_level)]['TotalEXP']
                constants.player_levels[uid] = new_level
                return True
    return False
def adjust_player_level(player_uid, target_level):
    if target_level < 1 or target_level > 65:
        return False
    current_level = constants.player_levels.get(str(player_uid).replace('-', ''), 1)
    if current_level == target_level:
        return True
    return set_player_level(player_uid, target_level)