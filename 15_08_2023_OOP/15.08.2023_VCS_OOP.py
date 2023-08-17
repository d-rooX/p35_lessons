items = {
    'computer': 100,
    'book': 15,
    'apple': 5,
    'banana': 6,
    'watermelon': 7,
    'pineapple': 8,
}

def calculate_price(items, cart):
    price = 0
    for item in cart:
        price += items[item]
    return price

# cart = []
# cart.append('computer')
# cart.append('book')


# print(calculate_price(items, ['computter', 'book', 'asd']))


####    Animal  -- body_temp
##  Human   Bird


# static, duck

# інкапсуляція, успадкування, поліморфізм

class Person:
    def __init__(self, name, age, country, job='unemployed', discount = 0):     # magic
        self.name = name
        self.age = age
        self.job = job
        self.country = country
        self.discount = discount

    def change_country(self, country):
        print(f"Person {self.name} is moving to country {country} ")
        self.job = 'unemployed'
        self.country = country

    def say_hello(self):
        print(f'Hello, my name is {self.name}, my age is {self.age} and i am {self.job}')

    def say_hello_to(self, person):
        print(f"Hello, {person.name}, my name is {self.name}")


#       Car
#  drive -> speed += 100
# car1   car2   car3

# print(Person.age)

person1 = Person("Peter", 25, job="Python Programmer")
person2 = Person("Steven", 30)

person3 = Person("Peter", 25, job="Python Programmer")

# person1.say_hello()
# person2.say_hello()

person2.say_hello_to(person1)


def add(a, b):
    return a + b

#     +
# int,  str
# print(add("Hello ", "world"))


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f'Item {self.name} costs {self.price}$')


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_price(self):
        price = 0
        for item in self.items:
            print(f"You added to cart: {item.name} ({item.price}$)")
            price += item.price
        return price


my_cart = Cart()
book = Item("Book", 15)
computer = Item("Computer", 100)
tv = Item("TV", 150)

my_cart.add_item(book)
my_cart.add_item(computer)
my_cart.add_item(tv)

print(my_cart.calculate_price())

country = input()
person3.change_country(country)

person3.country = 'Ukraine'

book.show_info()

