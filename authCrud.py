import sqlite3

conn = sqlite3.connect("main.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, email TEXT UNIQUE, password TEXT, role INTEGER)")
conn.commit()

def create_user(username, email, password, role=0):
    cursor.execute(
        "INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)",
        (username, email, password, role)
    )
    conn.commit()

def get_all_users():
    cursor.execute("SELECT id, username, email, role FROM users")
    return cursor.fetchall()

def get_user(user_id):
    cursor.execute(
        "SELECT id, username, email, role FROM users WHERE id = ?",
        (user_id,)
    )
    return cursor.fetchall()

def update_user(user_id, username, email, password, role):
    cursor.execute(
        "UPDATE users SET username = ?, email = ?, password = ?, role = ? WHERE id = ?",
        (username, email, password, role, user_id)
    )
    conn.commit()

def delete_user(user_id):
    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )
    conn.commit()

def login_user(username, password):
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    return cursor.fetchone()