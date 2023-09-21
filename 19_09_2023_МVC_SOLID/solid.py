# SOLID principles
#
# S - SRP - Single Responsibility Principle
#
# Bad Code
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def save_to_database(self):
#         # saving to database code
#         pass
#
#     def send_email(self, subject, message):
#         # sending email to user....
#         pass


#
#
# Good Code
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#
# class UserRepository:
#     def save_to_database(self, user):
#         ...
#
#     def save_to_file(self, user):
#         ...
#
#     def save_to_memory(self, user):
#         ...
#
#
# class EmailService:
#     def send_email(self, user, subject, message):
#         ...


# GOD - OBJECT

# O - OCP - Open-Closed principle

# Bad code
# class PaymentProcessor:
#     def process_payment(self, payment_details):
#         if payment_details['method'] == 'credit_card':
#             # Обробляємо платіж кредтною картою
#             pass
#         elif payment_details['method'] == 'paypal':
#             # Processing with PayPal
#             pass
#
#
# # Good Code
# class PaymentProcessor:
#     def process_payment(self, payment_details):
#         pass
#
#
# class CreditCardPaymentProcessor(PaymentProcessor):
#     def process_payment(self, payment_details):
#         pass
#
#
# class PayPalPaymentProcessor(PaymentProcessor):
#     def process_payment(self, payment_details):
#         # paypal processing
#         pass


##
# S - SRP - Single Responsibility
# O - OCP - Open-Closed
##########################################
#
# L - LSP - Liskov Substitution Principle
# I - ISP - Interface Segregation Principle
# D - DIP - Dependency Inversion Principle


# Bad code
# class Bird:
#     def fly(self):
#         print('This bird is flying...')
#
#
# class Kiwi(Bird):
#     def fly(self):
#         raise Exception("Kiwi cannot fly")
#
#     def move(self):
#         ...


# Good Code
# class Bird:
#     def move(self):
#         pass


# LSP гарантує що під-класи не порушують контракти базового класу

# class Kiwi(Bird):
#     def move(self):
#         print('Moving by legs')
#
#
# class Duck(Bird):
#     def move(self):
#         print('Swimming in river')
#
#
# class Sparrow(Bird):
#     def move(self):
#         print('Flying among the city')
#
#
# b = Sparrow()
#
#
# def check_bird(b: Bird):
#     b.move()
#
#
# check_bird(b)
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         if value >= 0:
#             self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         if value >= 0:
#             self._height = value
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# # Figure
#
# class Square(Rectangle):
#     def __init__(self, side):
#         self.side = side
#         super().__init__(side, side)
#
#     @property
#     def width(self):
#         return self.side
#
#     @width.setter
#     def width(self, value):
#         self.side = value
#
#     @property
#     def height(self):
#         return self.side
#
#     @height.setter
#     def height(self, value):
#         self.side = value
#
#     @property
#     def area(self):
#         return self.side * self.side
#
#
# def test_calculate_area(rectangle):
#     rectangle.width = 10
#     print("Area with width=10", rectangle.area)
#     rectangle.height = 20
#     print("Area with height=20", rectangle.area)


# a = Rectangle(1, 2)
# print("Rectangle area:", a.area)
# s = Square(10)
# print("Square area:", s.area)
# s.width = 25
# print("Square area:", s.area)
#
# test_calculate_area(a)
# print('.....')
# test_calculate_area(s)


# ISP
# interface segregation principle


# class ImageResizer:
#     def resize(self):
#         ...
#
#
# class ImageRotator:
#     def rotate(self):
#         ...
#
#
# class ImageFilter:
#     def apply_filter(self):
#         ...
#
#
# class ImageProcessor(ImageResizer, ImageRotator, ImageFilter):
#     def process(self):
#         ...
#
#
# class PhotoEditor(ImageProcessor):
#     def edit_photo(self):
#         self.resize()
#         self.rotate()
#         self.apply_filter()
#         print('Photo is edited!')
#
#
# class PhotoUploader(ImageResizer):
#     def upload_photo(self):
#         self.resize()
#         print('Photo uploaded!')
#
#
# p = PhotoEditor()
# p.edit_photo()
#
# pu = PhotoUploader()
# pu.upload_photo()
#
#
#############################
#    Dependency Inversion   #
#############################


# високорівневі модулі не повинні залежати від низькорівневих модулів
# а обидва повинні залежати від абстракій

# абстракції не повинні залежати від деталей.
# деталі повинні залежати від абстракій







