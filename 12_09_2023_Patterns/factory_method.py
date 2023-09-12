from abc import ABC, abstractmethod


class Truck:
    def __init__(self, route, cargo) -> None:
        self.route = route
        self.cargo = cargo
    
    def deliver(self):
        print(f"Delivering {self.cargo} to {self.route} using ground roads")


def get_cargos():
    cargos = ['Iron', 'Cooper', 'Food', 'Building Materials', 'Souvenirs']
    routes = ['Kyiv', 'Kharkiv', 'Mykolaiv', 'Lviv', 'Odessa']
    
    for cargo, route in zip(cargos, routes):
        yield cargo, route
    


if __name__ == '__main__':
    trucks = []
    for cargo, route in get_cargos():
        t = Truck(route, cargo)
        trucks.append(t)
    
    for truck in trucks:
        truck.deliver()
        
    

