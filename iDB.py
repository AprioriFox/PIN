import sqlite3

def insert_student(name, email):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_with_param = """INSERT INTO pi_1_19_students
                              (name, email)
                              VALUES (?, ?);"""

        data_tuple = (name, email)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу pi_1_19_students")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

insert_student('Kirill', 'apriorifox@gmail.com')
insert_student('Aziza','aziza@gmail.com')
insert_student('Tumar','tumar@gmail.com')
insert_student('Meikin','meikin@gmail.com')
insert_student('Mikhail','misha@gmail.com')

