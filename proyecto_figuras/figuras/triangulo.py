import math
from interfaces.figura import Figura

class Triangulo(Figura):
    def __init__(self, lado1: float, lado2: float, lado3: float):
        if not self._es_triangulo_valido(lado1, lado2, lado3):
             raise ValueError("Los lados no forman un triángulo válido.")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def calcular_perimetro(self) -> float:
        return self.lado1 + self.lado2 + self.lado3

    def calcular_area(self) -> float:
        s = self.calcular_perimetro() / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def obtener_nombre(self) -> str:
        return "Triángulo"
