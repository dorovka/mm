import sqlite3

def create(cursor):
    cursor.execute(''' CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    gender TEXT); ''')

def select(cursor):
    inf = cursor.execute('SELECT * FROM users;')
    result = inf.fetchall()
    return result

def insert(cursor, name, surname, gender):
    cursor.execute("INSERT INTO users (name, surname, gender) VALUES (?, ?, ?);", (name, surname, gender))
    #cursor.execute("INSERT INTO users (name, surname, gender) VALUES ('{}', '{}', '{}');")

def select_id(cursor, id_):
    inf = cursor.execute('SELECT * FROM USERS WHERE id = ?;', (id_,)) #запятая важна, чтобы получился кортеж (только на нём работает fetchall, нужный для работы с бд)
    result = inf.fetchall()
    return result

def select_gender(cursor, gender):
    inf = cursor.execute('SELECT * FROM USERS WHERE gender = ?;', (gender,))
    result = inf.fetchall()
    return result

def dele(cursor, id_):
    cursor.execute('DELETE FROM USERS WHERE id = ?;', (id_,))

with sqlite3.connect('G:\Godnota\prochee\python2\Repet\data.db') as cursor:
    #print(select(cursor))
    #insert(cursor, 'Bob', 'lol', 'M')
    #print(select(cursor))
    #print(select_id(cursor, 1))
    #dele(cursor)
    #print(select_gender(cursor, 'M'))
    #for i in range(3):
    #    insert(cursor, f'Bob{i}', 'lol', 'M')
    print(select_gender(cursor, 'M'))
    dele(cursor, 1)
    print(select(cursor))