import os
import json
from PySide6.QtWidgets import QMessageBox
from i18n import t
try:
    from palworld_aio import constants
    from palworld_aio.utils import are_equal_uuids, as_uuid, sav_to_json, json_to_sav
    from palworld_aio.data_manager import delete_player
except ImportError:
    from . import constants
    from .utils import are_equal_uuids, as_uuid, sav_to_json, json_to_sav
    from .data_manager import delete_player
def _load_exp_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    exp_file = os.path.join(base_dir, 'resources', 'game_data', 'pal_exp_table.json')
    try:
        with open(exp_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f'Error loading EXP_DATA from {exp_file}: {e}')
        return {}
EXP_DATA = _load_exp_data()
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
                if 'Level' not in sp_val:
                    from i18n import t
                    QMessageBox.warning(None, t('player.level.set_no_level_title') if t else 'Cannot Set Level', t('player.level.set_no_level_data') if t else 'This player has not leveled up yet. Please have them level up in-game first before using this tool.')
                    return False
                sp_val['Level']['value']['value'] = new_level
                if 'Exp' not in sp_val:
                    sp_val['Exp'] = {'value': EXP_DATA[str(new_level)]['TotalEXP']}
                else:
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