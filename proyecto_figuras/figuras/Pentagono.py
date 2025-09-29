class Pentagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def area(self):
        perimetro = 5 * self.lado
        return (perimetro * self.apotema) / 2

    def perimetro(self):
        return 5 * self.lado


# Ejemplo
p = Pentagono(6, 4)
print("Área del pentágono:", p.area())
print("Perímetro del pentágono:", p.perimetro())

