class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2
