import math
from interfaces.figura import Figura

class Octogono(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 8 * self.lado

    def calcular_area(self) -> float:
        perimetro = self.calcular_perimetro()
        apotema = self.lado / (2 * math.tan(math.pi / 8))
        return (perimetro * apotema) / 2

    def obtener_nombre(self) -> str:
        return "Octógono"
