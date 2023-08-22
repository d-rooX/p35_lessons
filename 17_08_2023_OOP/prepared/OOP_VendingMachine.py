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
    
    def get_balance(self):
        return self.__balance


class VendingMachine:
    def __init__(self, wallet):
        self._capacity = 5
        self.__items = []
        self.__wallet = wallet
    
    def get_wallet_balance(self):
        return self.__wallet.get_balance()
    
    def show_items(self):
        for index, item in enumerate(self.__items):
            print(f'{index}) {item.name} ({item.price}$)')
    
    def add_item(self, item):
        if len(self.__items) < self._capacity:
            self.__items.append(item)
            
    def add_items(self, *items):
        for item in items:
            self.add_item(item)
    
    def buy_item(self, item_index, wallet):
        if item_index < len(self.__items):
            item = self.__items[item_index]
        
            if wallet.withdraw_to(item.price, self.__wallet):
                self.__items.remove(item)
                return item
        
        return None 

class BiggerVendingMachine(VendingMachine):
    def __init__(self, wallet):
        super().__init__(wallet)
        self._capacity = 10

    def add_item(self, item):
        if isinstance(item, Item):
            super().add_item(item)
        else:
            raise Exception("Given item is not an Item object")
            

mars = Item("Mars", 10)
milky_way = Item("Milky Way", 15)
kitkat = Item("Kitkat", 16)
snickers = Item("Snickers", 20)
bounty = Item("Bounty", 25)
lion = Item("Lion", 30)

vending_wallet = Wallet()
vending_machine = VendingMachine(vending_wallet)
vending_machine.add_items(mars, milky_way, kitkat, snickers, bounty, lion)

vending_machine.__wallet.__balance = 0
