# figuras/triangulorec.py
from interfaces.figura import Figura
import math

class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser valores positivos.")
        self.base = base
        self.altura = altura

    def calcular_perimetro(self) -> float:
        hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)
        return self.base + self.altura + hipotenusa

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def obtener_nombre(self) -> str:
        return "Triángulo Rectángulo"
