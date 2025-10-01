# figuras/rectangulo.py
from interfaces.figura import Figura

class Rectangulo(Figura):
    def __init__(self, ancho: float, alto: float):
        if ancho <= 0 or alto <= 0:
            raise ValueError("El ancho y el alto deben ser valores positivos.")
        self.ancho = ancho
        self.alto = alto

    def calcular_perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)

    def calcular_area(self) -> float:
        return self.ancho * self.alto

    def obtener_nombre(self) -> str:
        return "Rectángulo"