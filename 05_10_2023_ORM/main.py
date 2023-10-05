from models import User, Cart, Order, Product
from pony.orm import *
from strings import AppStrings

current_user_id = None


@db_session
def add_products():
    Product(title='Tv PRO +++', price=1500)
    Product(title='Iphone 15+', price=56700)
    Product(title='Samsung Galaxy Ultra', price=4222)
    Product(title='Microwave Titan 100', price=12333)
    Product(title='Gigachad Vacuum Cleaner', price=14567)
    commit()


@db_session
def register_user():
    global current_user_id

    while True:
        username = input('Write your username: ')
        got_user = User.get(username=username)
        if got_user is None:
            break
        print('Username is already taken, please choose another.')

    while True:
        try:
            age = int(input('Write your age: '))
            break
        except ValueError:
            print('Please write age in digits')

    user = User(username=username, age=age)
    cart = Cart(user=user)
    user.cart = cart
    commit()

    current_user_id = user.id


@db_session
def login_user():
    global current_user_id

    while True:
        username = input("Write your username: ")
        got_user = User.get(username=username)
        if got_user:
            break
        print('User is not found, please retry')

    current_user_id = got_user.id


@db_session
def get_products():
    return Product.select()


@db_session
def add_product_to_cart(product):
    user = User.get(id=current_user_id)
    user.cart.products.add(product)
    commit()


@db_session
def process_product(product_id):
    chosen_product = Product.get(id=product_id)
    if chosen_product:
        text = AppStrings.sure_want_to_buy.format(
            title=chosen_product.title,
            price=chosen_product.price
        )
        if input(text).lower() == 'y':
            add_product_to_cart(chosen_product)


@db_session
def get_user_cart():
    user = User.get(id=current_user_id)
    if user.cart.products:
        print(f'You have {len(user.cart.products)} products in your cart:')
    else:
        return

    for product in user.cart.products:
        print("  - ", product.title)

    print(f'Your cart total price: {sum([product.price for product in user.cart.products])}')


@db_session
def main():
    match input('Login or register? [l/r]: ').lower():
        case 'l':
            login_user()
        case 'r':
            register_user()
        case _:
            exit()

    products = get_products()
    while True:
        for product in products:
            print(f'[{product.id}] {product.title}: {product.price}')

        print('_______________________')

        match input('Choose a product to buy by its id or [q]uit catalog: ').lower():
            case 'q':
                break
            case 'c':
                get_user_cart()
                print('_________________________')
            case product_id:
                process_product(product_id)


main()
