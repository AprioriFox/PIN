import sqlite3

try:
    sqlite_connection = sqlite3.connect('database.db')
    sqlite_select_from_table = """SELECT * FROM pi_1_19_students;"""

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_select_from_table)

    records = cursor.fetchall()
    print("\n")
    print("Всего строк:  ", len(records))
    print("\n")
    for row in records:
        print("Id: ", row[0])
        print("Name: ", row[1])
        print("Email: ", row[2])
        print("\n")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
