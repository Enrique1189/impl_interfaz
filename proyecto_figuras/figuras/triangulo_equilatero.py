import math
from interfaces.figura import Figura

class TrianguloEquilatero(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 3 * self.lado

    def calcular_area(self) -> float:
        return (math.sqrt(3) / 4) * (self.lado ** 2)

    def obtener_nombre(self) -> str:
        return "Triángulo Equilátero"
