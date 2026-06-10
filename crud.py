import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (name TEXT, price INTEGER, quantity INTEGER)")

conn.commit()

def create(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()

def getAll():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def get(name):
    cursor.execute(
        "SELECT * FROM products WHERE name = ?",
        (name,)
    )
    return cursor.fetchall()

def update(name, price, quantity):
    cursor.execute(
        "UPDATE products SET price = ?, quantity = ? WHERE name = ?",
        (price, quantity, name)
    )
    conn.commit()

def delete(name):
    cursor.execute(
        "DELETE FROM products WHERE name = ?",
        (name,)
    )
    conn.commit()