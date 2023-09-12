from abc import ABC, abstractmethod


#### ABSTRACT
class Transport(ABC):
    def __init__(self, route, cargo):
        self.route = route
        self.cargo = cargo

    @abstractmethod
    def deliver(self):
        pass


class TransportCreator(ABC):
    @abstractmethod
    def create_transport(self, route, cargo):
        pass


#### CONCRETE
class Ship(Transport):
    def deliver(self):
        print(f"Delivering {self.cargo} to {self.route} using sea route")


class Truck(Transport):
    def deliver(self):
        print(f"Delivering {self.cargo} to {self.route} using ground roads")


class ShipCreator(TransportCreator):
    def create_transport(self, route, cargo):
        return Ship(route, cargo)


class TruckCreator(TransportCreator):
    def create_transport(self, route, cargo):
        return Truck(route, cargo)


def get_cargos():
    cargos = ['Iron', 'Cooper', 'Food', 'Building Materials', 'Souvenirs']
    routes = ['Kyiv', 'Kharkiv', 'Mykolaiv', 'Lviv', 'Odessa']
    transit_types = ['Ground', 'Ground', 'Sea', 'Ground', 'Sea']

    for cargo, route, transit_type in zip(cargos, routes, transit_types):
        yield cargo, route, transit_type


if __name__ == '__main__':
    transport_creators = {
        'Sea': ShipCreator(),
        'Ground': TruckCreator(),
    }

    transports = []

    for cargo, route, transit_type in get_cargos():
        creator = transport_creators.get(transit_type)
        if creator:
            transport = creator.create_transport(route, cargo)
            transports.append(transport)

    for transport in transports:
        transport.deliver()
