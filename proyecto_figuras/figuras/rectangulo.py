import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Rectangulo(Figura):
    def _init_(self, largo: float, ancho: float):
        if largo <= 0 or ancho <= 0:
            raise ValueError("El largo y el ancho deben ser valores positivos.")
        self.largo = largo
        self.ancho = ancho

    def calcular_perimetro(self) -> float:
        return 2 * (self.largo + self.ancho)

    def calcular_area(self) -> float:
        return self.largo * self.ancho

    def obtener_nombre(self) -> str:
        return "Rectángulo"