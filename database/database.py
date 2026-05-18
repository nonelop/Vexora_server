import sqlite3


def connect_database():
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    return connection, cursor


def write_new_user(username: str, reg_time: str):
    conn, cursor = connect_database()

    cursor.execute(
        """INSERT OR IGNORE INTO users (username, reg_time) VALUES (?, ?)""",
        (username, reg_time),
    )
    conn.commit()
    conn.close()


def check_username(username: str):
    conn, cursor = connect_database()

    cursor.execute("""SELECT username FROM users WHERE username = ?""", (username,))

    result = cursor.fetchone()

    if result:
        is_exist = True
    else:
        is_exist = False

    conn.close()

    return is_exist


def write_new_token(data: tuple):
    conn, cursor = connect_database()

    cursor.execute("""INSERT INTO tokens (user_id, token_hash) VALUES (?, ?)""", data)
    conn.commit()
    conn.close()


def check_tokens(user_id: int):

    conn, cursor = connect_database()

    cursor.execute("""SELECT token_hash FROM tokens WHERE user_id = ?""", (user_id,))

    result = cursor.fetchall()

    conn.close()

    if result:
        return result
    else:
        return False


def write_new_message(from_user_id: int, chat_id: int, content_type: str, text):

    conn, cursor = connect_database()

    cursor.execute(
        """INSERT INTO messages (from_user_id, chat_id, content_type, text) VALUES (?, ?, ?, ?)""",
        (from_user_id, chat_id, content_type, text),
    )

    conn.commit()
    conn.close()
