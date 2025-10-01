# figuras/rombo.py
from interfaces.figura import Figura

class Rombo(Figura):
    def __init__(self, d_mayor: float, d_menor: float, lado: float):
        if d_mayor <= 0 or d_menor <= 0 or lado <= 0:
            raise ValueError("Diagonales y lado deben ser positivos.")
        self.d_mayor = d_mayor
        self.d_menor = d_menor
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def calcular_area(self) -> float:
        return (self.d_mayor * self.d_menor) / 2

    def obtener_nombre(self) -> str:
        return "Rombo"

