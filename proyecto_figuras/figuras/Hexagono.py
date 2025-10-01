import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Hexagono(Figura):
    def _init_(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 6 * self.lado

    def calcular_area(self) -> float:
        apotema = self.lado / (2 * math.tan(math.pi / 6))
        return 6 * self.lado * apotema / 2

    def obtener_nombre(self) -> str:
        return "Hexágono"