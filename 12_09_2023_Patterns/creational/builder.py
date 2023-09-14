from abc import abstractmethod, ABC


class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None
        self.pool = None
        self.garden = None
        self.greenhouse = None


class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_pool(self):
        pass

    @abstractmethod
    def build_garden(self):
        pass

    @abstractmethod
    def build_greenhouse(self):
        pass

    @abstractmethod
    def get_house(self):
        pass


class ConcreteHouseBuilder(HouseBuilder):
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



house_builder = ConcreteHouseBuilder()
house_builder.build_walls()
house_builder.build_doors()
house_builder.build_windows()


house = house_builder.get_house()





