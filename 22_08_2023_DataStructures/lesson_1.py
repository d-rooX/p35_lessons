# успадкування
#   множинне успадкування
#   міксіни
#   mro


# методи та керовані атрибути
#   статичні
#   методи класу
#   property
#    - getter
#    - setter


# class Number:
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self, other):
#         return Number(self.number + other.number)
#
#     def __str__(self):
#         return str(self.number)
#
#
# a = Number(10)
# b = Number(25)
#
# c = a + b
#
# print(c)
# print(type(c))
#
#
# print([1, 2, 3].__len__())
#
#
# class Vehicle:
#     def __init__(self, engine_power, door_count):
#         self.engine_power = engine_power
#         self.door_count = door_count
#
#     def drive(self):
#         print(f'Машина їде! Невідомо з якою швидкістю, але під капотом {self.engine_power} коней!')
#
#
# class Tracktor(Vehicle):
#     def __init__(self):
#         super().__init__(engine_power=10, door_count=2)
#
# t = Tracktor()
# t.drive()

# class WalkerMixin:
#     def walk(self):
#         print('Im walking')
#
#
# class FlyerMixin:
#     def fly(self):
#         print('Im flying')
#
#
# class BirdMixin(WalkerMixin, FlyerMixin):
#     def make_eggs(self):
#         print('10 eggs made!')
#
#
# class Animal:
#     def __init__(self, age):
#         self.age = age
#
#     def eat(self):
#         print('im eating food')
# #
# #
# # class Mammal(Animal, WalkerMixin):
# #     pass
# #
# #
# class Bird(Animal, BirdMixin):
#     def __init__(self, age, fly_height):
#         super().__init__(age)
#         self.fly_height = fly_height
#
#
# # mammal = Mammal(10)
# # mammal.eat()
# # mammal.walk()
#
# duck = Bird(5, 200)
#
# duck.fly()
# duck.eat()
#
# print(Bird.mro())

class Item:
    category = "Uncategorized"
    __items = []

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Item.__items.append(self)

    def foo(self):
        pass

    @classmethod
    def single_category_item(cls, title, price, category):
        # cls - Item
        # Item()

        item = cls(title, price)
        item.category = category
        return item

    @classmethod  # decorator
    def show_all_items(cls):
        for item in cls.__items:
            print(f'{item.category}: {item.title} ({item.price}$)')

    @classmethod
    def change_category(cls, new_category):
        cls.category = new_category
#
#     # @classmethod
#
#
# class Book(Item):
#     category = "Literature"
#
# class Smartphone(Item):
#     category = "Electronics"
#
#
# item = Item("plant seeds", 2.5)
# harry_potter0 = Book("Harry Potter", 15)
# harry_potter1 = Book("Harry Potter 2", 20)
# harry_potter2 = Book("Harry Potter 3", 25)
# iphone0 = Smartphone("Iphone 17+ pro", 200000)
# iphone1 = Smartphone("Iphone 18+ pro", 2000000)
# iphone2 = Smartphone("Iphone 19+ pro", 20000000)
# iphone3 = Smartphone("Iphone 27+ pro", 200000000)
#
# iphone3.change_category("Devices")
# Smartphone.change_category("Electronic Devices")

# Smartphone(title, price)


# items = [item, harry_potter0, harry_potter1, harry_potter2, iphone0, iphone1, iphone2, iphone3]
# Smartphone.category = "Smartphones"
# for i in items:
#     print(i.category)

# unique_item = Item.single_category_item("Apple", 2.5, "Fruit")
# print(unique_item)

# item_test = Item("test", 0.01)
# print(item_test.__dict__)
# print(item_test.category)
# print(item_test.__class__.__dict__)

# Item.show_all_items()

# class AreaUtils:
#     @staticmethod
#     def circle_area(radius):
#         return 3.14 * (radius ** 2)
#
#     @staticmethod
#     def rectangle_area(width, length):
#         return width * length


# print(AreaUtils.circle_area(10))
# print(AreaUtils.rectangle_area(15, 20))



#################################
# @property


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property  # getter   GET
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9


t = Temperature(10)
print(t.celsius)

t.celsius = -200

print(t.celsius)
print(t.fahrenheit)

t.fahrenheit = 100

print(t.celsius)
print(t.fahrenheit)

# GITHUB COPILOT


# створює кілька елементів класу Node і вертає список

