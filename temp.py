import sqlite3

def connection(username):
    conn = sqlite3.connect('Snake Game.db')
    cursorObj = conn.cursor()
    listTables = conn.execute(""" 
    SELECT name FROM sqlite_master WHERE type='table'AND name='users';""").fetchall()
    if listTables != []:
        print('Table exists.')
    else:
        cursorObj.execute("""CREATE TABLE users (
                                id INTEGER PRIMARY KEY,
                                username text
                             )""")

    sqlite_insert_with_param = f"""INSERT INTO users
                              (username) 
                              VALUES ("{username}");"""
    cursorObj.execute(sqlite_insert_with_param)
    conn.commit()
    conn.close()