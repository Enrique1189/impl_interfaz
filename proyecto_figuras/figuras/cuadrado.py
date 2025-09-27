# figuras/cuadrado.py
from interfaces.figura import Figura

class Cuadrado(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def obtener_nombre(self) -> str:
        return "Cuadrado"
