import sqlite3
import sys

conn = sqlite3.connect('db/info_settings.db', check_same_thread=False) # ...=False --> don't while check
cursor = conn.cursor()


def get_setting(mapn = 0) -> str:
    """Возвращает сеттинг по мапу"""
    if mapn != 0:
        cursor.execute("select setting from set_map where maps=:mapn", {"mapn": mapn})
        setting = cursor.fetchall()
        setting = setting[0][0]
    else:
        cursor.execute("select setting from set_map")
        setting = cursor.fetchall()
        settings = {e for l in setting for e in l}


    return settings # return in set() format str


def get_maps(setting = 0) -> str:
    '''Возвращает мапы по сеттингу sep=";"'''
    if setting != 0:
        cursor.execute("select maps from set_map where setting=:setting", {"setting": setting})
        maps = cursor.fetchall()
        maps = [x[0] for x in maps]
        maps = ';'.join(maps)
    else:
        cursor.execute("select maps from set_map")
        maps = cursor.fetchall()
        maps = [x[0] for x in maps]
        maps = ';'.join(maps)

    return maps # return in str, separated ;


def get_maps_info(mapn) -> str:
    """Возвращает информацию о локации и сеттинге"""
    cursor.execute("select maps_info from set_map where maps=:mapn", {"mapn": mapn})
    info = cursor.fetchall()

    
    return info[0][0] # return in str


def get_hero_info(hero=0):
    if hero != 0:
        cursor.execute("select hero_info from heroes_dnd where hero=:hero", {"hero": hero})
        hero_info = cursor.fetchall()
        hero_info = hero_info[0][0]
    else:
        cursor.execute("SELECT hero_info FROM heroes_dnd")
        hero_info = cursor.fetchall()
        # hero_info = hero_info[0][0]

    return hero_info # return in str (if hero=0)


'''
print('def get_setting: ', get_setting())
print('def get_maps: ', get_maps())
print('def get_item_info: ', get_maps_info('Nirn'))
print('def get_hero_info: ', get_hero_info('Вампиры'))
'''

conn.close()
