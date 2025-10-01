import math
from interfaces.figura import Figura

class Pentagono(Figura):
    def __init__(self, lado):
        self.lado = lado
        self.apotema = lado / (2 * math.tan(math.pi / 5))

    def calcular_area(self):
        return (5 * self.lado * self.apotema) / 2

    def calcular_perimetro(self):
        return 5 * self.lado

    def obtener_nombre(self):
        return "Pentágono Regular"
