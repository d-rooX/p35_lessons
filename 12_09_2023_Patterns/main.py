#########################################################
# Твірні       створювати об'єкти
# Структурні   об'єднувати об'єкти та класи
# Поведінкові  доповнити, змінити поведінку об'єкта
##########################################################
#
#
# Creational
# Singleton
# _________________________
# class DBConnection
# DBConnection() --> instance_1
# DBConnection() --> instance_1
# DBConnection() --> instance_1
# DBConnection() --> instance_1
# _________________________
#
# Structural
# Adapter  (adapt interface)
# _______________________
# LegacyLogger.print_message
# LegacyLoggerAdapter ---> log --> print_message
# NewLogger.log
# do_work(logger) ---> logger.log
# _______________________
#
#
# Behavioral
# Decorator
# _______________________
# decorator(func)  --> func*
# _______________________
#




###### Composite
class HierarchyElement:
    def show_price(self):
        pass


class Item(HierarchyElement):
    def __init__(self, price):
        self.price = price

    def show_price(self):
        return self.price


class Box(HierarchyElement):
    def __init__(self, children=None):
        if children is None:
            children = []

        self.children: list[HierarchyElement] = children

    def add_child(self, item):
        self.children.append(item)

    def show_price(self):
        total_price = 0
        for item in self.children:
            total_price += item.show_price()
        return total_price


box = Box()
box.add_child(Item(100))
box.add_child(Box([Item(5), Box([Item(10), Item(15)])]))
box.add_child(Item(500))

price = box.show_price()
print(price)
