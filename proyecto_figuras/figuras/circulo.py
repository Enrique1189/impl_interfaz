# figuras/circulo.py
import math
from interfaces.figura import Figura

class Circulo(Figura):
    def __init__(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser un valor positivo.")
        self.radio = radio

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def obtener_nombre(self) -> str:
        return "Círculo"