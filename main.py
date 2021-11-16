import sqlite3
import sys

conn = sqlite3.connect('db_hero/heroes.db', check_same_thread=False) # ...=False --> don't while check
cursor = conn.cursor()


def get_info(hero):
    conn = sqlite3.connect('db_hero/heroes.db', check_same_thread=False) # ...=False --> don't while check
    cursor = conn.cursor()

    # возврат описания героя по аргументу hero, все герои представлены в бд в колонке hero
    cursor.execute("select hero_info from heroes_dnd where hero=:hero", {"hero": hero})
    hero_info = cursor.fetchall()
    hero_info = hero_info[0][0] # вывод описания в формате str

    return hero_info


conn.close()
