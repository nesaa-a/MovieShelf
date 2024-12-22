import sqlite3

def get_connection():
    return sqlite3.connect("movies.db")

def create_database():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        """)
        conn.commit()
