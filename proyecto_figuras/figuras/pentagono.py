import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Rectangulo(Figura):
    """Representa un rectángulo con una base y una altura dadas."""
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser valores positivos.")
        self.base = base
        self.altura = altura

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro (2 * (base + altura))."""
        return 2 * (self.base + self.altura)

    def calcular_area(self) -> float:
        """Calcula el área (base * altura)."""
        return self.base * self.altura

    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la figura."""
        return "Rectángulo"