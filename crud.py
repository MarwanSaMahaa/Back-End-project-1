import sqlite3

conn = sqlite3.connect("products.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (name TEXT, price INTEGER, quantity INTEGER)")

conn.commit()

def create(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()

def get_all():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def get(name):
    cursor.execute(
        "SELECT * FROM products WHERE name = ?",
        (name,)
    )
    return cursor.fetchall()

def update(old_name, new_name, price, quantity):
    cursor.execute(
        "UPDATE products SET name = ?, price = ?, quantity = ? WHERE name = ?",
        (new_name, price, quantity, old_name)
    )
    conn.commit()

def delete(name):
    cursor.execute(
        "DELETE FROM products WHERE name = ?",
        (name,)
    )
    conn.commit()