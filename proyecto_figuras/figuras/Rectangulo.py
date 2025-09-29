class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# Ejemplo
r = Rectangulo(8, 4)
print("Área del rectángulo:", r.area())
print("Perímetro del rectángulo:", r.perimetro())

