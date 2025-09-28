import math
from interfaces.figura import Figura

class Ovalo(Figura):
    def __init__(self, eje_mayor: float, eje_menor: float):
        if min(eje_mayor, eje_menor) <= 0:
            raise ValueError("Los ejes deben ser positivos.")
        self.a = eje_mayor / 2  # Semieje mayor
        self.b = eje_menor / 2  # Semieje menor

    def calcular_perimetro(self) -> float:
        # Aproximación de Ramanujan para el perímetro de una elipse
        h = ((self.a - self.b) ** 2) / ((self.a + self.b) ** 2)
        return math.pi * (self.a + self.b) * (1 + (3*h) / (10 + math.sqrt(4 - 3*h)))

    def calcular_area(self) -> float:
        return math.pi * self.a * self.b

    def obtener_nombre(self) -> str:
        return "Óvalo"
