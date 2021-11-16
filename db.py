import sqlite3
import sys

conn = sqlite3.connect('db/dnd_db.db', check_same_thread=False) # ...=False --> don't while check
cursor = conn.cursor()


def get_setting(mapn = 0) -> str:
    """Возвращает сеттинг по мапу"""
    conn = sqlite3.connect('db/dnd_db.db', check_same_thread=False) # ...=False --> don't while check
    cursor = conn.cursor()
    if mapn != 0:
        cursor.execute("select setting from set_map where maps=:mapn", {"mapn": mapn})
        setting = cursor.fetchall()
        setting = setting[0][0]
    else:
        cursor.execute("select setting from set_map")
        setting = cursor.fetchall()
        settings = {e for l in setting for e in l}


    return settings


def get_maps(setting = 0) -> str:
    '''Возвращает мапы по сеттингу sep=";"'''
    conn = sqlite3.connect('db/dnd_db.db', check_same_thread=False) # ...=False --> don't while check
    cursor = conn.cursor()
    if setting != 0:
        cursor.execute("select maps from set_map where setting=:setting", {"setting": setting})
        maps = cursor.fetchall()
        maps = [x[0] for x in maps]
        # maps = ';'.join(maps)
    else:
        cursor.execute("select maps from set_map")
        maps = cursor.fetchall()
        maps = [x[0] for x in maps]

    return maps


def get_info(mapn) -> str:
    """Возвращает информацию о локации и сеттинге"""
    conn = sqlite3.connect('db/dnd_db.db', check_same_thread=False) # ...=False --> don't while check
    cursor = conn.cursor()
    cursor.execute("select maps_info from set_map where maps=:mapn", {"mapn": mapn})
    info = cursor.fetchall()

    
    return info[0][0]


conn.close()
