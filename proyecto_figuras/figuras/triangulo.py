from interfaces.figura import Figura

class Triangulo(Figura):
    def __init__(self, base: float, altura: float, lado1: float, lado2: float):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_perimetro(self) -> float:
        return self.base + self.lado1 + self.lado2

    def obtener_nombre(self) -> str:
        return "Triángulo"
