import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class TrianguloRectangulo(Figura):
    """Representa un triángulo rectángulo con base (cateto1) y altura (cateto2) dadas."""
    def __init__(self, cateto1: float, cateto2: float):
        if cateto1 <= 0 or cateto2 <= 0:
            raise ValueError("Los catetos deben ser valores positivos.")
        self.cateto1 = cateto1
        self.cateto2 = cateto2
        # Calcula la hipotenusa usando el Teorema de Pitágoras: h = sqrt(a^2 + b^2)
        self.hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro (cateto1 + cateto2 + hipotenusa)."""
        return self.cateto1 + self.cateto2 + self.hipotenusa

    def calcular_area(self) -> float:
        """Calcula el área ((base * altura) / 2)."""
        # Los catetos actúan como base y altura
        return (self.cateto1 * self.cateto2) / 2

    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la figura."""
        return "Triángulo Rectángulo"