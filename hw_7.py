import sqlite3

with sqlite3.connect('students.db') as conn:
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS students (
    id_hobby INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    born_year INTEGER NOT NULL,
    mark INTEGER
    )''')

    # c.execute('''
    # INSERT INTO students (name, surname, born_year, mark) VALUES
    # ('Ars','Boloev',2004,6),
    # ('Argen','Baltbaev',2004,12),
    # ('Adina','Believa',2005,9),
    # ('Akes','Akaev',2004,11),
    # ('Timu','Chin',1678,10),
    # ('Janna','Dark',1456,8),
    # ('Mohito','Pepsi',1996,17),
    # ('Sun','Zhi',1452,18),
    # ('Alla','Pugachova',1984,7),
    # ('Alina','Asenova',2004,9)
    # ''')

    c.execute('''SELECT * FROM students WHERE length(name) >= 10''')
    for i in c.fetchall():
        print(i)

    c.execute('''UPDATE students SET name = 'Genius' WHERE mark >= 10''')

    c.execute('''SELECT * FROM students''')
    for i in c.fetchall():
        print(i)

