# figuras/rombo.py
from interfaces.figura import Figura

class Rombo(Figura):
    def __init__(self, lado: float, diagonal_mayor: float, diagonal_menor: float):
        if lado <= 0 or diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("El lado y las diagonales deben ser valores positivos.")
        self.lado = lado
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_perimetro(self) -> float:
        return 4 * self.lado  # El perímetro de un rombo es 4 veces el valor de su lado

    def calcular_area(self) -> float:
        return (self.diagonal_mayor * self.diagonal_menor) / 2  # Fórmula para el área de un rombo

    def obtener_nombre(self) -> str:
        return "Rombo"