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


def check_username(username):
    conn, cursor = connect_database()

    cursor.execute("""SELECT username FROM users WHERE username = ?""", (username,))

    result = cursor.fetchone()

    if result:
        is_exist = True
    else:
        is_exist = False

    conn.close()

    return is_exist