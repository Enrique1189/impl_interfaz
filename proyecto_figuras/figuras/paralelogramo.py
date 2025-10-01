from interfaces.figura import Figura

class Paralelogramo(Figura):
    def __init__(self, base: float, altura: float, lado: float):
        if min(base, altura, lado) <= 0:
            raise ValueError("Todos los valores deben ser positivos.")
        self.base = base
        self.altura = altura
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.lado)

    def calcular_area(self) -> float:
        return self.base * self.altura

    def obtener_nombre(self) -> str:
        return "Paralelogramo"
