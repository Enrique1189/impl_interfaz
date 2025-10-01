from interfaces.figura import Figura

class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

    def obtener_nombre(self):
        return "Trapecio"
