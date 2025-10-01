import math
from interfaces.figura import Figura

class Elipse(Figura):
    def __init__(self, eje_mayor: float, eje_menor: float):
        if min(eje_mayor, eje_menor) <= 0:
            raise ValueError("Ambos ejes deben ser positivos.")
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def calcular_perimetro(self) -> float:
        # Aproximación de Ramanujan
        a = self.eje_mayor / 2
        b = self.eje_menor / 2
        h = ((a - b)**2) / ((a + b)**2)
        return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def calcular_area(self) -> float:
        return math.pi * (self.eje_mayor / 2) * (self.eje_menor / 2)

    def obtener_nombre(self) -> str:
        return "Elipse"
