from interfaces.figura import Figura
import math

class Pentagono(Figura):
    def __init__(self, lado: float, apotema: float):
        self.lado = lado
        self.apotema = apotema

    def area(self) -> float:
        perimetro = 5 * self.lado
        return (perimetro * self.apotema) / 2

    def perimetro(self) -> float:
        return 5 * self.lado
