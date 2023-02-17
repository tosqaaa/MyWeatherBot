import sqlite3


def create_db():
    try:
        conn = sqlite3.connect('users.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        user_name TEXT NOT NULL,
        user_nick TEXT,
        user_language TEXT);
        """)
        conn.commit()
    except sqlite3.Error as er:
        print(er)
    finally:
        conn.close()


def insert_db(user_id: int, user_name: str, user_nickname: str):
    try:
        conn = sqlite3.connect('users.db', check_same_thread=False)
        cursor = conn.cursor()

        cursor.execute("INSERT or IGNORE INTO users(user_id, user_name, user_nick) VALUES (?,?,?)", (user_id, user_name,
                                                                                                 user_nickname))
        conn.commit()
        cursor.close()
    except sqlite3.Error as er:
        print(er)
    
    finally:
        conn.close()
    
def change_language_in_db(user_id: int, user_language: str):
    try:
        conn = sqlite3.connect('users.db', check_same_thread=False)
        cursor = conn.cursor()
    
        cursor.execute("""UPDATE users SET user_language = ? WHERE user_id = ?""",(user_language, user_id))
        conn.commit()
    
        cursor.close()
    except sqlite3.Error as er:
        print(er)
    finally:
        conn.close()
        
def get_language_from_user(user_id: int):
    try:
        conn = sqlite3.connect('users.db', check_same_thread=False)
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM users where user_id = ?""",(user_id, ))
        
        selected_language = cursor.fetchone()
        return selected_language[3]
        
    except sqlite3.Error as er:
        print(er)
    finally:
        cursor.close()
        conn.close()
