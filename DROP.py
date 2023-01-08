import sqlite3

try:
    sqlite_connection = sqlite3.connect('database.db')
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")



    sqlite_drop_table = """DROP TABLE pi_1_19_students ; """  
    cursor.execute(sqlite_drop_table)

    sqlite_connection.commit()
    print("Таблица удалена")


    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")