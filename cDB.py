import sqlite3

try:
    sqlite_connection = sqlite3.connect('database.db')
    sqlite_create_table_query = '''CREATE TABLE pi_1_19_students (
                                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
