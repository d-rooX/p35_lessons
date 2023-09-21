# TDD Test Driven Development


class User:
    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    def email(self):
        return f'{self.name.capitalize()}.{self.lastname.capitalize()}@gmail.com'

    def rise_salary(self, percent):
        self.salary = self.salary * (1 + percent)

