import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Trapecio(Figura):
    """Representa un trapecio con dos bases paralelas, altura y lados no paralelos."""
    def __init__(self, base_mayor: float, base_menor: float, altura: float, lado1: float, lado2: float):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0 or lado1 <= 0 or lado2 <= 0:
            raise ValueError("Todas las dimensiones deben ser valores positivos.")
        if base_menor >= base_mayor:
             raise ValueError("La base mayor debe ser más grande que la base menor.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1 # Lado no paralelo 1
        self.lado2 = lado2 # Lado no paralelo 2

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro (suma de todos los lados)."""
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

    def calcular_area(self) -> float:
        """Calcula el área ((base_mayor + base_menor) / 2 * altura)."""
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la figura."""
        return "Trapecio"