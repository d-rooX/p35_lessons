# class Student:
#     def __init__(self, student_name):
#         self.name = student_name
#
#     def show_scores(self):
#         return [5, 5, 5, 4]
#
#     def say_hello(self):
#         print(f'Hello, my name is {self.name}')
#
#
# student1 = Student("Daniel")
# student2 = Student("Steve")
# print(student1.name)
# print(student2.name)
#
# student1.say_hello()
# student2.say_hello()





# circle_radius = 5
# circle_area = 3.14 * (circle_radius ** 2)
# circle_circumference = 2 * 3.14 * circle_radius
# circle_x = 0
# circle_y = 0
#
#
# rectangle_width = 10
# rectangle_height = 8
# rectangle_area = rectangle_width * rectangle_height
# rectangle_perimeter = 2 * (rectangle_width + rectangle_height)
# rectangle_x = 0
# rectangle_y = 0
#
#
# rectangle1_width = 10
# rectangle1_height = 8
# rectangle1_area = rectangle_width * rectangle_height
# rectangle1_perimeter = 2 * (rectangle_width + rectangle_height)
# rectangle1_x = 0
# rectangle1_y = 0


# class Circle:
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * (self.radius ** 2)
#
#     def circumference(self):
#         return 2 * 3.14 * self.radius
#
# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# circle00 = Circle(0, 0, 10)
# circle10 = Circle(0, 5, 15)
# circle11 = Circle(0, 0, 13)
# circle12 = Circle(7, 3, 12)
# circle13 = Circle(4, 8, 11)
# rectangle00 = Rectangle(0, 0, 100, 200)
#
#
# print(f'Rectangle perimeter: {rectangle00.perimeter()}')
#
#
# print(circle00.radius)
# print(circle00.circumference())


#### інкапсуляція, успадкування, поліморфізм


################ INCAPSULATION

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
#
#     def _deduct_fees(self, amount):
#         fee = amount * 0.05
#         return amount - fee
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             amount = self._deduct_fees(amount)
#             self.__balance -= amount
#
#     def show_balance(self):
#         print(self.__balance)
#
# bank_account = BankAccount()
# bank_account.deposit(100)
# bank_account._deduct_fees()
#
# bank_account.__balance = 1000
# bank_account.show_balance()
# print(bank_account.__balance)
#
#
# print(bank_account.__dict__)
# print(bank_account._BankAccount__balance)
# bank_account._BankAccount__balance += 100
# print(bank_account._BankAccount__balance)

# def foo():
#     foo.counter += 1
#     print('Hello')
#
# foo.counter = 0
#
# foo()
# foo()
# foo()
# foo()
#
# print(foo.counter)

# bank_account
# print(bank_account.balance)
# bank_account.withdraw(50)
# print(bank_account.balance)
# bank_account.balance -= 100
# bank_account.withdraw(10000)
# print(bank_account.balance)


# bank_account._balance += 100
# print(bank_account._balance)

########### INHERITANCE

class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return None


class Circle(Figure):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius

class Rectangle(Figure):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
#
def move_figure(figure, dx, dy):
    figure.x += dx
    figure.y += dy
    print(f"Figure with area {figure.area()} moved on {dx = }, {dy = }")
    # f-strings

#
# figures = [
#     Circle(10, 10, 50),
#     Circle(10, 0, 100),
#     Circle(10, 15, 60),
#     Circle(20, 10, 55),
#     Rectangle(10, 2, 200, 450),
#     Rectangle(10, 2, 200, 450),
#     Rectangle(10, 2, 200, 450),
#     Rectangle(10, 2, 200, 450),
# ]
#
# for figure in figures:
#     move_figure(figure, 10, 50)

####### POLIMORPHISM

# numbers = [1, 2, 3, 4, 5]
# text = "one two three"
# dic = {'a': 1}
# x = 10
#
#
# print(len(numbers))
# print(len(text))
# print(len(dic))
# print(len(x))

# class Cat:
#     def speak(self):
#         return "Meow!"
#
#
# class Dog:
#     def speak(self):
#         return "Woof!"
#
#
# class Cow:
#     def speak(self):
#         return "Moo!"
#
#
# animals = [Cat(), Dog(), Cow()]
# for animal in animals:
#     print(animal.speak())

# print(5 + 3)
# print("Hello " + "world")

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Vector<{self.x}, {self.y}>'
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             new_x = self.x + other.x
#             new_y = self.y + other.y
#             return Vector(new_x, new_y)
#         raise Exception(f"Impossible to add Vector with {type(other)} ")
#
#     def __iadd__(self, other):
#         self.x += other.x
#         self.y += other.y
#         return self
#
#     def __len__(self):
#         return int((self.x ** 2 + self.y ** 2) ** 0.5)
#
#     # equals
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v4 = Vector(10, 2)
# print(len(v4))
#
# print(v1)
# v1 += v2
# print(v1)

# v3 = v1 + v2 + v4
#
# print(v3.x, v3.y)
# print(v1 == v4)

# class StudentsList:
#     def __init__(self):
#         self.students = []
#
#     def __len__(self):
#         return len(self.students)
#
#
# students_list = StudentsList()
# print(len(students_list))

# class Multiplier:
#     def __init__(self, factor):
#         self.factor = factor
#
#     def __call__(self, x):
#         return x * self.factor
#
# double = Multiplier(3)
# print(double(10))




