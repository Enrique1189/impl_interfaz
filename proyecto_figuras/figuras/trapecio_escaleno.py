import math
from interfaces.figura import Figura

class TrapecioEscaleno(Figura):
    def __init__(self, base_mayor: float, base_menor: float, lado1: float, lado2: float, altura: float):
        lados = [base_mayor, base_menor, lado1, lado2]
        if any(l <= 0 for l in lados) or altura <= 0:
            raise ValueError("Las dimensiones deben ser positivas.")
        if base_menor >= base_mayor:
            raise ValueError("La base menor debe ser menor que la base mayor.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura

    def calcular_perimetro(self) -> float:
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

    def calcular_area(self) -> float:
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

    def obtener_nombre(self) -> str:
        return "Trapecio Escaleno"
