# figuras/rombo.py
from interfaces.figura import Figura

class Rombo(Figura):
    def __init__(self, diagonal_mayor: float, diagonal_menor: float, lado: float):
        if diagonal_mayor <= 0 or diagonal_menor <= 0 or lado <= 0:
            raise ValueError("Todos los valores deben ser positivos.")
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def calcular_area(self) -> float:
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def obtener_nombre(self) -> str:
        return "Rombo"
