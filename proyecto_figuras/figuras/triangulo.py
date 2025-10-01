from interfaces.figura import Figura

class Triangulo(Figura):
    def __init__(self, base: float, altura: float, lado1: float, lado2: float):
        if min(base, altura, lado1, lado2) <= 0:
            raise ValueError("Todos los lados deben ser positivos.")
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_perimetro(self) -> float:
        return self.base + self.lado1 + self.lado2

    def calcular_area(self) -> float:
        return 0.5 * self.base * self.altura

    def obtener_nombre(self) -> str:
        return "Triángulo"
