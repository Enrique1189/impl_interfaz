import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Rombo(Figura):
    """Representa un rombo con un lado y las longitudes de sus diagonales dadas."""
    def __init__(self, lado: float, diagonal_mayor: float, diagonal_menor: float):
        if lado <= 0 or diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("El lado y las diagonales deben ser valores positivos.")
        self.lado = lado
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro (4 * lado)."""
        return 4 * self.lado

    def calcular_area(self) -> float:
        """Calcula el área ((Diagonal Mayor * Diagonal Menor) / 2)."""
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la figura."""
        return "Rombo"