class Octagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def area(self):
        return (8 * self.lado * self.apotema) / 2

    def perimetro(self):
        return 8 * self.lado
