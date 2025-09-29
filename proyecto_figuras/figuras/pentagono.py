import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class PentagonoRegular(Figura):
    """Representa un pentágono regular con un lado dado."""
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado
        # Calcular el apotema: a = lado / (2 * tan(180/5))
        self.apotema = self.lado / (2 * math.tan(math.pi / 5))

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro (5 * lado)."""
        return 5 * self.lado

    def calcular_area(self) -> float:
        """Calcula el área ((Perímetro * Apotema) / 2)."""
        perimetro = self.calcular_perimetro()
        return (perimetro * self.apotema) / 2

    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la figura."""
        return "Pentágono Regular"