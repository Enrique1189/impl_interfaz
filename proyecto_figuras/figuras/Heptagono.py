class Heptagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def area(self):
        perimetro = 7 * self.lado
        return (perimetro * self.apotema) / 2

    def perimetro(self):
        return 7 * self.lado



h = Heptagono(6, 8)
print("Área del heptágono:", h.area())
print("Perímetro del heptágono:", h.perimetro())