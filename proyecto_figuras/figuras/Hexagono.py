class Hexagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def area(self):
        perimetro = 6 * self.lado
        return (perimetro * self.apotema) / 2

    def perimetro(self):
        return 6 * self.lado


# Ejemplo
hx = Hexagono(5, 4)
print("Área del hexágono:", hx.area())
print("Perímetro del hexágono:", hx.perimetro())

