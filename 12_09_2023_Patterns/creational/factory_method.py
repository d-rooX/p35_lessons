from abc import abstractmethod, ABC


############## ABSTRACT
class Transport(ABC):
    def __init__(self, cargo, route):
        self.cargo = cargo
        self.route = route

    @abstractmethod
    def deliver(self):
        pass


class TransportCreator(ABC):
    @abstractmethod
    def create_transport(self, route, cargo) -> Transport:
        pass


############### CONCRETE
class Ship(Transport):
    def deliver(self):
        print(f"Delivering {self.cargo} to {self.route} using sea routes")


class Truck(Transport):
    def deliver(self):
        print(f"Delivering {self.cargo} to {self.route} using ground roads")


class ShipCreator(TransportCreator):
    def create_transport(self, route, cargo) -> Transport:
        return Ship(cargo, route)


class TruckCreator(TransportCreator):
    def create_transport(self, route, cargo) -> Transport:
        return Truck(cargo, route)

################################


def get_cargos():
    cargos = ['Iron', 'Cooper', 'Food', 'Building Material', 'Souvenirs']
    routes = ['Kyiv', 'Kharkiv', 'Mykolaiv', 'Lviv', 'Odessa']
    transit_types = ['Ground', 'Ground', 'Sea', 'Ground', 'Sea']

    for cargo, route, transit_type in zip(cargos, routes, transit_types):
        yield cargo, route, transit_type


##################################
######### FACTORY METHOD #########
##################################

if __name__ == '__main__':
    creators = {
        'Ground': TruckCreator(),
        'Sea': ShipCreator(),
    }

    transport = []
    for cargo, route, transit_type in get_cargos():
        if transit_type in creators:
            creator = creators[transit_type]
            t = creator.create_transport(route, cargo)
        else:
            raise ValueError("No such transit type")

        transport.append(t)

    for truck in transport:
        truck.deliver()
