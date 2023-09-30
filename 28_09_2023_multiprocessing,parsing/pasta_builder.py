

class Pasta:
    def __init__(self):
        self.souce = None
        self.a = None
        self.b = None
        self.c = None
        self.c1 = None
        self.c12 = None
        self.c133 = None
        self.c144 = None
        self.c155 = None
        self.c166 = None

class PastaBuilder:
    ...


class CarbonaraPastaBuilder(PastaBuilder):
    def __init__(self):
        self.pasta = Pasta()

    def add_souce(self):
        self.pasta.souce = 'Carbonara souce'

    def add_a(self, a):
        self.pasta.a = a

    def get_pasta(self):
        return self.pasta
    


# Pasta(..., ..., ...)
# .add...()
# .add...()
# .add...()




