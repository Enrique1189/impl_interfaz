from interfaces.figura import Figura

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

    def obtener_nombre(self):
        return "Cuadrado"
