
import sqlite3

DATABASE_NAME = "smartfoot.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def create_tables():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            home_team TEXT NOT NULL,
            away_team TEXT NOT NULL,
            competition TEXT NOT NULL,
            minute INTEGER NOT NULL
        )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        event_type TEXT NOT NULL,
        minute INTEGER NOT NULL,
        description TEXT NOT NULL,
        FOREIGN KEY (match_id) REFERENCES matches(id)
             )
                """)

    connection.commit()
    connection.close()


