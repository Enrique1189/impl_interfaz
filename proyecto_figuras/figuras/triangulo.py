import math
from interfaces.figura import Figura

class Triangulo(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return (math.sqrt(3) / 4) * self.lado ** 2

    def calcular_perimetro(self):
        return 3 * self.lado

    def obtener_nombre(self):
        return "Triángulo Equilátero"
