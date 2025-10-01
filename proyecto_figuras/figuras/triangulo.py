import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Triangulo(Figura):
    def _init_(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser valores positivos.")
        self.base = base
        self.altura = altura

    def calcular_perimetro(self) -> float:
        return 3 * self.base 

    def calcular_area(self) -> float:
        return 0.5 * self.base * self.altura

    def obtener_nombre(self) -> str:
        return "Triángulo"