import math
from interfaces.figura import Figura

class Hexagono(Figura):
    def __init__(self, lado: float, apotema: float):
        if min(lado, apotema) <= 0:
            raise ValueError("Lado y apotema deben ser positivos.")
        self.lado = lado
        self.apotema = apotema

    def calcular_perimetro(self) -> float:
        return 6 * self.lado

    def calcular_area(self) -> float:
        return (self.calcular_perimetro() * self.apotema) / 2

    def obtener_nombre(self) -> str:
        return "Hexágono"
