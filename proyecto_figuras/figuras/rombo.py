class Rombo:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def area(self):
        return (self.d1 * self.d2) / 2

    def perimetro(self):
        # Aproximamos lado como d1/2 (puedes cambiarlo si tienes el lado real)
        lado = self.d1 / 2
        return 4 * lado