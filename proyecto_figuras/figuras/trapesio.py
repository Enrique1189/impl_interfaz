import math
from interfaces.figura import Figura

class Trapecio(Figura):
    def __init__(self, base_mayor: float, base_menor: float, altura: float):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Las dimensiones deben ser positivas.")
        if base_menor >= base_mayor:
            raise ValueError("La base menor debe ser menor que la base mayor.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def calcular_perimetro(self) -> float:
        lado = math.sqrt(((self.base_mayor - self.base_menor) / 2) ** 2 + self.altura ** 2)
        return self.base_mayor + self.base_menor + 2 * lado

    def calcular_area(self) -> float:
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

    def obtener_nombre(self) -> str:
        return "Trapecio"
