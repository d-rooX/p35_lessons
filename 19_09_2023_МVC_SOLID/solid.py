
# SOLID principles


# S - SRP - Single Responsibility Principle

# Bad Code
#
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


# Good Code
#
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

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

# Good Code
# class PaymentProcessor:
#     def process_payment(self, payment_details):
#         pass
#
# class CreditCardPaymentProcessor(PaymentProcessor):
#     def process_payment(self, payment_details):
#         pass
#
# class PayPalPaymentProcessor(PaymentProcessor):
#     def process_payment(self, payment_details):
#         # paypal processing
#         pass


###
# S - SRP
# O - OCP

###########################################
# L - LSP - Liskov Substitution Principle
# I - ISP - Interface Segregation Principle
# D - DIP - Dependency Inversion Principle


