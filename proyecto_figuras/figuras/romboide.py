# figuras/romboide.py
from interfaces.figura import Figura

class Romboide(Figura):
    def __init__(self, base: float, altura: float, lado: float):
        if base <= 0 or altura <= 0 or lado <= 0:
            raise ValueError("La base, altura y el lado deben ser valores positivos.")
        self.base = base
        self.altura = altura
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.lado)  # El perímetro es 2 veces la suma de la base y el lado

    def calcular_area(self) -> float:
        return self.base * self.altura  # El área de un romboide se calcula base * altura

    def obtener_nombre(self) -> str:
        return "Romboide"