class Octagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def area(self):
        perimetro = 8 * self.lado
        return (perimetro * self.apotema) / 2

    def perimetro(self):
        return 8 * self.lado


# Ejemplo
o = Octagono(4, 5)
print("Área del octágono:", o.area())
print("Perímetro del octágono:", o.perimetro())

