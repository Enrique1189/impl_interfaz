from interfaces.figura import Figura
import math

class Triangulo(Figura):
    def __init__(self, base: float, altura: float, lado1: float, lado2: float, lado3: float):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def perimetro(self) -> float:
        return self.lado1 + self.lado2 + self.lado3
