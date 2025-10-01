import math
from interfaces.figura import Figura

class TrianguloRectangulo(Figura):
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2
        self.hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

    def calcular_area(self):
        return (self.cateto1 * self.cateto2) / 2

    def calcular_perimetro(self):
        return self.cateto1 + self.cateto2 + self.hipotenusa

    def obtener_nombre(self):
        return "Triángulo Rectángulo"
