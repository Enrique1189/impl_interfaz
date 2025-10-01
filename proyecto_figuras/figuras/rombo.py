import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Rombo(Figura):
    def _init_(self, diagonal_mayor: float, diagonal_menor: float):
        if diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("Las diagonales deben ser valores positivos.")
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_perimetro(self) -> float:
        lado = ((self.diagonal_mayor * 2 + self.diagonal_menor * 2) / 4) ** 0.5
        return 4 * lado

    def calcular_area(self) -> float:
        return 0.5 * self.diagonal_mayor * self.diagonal_menor

    def obtener_nombre(self) -> str:
        return "Rombo"