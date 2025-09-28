import math
from interfaces.figura import Figura

class Triangulo(Figura):
    def __init__(self, lado1: float, lado2: float, lado3: float):
        if min(lado1, lado2, lado3) <= 0:
            raise ValueError("Los lados deben ser positivos.")
        if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
            raise ValueError("Los lados no forman un triángulo válido.")
        self.l1, self.l2, self.l3 = lado1, lado2, lado3

    def calcular_perimetro(self) -> float:
        return self.l1 + self.l2 + self.l3

    def calcular_area(self) -> float:
        s = self.calcular_perimetro() / 2
        return math.sqrt(s * (s - self.l1) * (s - self.l2) * (s - self.l3))  # Fórmula de Herón

    def obtener_nombre(self) -> str:
        return "Triángulo"
