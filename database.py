import sqlite3

def create_database():

    conn= sqlite3.connect("movie.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KET AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT NOT NULL,
            year INTEGER NOT NULL,
            genre TEXT
       )
    """)
    conn.comit()
    conn.close()

def get_connection():
    return sqlite3.connect("movies.db")


