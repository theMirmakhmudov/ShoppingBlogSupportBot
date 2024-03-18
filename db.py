import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(255),
    username VARCHAR(255),
    user_id INTEGER
     )
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS feedbacks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR(255),
phone_number VARCHAR(255),
type VARCHAR(255),
code VARCHAR(255),
price VARCHAR(255),
fixed VARCHAR(255) NOT NULL

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ideas(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR(255) NOT NULL,
username VARCHAR(255) NOT NULL,
idea VARCHAR(255) NOT NULL

)''')
conn.commit()  # Commit change database


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, full_name, username, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO users (full_name, username, user_id) VALUES (?, ?, ?)',
                                       (full_name, username, user_id))

    def check_user(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()


class Database2:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, fullname, phone_number, type, code, price, fixed):
        with self.connection:
            return self.cursor.execute(
                'INSERT INTO feedbacks (fullname, phone_number, type, code,price, fixed) VALUES (?, ?, ?, ?, ?, ?)',
                (fullname, phone_number, type, code, price, fixed))


conn.close()  # Closing database connection


class Database3:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, fullname, username, idea):
        with self.connection:
            return self.cursor.execute(
                'INSERT INTO ideas(fullname, username, idea) VALUES (?,?,?)',
                (fullname, username, idea))


conn.close()  # Closing database connection
