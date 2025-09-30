from interfaces.figura import Figura

class Cuadrado(Figura):
    def __init__(self, lado: float):
        self.lado = lado

    def area(self) -> float:
        return self.lado * self.lado

    def perimetro(self) -> float:
        return 4 * self.lado

