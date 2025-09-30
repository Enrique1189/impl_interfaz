from interfaces.figura import Figura

class Heptagono(Figura):
    def __init__(self, lado: float, apotema: float):
        self.lado = lado
        self.apotema = apotema

    def area(self) -> float:
        perimetro = 7 * self.lado
        return (perimetro * self.apotema) / 2

    def perimetro(self) -> float:
        return 7 * self.lado
