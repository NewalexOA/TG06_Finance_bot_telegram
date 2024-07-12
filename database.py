import sqlite3


def init_db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY,
       telegram_id INTEGER UNIQUE,
       name TEXT,
       category1 TEXT,
       category2 TEXT,
       category3 TEXT,
       expenses1 REAL,
       expenses2 REAL,
       expenses3 REAL
       )
    ''')

    conn.commit()
    return conn, cursor


def get_connection_and_cursor():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    return conn, cursor


def close_connection(conn):
    conn.close()
