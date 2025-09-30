from interfaces.figura import Figura

class Heptagono(Figura):
    def __init__(self, lado: float, apotema: float):
        self.lado = lado
        self.apotema = apotema

    def calcular_area(self) -> float:
        return (self.calcular_perimetro() * self.apotema) / 2

    def calcular_perimetro(self) -> float:
        return 7 * self.lado

    def obtener_nombre(self) -> str:
        return "Heptágono"
