class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Wallet:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def withdraw_to(self, amount, wallet):
        if self.withdraw(amount):
            wallet.deposit(amount)
            return True
        return False

    def balance(self):
        return self.__balance


class VendingMachine:
    def __init__(self, wallet):
        self.__items = []
        self._capacity = 5
        self._wallet = wallet

    def add_item(self, item):
        if len(self.__items) < self._capacity:
            self.__items.append(item)

    def buy_item(self, item_index, wallet):
        if item_index < len(self.__items):
            item = self.__items[item_index]

            if wallet.withdraw_to(item.price, self._wallet):
                self.__items.remove(item)
                return item

    def show_items(self):
        for index, item in enumerate(self.__items):
            print(f'{index}) {item.name}, {item.price}')

class BiggerVendingMachine(VendingMachine):
    def __init__(self, wallet):
        super().__init__(wallet)
        self._capacity = 10


items = [
    Item("Mars", 10),
    Item("Bounty", 12),
    Item("Snickers", 15),
    Item("Milky Way", 20),
    Item("Lion", 32),
    Item("Lion", 32),
    Item("Lion", 32),
    Item("Lion", 32),
    Item("Lion", 32),
    Item("Lion", 32),
    # CTRL + D
]

vending_wallet = Wallet()
vending_machine = VendingMachine(vending_wallet)
for item in items:
    vending_machine.add_item(item)

vending_machine.show_items()

# my_wallet = Wallet()
# my_wallet.deposit(100)

