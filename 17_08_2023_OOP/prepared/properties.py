# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius
#
#     def get_celsius(self):
#         return self._celsius
#
#     def set_celsius(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature cannot be below absolute zero.")
#         self._celsius = value
#
#     def get_fahrenheit(self):
#         return self._celsius * 9/5 + 32
#
#     def set_fahrenheit(self, value):
#         celsius = (value - 32) * 5/9
#         self.set_celsius(celsius)


# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius
#
#     @property
#     def celsius(self):
#         return self._celsius
#
#     @celsius.setter
#     def celsius(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature cannot be below absolute zero.")
#         self._celsius = value
#
#     @property
#     def fahrenheit(self):
#         return self._celsius * 9/5 + 32
#
#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self.celsius = (value - 32) * 5/9


# temp = Temperature(25)
# print(temp.celsius)  # Виводить: 25
# print(temp.fahrenheit)  # Виводить: 77.0
#
# temp.fahrenheit = 100
# print(temp.celsius)  # Виводить: 37.77777777777778
#
# temp.fahrenheit = -1000 # ERROR
# print(temp.celsius)


