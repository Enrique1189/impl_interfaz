import math
from interfaces.figura import Figura

class Elipse(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular_area(self):
        return math.pi * self.a * self.b

    def calcular_perimetro(self):
        # Fórmula aproximada de Ramanujan
        return math.pi * (3*(self.a + self.b) - math.sqrt((3*self.a + self.b)*(self.a + 3*self.b)))

    def obtener_nombre(self):
        return "Elipse"
