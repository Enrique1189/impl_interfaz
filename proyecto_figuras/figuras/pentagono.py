# figuras/pentagono.py
import math
from interfaces.figura import Figura

class Pentagono(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 5 * self.lado

    def calcular_area(self) -> float:
        apotema = self.lado / (2 * math.tan(math.pi / 5))  # Apotema calculado con la fórmula del pentágono regular
        return (5 * self.lado * apotema) / 2  # Fórmula del área de un polígono regular

    def obtener_nombre(self) -> str:
        return "Pentágono"