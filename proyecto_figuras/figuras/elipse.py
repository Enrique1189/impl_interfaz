import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Elipse(Figura):
    """Representa una elipse con semieje mayor (a) y semieje menor (b)."""
    def __init__(self, semieje_a: float, semieje_b: float):
        if semieje_a <= 0 or semieje_b <= 0:
            raise ValueError("Los semiejes deben ser valores positivos.")
        self.semieje_a = semieje_a
        self.semieje_b = semieje_b

    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro (Circunferencia) aproximado de la elipse
        usando la fórmula de Ramanujan: π * [3(a+b) - sqrt((3a+b)(a+3b))]
        """
        a = self.semieje_a
        b = self.semieje_b
        # Es una aproximación muy precisa
        return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

    def calcular_area(self) -> float:
        """Calcula el área (π * a * b)."""
        return math.pi * self.semieje_a * self.semieje_b

    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la figura."""
        return "Elipse"