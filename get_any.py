import sqlite3
import sys

conn = sqlite3.connect('db/info_settings.db', check_same_thread=False) # ...=False --> don't while check
cursor = conn.cursor()


def get_setting(mapn = None) -> str or list:
    """Возвращает сеттинг по мапу.
    Если в аргументы нчиего не передано, то функция возращает список все сеттинги"""
    if mapn is not None:
        cursor.execute("select setting from set_map where maps=:mapn", {"mapn": mapn})
        setting = cursor.fetchall()
        settings = setting[0][0]
    else:
        cursor.execute("select setting from set_map")
        setting = cursor.fetchall()
        settings = list({e for l in setting for e in l})


    return settings # return str


def get_maps(setting = None) -> str:
    '''Возвращает мапы по сеттингу sep=";"'''
    if setting is not None:
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


def get_hero_info(hero=None) -> str or None:
    """Функция возращает описание неигровго персонажа.
    Если персонажа нет в БД, функция возращает None"""
    if hero is not None:
        try:
            cursor.execute("select hero_info from heroes_dnd where hero=:hero", {"hero": hero})
            hero_info = cursor.fetchall()
            hero_info = hero_info[0][0]
        except IndexError:
            return None
    else:
        cursor.execute("SELECT hero_info FROM heroes_dnd")
        hero_info = cursor.fetchall()
        # hero_info = hero_info[0][0]

    return hero_info # return in str

if __name__ == "__main__":
    print('def get_setting: ', get_setting())
    print('def get_maps: ', get_maps())
    print('def get_item_info: ', get_maps_info('Nirn'))
    print('def get_hero_info: ', get_hero_info('Вампиры'))


#conn.close()