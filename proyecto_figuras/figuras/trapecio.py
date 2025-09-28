from interfaces.figura import Figura

class Trapecio(Figura):
    def __init__(self, base_mayor: float, base_menor: float, altura: float, lado1: float, lado2: float):
        if min(base_mayor, base_menor, altura, lado1, lado2) <= 0:
            raise ValueError("Todos los valores deben ser positivos.")
        self.B = base_mayor
        self.b = base_menor
        self.h = altura
        self.l1 = lado1
        self.l2 = lado2

    def calcular_perimetro(self) -> float:
        return self.B + self.b + self.l1 + self.l2

    def calcular_area(self) -> float:
        return ((self.B + self.b) * self.h) / 2

    def obtener_nombre(self) -> str:
        return "Trapecio"
