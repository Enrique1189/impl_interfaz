from interfaces.figura import Figura

class Trapecio(Figura):
    def __init__(self, base_menor: float, base_mayor: float, altura: float, lado1: float, lado2: float):
        self.base_menor = base_menor
        self.base_mayor = base_mayor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self) -> float:
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self) -> float:
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

    def obtener_nombre(self) -> str:
        return "Trapecio"
