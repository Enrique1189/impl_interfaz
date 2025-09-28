import math
from interfaces.figura import Figura

class Hexagono(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 6 * self.lado

    def calcular_area(self) -> float:
        apotema = self.lado * math.sqrt(3) / 2
        return (self.calcular_perimetro() * apotema) / 2

    def obtener_nombre(self) -> str:
        return "Hexágono"
