class Item:
    item_type = "Uncategorized"
    __items = []
    
    def __init__(self, title, price):
      self.title = title 
      self.price = price
      Item.__items.append(self)

    def __str__(self):
        return f'Item<{self.item_type}, ({self.title} {self.price}$)>'
    
    def __repr__(self):
        return self.__str__()
    
    @staticmethod
    def show_all_items():
        for item in Item.__items:
            print(f"{item.item_type}: {item.title} ({item.price}$)")
    
    @classmethod
    def change_category(cls, new_category):
        cls.item_type = new_category
        
    
class Book(Item):
    item_type = "Literature"
    
class Smartphone(Item):
    item_type = "Electronics"    


harry_potter = Book("Harry Potter", 25)
python_book = Book("Learning Python 5 Edition", 70)
iphone = Smartphone("Iphone X", 700)
samsung = Smartphone("Galaxy Edge 15+", 1500)

Item.show_all_items()

iphone.change_category("Smartphones")
print("_____________________")

Item.show_all_items()
