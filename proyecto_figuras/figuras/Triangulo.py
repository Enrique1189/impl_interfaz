class Triangulo:
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


# Ejemplo
t = Triangulo(6, 4, 6, 5, 7)
print("Área del triángulo:", t.area())
print("Perímetro del triángulo:", t.perimetro())

