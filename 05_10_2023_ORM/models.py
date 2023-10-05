from datetime import datetime

from pony.orm import *

db = Database()


class User(db.Entity):
    username = Required(str, unique=True)
    age = Required(int)
    address = Optional(str)
    cart = Optional('Cart')


# One-to-one

class Cart(db.Entity):
    user = Required(User)
    products = Set('Product')


# many-to-many

class Product(db.Entity):
    title = Required(str)
    price = Required(float)

    carts = Set(Cart)
    orders = Set('Order')

# many-to-many

class Order(db.Entity):
    address = Required(str)
    products = Set(Product)
    date = Required(datetime)


db.bind(provider='sqlite', filename='database.db', create_db=True)
db.generate_mapping(create_tables=True)
