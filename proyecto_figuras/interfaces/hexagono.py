from interfaces.figura import Figura
import math

class Hexagono(Figura):
    def __init__(self, lado: float, apotema: float):
        self.lado = lado
        self.apotema = apotema

    def area(self) -> float:
        perimetro = 6 * self.lado
        return (perimetro * self.apotema) / 2

    def perimetro(self) -> float:
        return 6 * self.lado
