# Класс Дома, который мы хотим построить
class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None
        self.pool = None  # Необязательный параметр
        self.garden = None  # Необязательный параметр
        self.greenhouse = None  # Необязательный параметр

# Абстрактный класс Строителя
class HouseBuilder:
    def build_walls(self):
        pass

    def build_doors(self):
        pass

    def build_windows(self):
        pass

    def build_roof(self):
        pass

    def build_pool(self):
        pass

    def build_garden(self):
        pass

    def build_greenhouse(self):
        pass

    def get_house(self):
        pass

# Конкретный Строитель для создания домов
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "Brick walls"

    def build_doors(self):
        self.house.doors = "Wooden doors"

    def build_windows(self):
        self.house.windows = "Glass windows"

    def build_roof(self):
        self.house.roof = "Tiled roof"

    def build_pool(self):
        self.house.pool = "Swimming pool"

    def build_garden(self):
        self.house.garden = "Beautiful garden"

    def build_greenhouse(self):
        self.house.greenhouse = "Glass greenhouse"

    def get_house(self):
        return self.house

# Директор, который управляет процессом построения дома
class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()
        # Строитель не обязательно вызывает все методы
        # Можно выбирать, какие параметры добавить

# Использование паттерна Строитель
if __name__ == "__main__":
    builder = ConcreteHouseBuilder()  # Создаем конкретного строителя
    director = HouseDirector(builder)  # Создаем директора

    director.construct()  # Строим дом
    house = builder.get_house()  # Получаем готовый дом

    print(f"Walls: {house.walls}")
    print(f"Doors: {house.doors}")
    print(f"Windows: {house.windows}")
    print(f"Roof: {house.roof}")
    print(f"Pool: {house.pool}")
    print(f"Garden: {house.garden}")
    print(f"Greenhouse: {house.greenhouse}")
