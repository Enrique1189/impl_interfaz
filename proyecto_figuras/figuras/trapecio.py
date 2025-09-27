# figuras/trapecio.py
from interfaces.figura import Figura

class Trapecio(Figura):
    def __init__(self, base_mayor: float, base_menor: float, altura: float, lado1: float, lado2: float):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0 or lado1 <= 0 or lado2 <= 0:
            raise ValueError("Todos los valores deben ser positivos.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_perimetro(self) -> float:
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

    def calcular_area(self) -> float:
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def obtener_nombre(self) -> str:
        return "Trapecio"
