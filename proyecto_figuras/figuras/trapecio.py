import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Trapecio(Figura):
    def _init_(self, base_mayor: float, base_menor: float, altura: float):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Las bases y la altura deben ser valores positivos.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def calcular_perimetro(self) -> float:
        lado_lateral = ((self.base_mayor - self.base_menor) * 2 + self.altura * 2) ** 0.5
        return self.base_mayor + self.base_menor + 2 * lado_lateral

    def calcular_area(self) -> float:
        return 0.5 * (self.base_mayor + self.base_menor) * self.altura

    def obtener_nombre(self) -> str:
        return "Trapecio"