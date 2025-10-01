import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Paralelogramo(Figura):
    def _init_(self, base: float, altura: float, lado: float):
        if base <= 0 or altura <= 0 or lado <= 0:
            raise ValueError("La base, altura y el lado deben ser valores positivos.")
        self.base = base
        self.altura = altura
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.lado)

    def calcular_area(self) -> float:
        return self.base * self.altura

    def obtener_nombre(self) -> str:
        return "Paralelogramo"