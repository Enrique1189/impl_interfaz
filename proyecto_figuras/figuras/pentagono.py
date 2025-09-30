class Pentagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def area(self):
        return (5 * self.lado * self.apotema) / 2

    def perimetro(self):
        return 5 * self.lado