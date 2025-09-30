from interfaces.figura import Figura

class Octagono(Figura):
    def __init__(self, lado: float, apotema: float):
        self.lado = lado
        self.apotema = apotema

    def area(self) -> float:
        perimetro = 8 * self.lado
        return (perimetro * self.apotema) / 2

    def perimetro(self) -> float:
        return 8 * self.lado
