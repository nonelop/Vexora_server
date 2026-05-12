import sqlite3

def connect_database():
    connection = sqlite3.connect("database/users.db")
    cursor = connection.cursor()

    return connection, cursor


def write_new_user(values: tuple):
    conn, cursor = connect_database()

    cursor.execute("""INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)""", values)
    conn.commit()
    conn.close()


def check_user(username):
    conn, cursor = connect_database()

    cursor.execute("""SELECT username FROM users WHERE username = ?""", (username,))

    result = cursor.fetchone()

    if result:
        is_exist = True
    else:
        is_exist = False

    conn.close()

    return is_exist


def check_password(username, password):
    conn, cursor = connect_database()

    cursor.execute("""SELECT password FROM users WHERE username = ?""", (username,))

    result = cursor.fetchone()

    if result[0] == password:
        is_password_correct = True
    else:
        is_password_correct = False

    conn.close()

    return is_password_correct
