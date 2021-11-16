import sqlite3
import sys

conn = sqlite3.connect('db/dnd_db.db', check_same_thread=False) # ...=False --> don't while check
cursor = conn.cursor()


def get_setting(mapn):
    conn = sqlite3.connect('db/dnd_db.db', check_same_thread=False) # ...=False --> don't while check
    cursor = conn.cursor()
    cursor.execute("select setting from set_map where maps=:mapn", {"mapn": mapn})
    setting = cursor.fetchone()
    return setting[0][0]


def get_maps(setting):
    conn = sqlite3.connect('db/dnd_db.db', check_same_thread=False) # ...=False --> don't while check
    cursor = conn.cursor()
    cursor.execute("select maps from set_map where setting=:setting", {"setting": setting})
    maps = cursor.fetchall()
    maps = [x[0] for x in maps]
    maps = ', '.join(maps)
    return maps


def get_info(mapn):
    conn = sqlite3.connect('db/dnd_db.db', check_same_thread=False) # ...=False --> don't while check
    cursor = conn.cursor()
    cursor.execute("select maps_info from set_map where maps=:mapn", {"mapn": mapn})
    info = cursor.fetchall()
    return info[0][0]


conn.close()
