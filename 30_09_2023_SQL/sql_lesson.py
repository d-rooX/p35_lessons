#   Relative
#      Table (schema)
#      Relations
#
#
#
#
#
import random
# Users
#       ID,     NAME,       LASTNAME,       BIRTHDATE,
#       1       John        Doe             1995
#


# Orders
#       ID      PRODUCT_NAME        PRODUCT_PRICE       DATE    USER_ID
#
#
#
#
#
# STRUCTURED QUERY LANGUAGE
# SQL
# Sqlite СУБД
#

import sqlite3

# TABLE
#   ID : INT
#   NAME : TEXT
#   IS_ADMIN : BOOL


# integers
#   bigint | від -9 223 372 036 854 775 808      | 8 bytes
#          |  до 9 223 372 036 854 775 807       |
#
#   int    | від -2 147 483 648 до 2 147 483 647 | 4 bytes
#
#   smallint |   від -32 768 до 32 767           |  2 bytes
#
#   tiny     | 0 - 255    | 1 bytes
#
#       char        - fixed, without unicode
#       varchar     - var
#       nchar
#       nvarchar
#
#        float, real
#
#
#
#   datetime, datetime2


###########
###########
###########
###########
###########


# Sq(lite)
# NULL
# INTEGER
# REAL
# TEXT
# BLOB
#
#   SELECT LastName
#   FROM Students
#   WHERE MONTH(BirthDate) = 11;
#
#
#
#   SELECT name, lastname
#   FROM tableName;
#
#   WHERE firstname = 'John' OR firstname = 'David' AND
#   ORDER BY columnName1 ASC DESC, ...;
#
#
#
#
#   INSERT INTO Users(Firstname, Lastname, Age)
#   VALUES ('John', 'Doe', 25)
#
#
#   UPDATE Users
#   SET firstname = 'John'
#   WHERE lastname = 'Doe'
#
#
#
#
#
#
#
# Transaction
#               ACID
#   Atomicity (атомарність)
#   Consistency (узгодженість)
#   Isolation
#   Durability
#
#
##
#  BEGIN TRAN
## COMMIT TRAN
## ROLLBACK TRAN
#
#
#
# ALTER TABLE Users
#


import sqlite3

conn: sqlite3.Connection | None = None
cursor: sqlite3.Cursor | None = None


def init_db():
    global cursor, conn
    conn = sqlite3.connect('database.db')
    conn.execute("PRAGMA foreign_keys = ON")
    conn.commit()
    cursor = conn.cursor()


def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    ''')
    # one to one relationship
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL
        )
    ''')

    # many to many relationship
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS product_cart (
                product_id INTEGER,
                cart_id INTEGER,
                FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
                FOREIGN KEY (cart_id) REFERENCES carts(id) ON DELETE CASCADE,
                PRIMARY KEY (product_id, cart_id)
            )
        ''')

    # one to many
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product TEXT,
            price REAL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
        )
    ''')
    conn.commit()


def add_user(user):
    cursor.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)
    ''', (user['name'], user['age']))

    user_id = cursor.lastrowid
    if user_id:
        cursor.execute('''
            INSERT INTO carts (user_id) VALUES (?)
        ''', (user_id,))

    conn.commit()


def add_order(user_id, product, price):
    cursor.execute(f'''
        INSERT INTO orders (user_id, product, price) VALUES (?, ?, ?);
    ''', (user_id, product, price))
    conn.commit()


def add_products():
    for product_name in ['Tv', 'Iphone', 'Google pixel', 'Smart Watch', 'Laptop', 'MacBook']:
        cursor.execute('''
            INSERT INTO products(name, price) VALUES (?, ?)       
        ''', (product_name, random.randint(1000, 10000)))
    conn.commit()


def get_all_users():
    cursor.execute('SELECT age, id, name FROM users')
    rows = cursor.fetchall()
    return rows


def select_user_orders(user_id):
    cursor.execute('''
        SELECT orders.id, orders.product, orders.price, users.name, users.age FROM orders
        JOIN users ON orders.user_id = users.id WHERE users.id = ?
        ''', (user_id,))
    orders = cursor.fetchall()
    return orders


def add_to_cart(user_id, product_ids: list[int]):
    cursor.execute('''
        SELECT carts.id FROM carts WHERE carts.user_id = ?
    ''', (user_id,))
    cart_id = cursor.fetchone()[0]

    for product_id in product_ids:
        cursor.execute('''
            INSERT INTO product_cart (product_id, cart_id) VALUES (?, ?)
        ''', (product_id, cart_id))
    conn.commit()


def delete_users_by_name(name):
    cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    conn.commit()


if __name__ == '__main__':
    init_db()
    create_tables()
    add_products()

    add_user({'name': "Check User", 'age': 22})
    add_user({'name': "Check User 1", 'age': 23})
    add_user({'name': "Check User 2", 'age': 24})
    add_user({'name': "Check User 3", 'age': 25})

    add_to_cart(4, [6, 5])


    # OOP <--> SQL  ------>>  ORM  Object Relation Mapping
    # user_cart = Cart() ----> carts

