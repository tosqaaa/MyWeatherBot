import sqlite3


def create_db():
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        count INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER UNIQUE NOT NULL,
        user_name TEXT NOT NULL,
        user_nick TEXT);
    """)
    conn.commit()


def insert_db(user_id: int, user_name: str, user_nickname: str):
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute("INSERT or IGNORE INTO users(user_id, user_name, user_nick) VALUES (?,?,?)", (user_id, user_name,
                                                                                                 user_nickname))
    conn.commit()
