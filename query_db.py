# Импорт библиотеки
import sqlite3

con = sqlite3.connect("films_db.sqlite")
cur = con.cursor()


def select_table(table_name, *fields):
    query = f"""SELECT {', '.join(fields)} FROM {table_name}"""
    return cur.execute(query).fetchall()


if __name__ == '__main__':
    print(*select_table('films', 'title', 'year'), sep='\n')