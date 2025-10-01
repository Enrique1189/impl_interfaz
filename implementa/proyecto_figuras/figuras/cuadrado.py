import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Cuadrado(Figura):
    """Representa un cuadrado con un lado dado."""
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro (4 * lado)."""
        return 4 * self.lado

    def calcular_area(self) -> float:
        """Calcula el área (lado ** 2)."""
        return self.lado ** 2

    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la figura."""
        return "Cuadrado"

# Ejemplo de uso:
# cuadrado = Cuadrado(5.0)
# print(f"Área del {cuadrado.obtener_nombre()}: {cuadrado.calcular_area()}")
# print(f"Perímetro del {cuadrado.obtener_nombre()}: {cuadrado.calcular_perimetro()}")