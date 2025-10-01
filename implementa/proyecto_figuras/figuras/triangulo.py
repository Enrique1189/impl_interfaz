import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class TrianguloEquilatero(Figura):
    """Representa un triángulo equilátero con un lado dado."""
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro (3 * lado)."""
        return 3 * self.lado

    def calcular_area(self) -> float:
        """Calcula el área (sqrt(3)/4 * lado^2)."""
        # Fórmula del área: (lado^2 * sqrt(3)) / 4
        return (math.sqrt(3) / 4) * (self.lado ** 2)

    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la figura."""
        return "Triángulo Equilátero"