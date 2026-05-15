import sqlite3


def connect_database():
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    return connection, cursor


def write_new_user(data: tuple):
    conn, cursor = connect_database()

    cursor.execute(
        """INSERT OR IGNORE INTO users (username,) VALUES (?,)""", data
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

    cursor.execute(
        """INSERT INTO tokens (token_hash, user_id) VALUES (?, ?)""", data
    )
    conn.commit()
    conn.close()


def check_has_token(user_id: int):

    conn, cursor = connect_database()

    cursor.execute("""SELECT user_id FROM tokens WHERE user_id = ?""", (user_id,))

    result = cursor.fetchone()

    if result:
        has_token = True
    else:
        has_token = False

    conn.close()

    return has_token

