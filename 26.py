import sqlite3

'''try:
    connection = sqlite3.connect('G:\Godnota\prochee\python2\Repet\data.db')
except sqlite3.DatabaseError:
    print('Error')
finally:
    print('all good')
    connection.close()'''


with sqlite3.connect('G:\Godnota\prochee\python2\Repet\data.db') as cursor:
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    gender TEXT);""")



with sqlite3.connect('G:\Godnota\prochee\python2\Repet\data.db') as cursor:
    print(cursor)
    cursor.execute("INSERT INTO users (name, surname, gender) VALUES ('artem', 'sim', 'M');")