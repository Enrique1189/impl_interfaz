# figuras/octagono.py
import math
from interfaces.figura import Figura

class Octagono(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 8 * self.lado

    def calcular_area(self) -> float:
        return 2 * (1 + math.sqrt(2)) * self.lado ** 2

    def obtener_nombre(self) -> str:
        return "Octágono"

