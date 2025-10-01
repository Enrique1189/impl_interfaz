# figuras/triangulo.py
import math
from interfaces.figura import Figura

class Triangulo(Figura):
    def __init__(self, lado_a: float, lado_b: float, lado_c: float):
        if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
            raise ValueError("Los lados deben ser valores positivos.")
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

        # Comprobamos si es un triángulo válido (desigualdad triangular)
        if (lado_a + lado_b <= lado_c) or (lado_a + lado_c <= lado_b) or (lado_b + lado_c <= lado_a):
            raise ValueError("Los lados proporcionados no forman un triángulo válido.")

    def calcular_perimetro(self) -> float:
        # El perímetro de un triángulo es la suma de sus tres lados
        return self.lado_a + self.lado_b + self.lado_c

    def calcular_area(self) -> float:
        # Calculamos el semiperímetro
        s = (self.lado_a + self.lado_b + self.lado_c) / 2
        # Usamos la fórmula de Herón para calcular el área
        area = math.sqrt(s * (s - self.lado_a) * (s - self.lado_b) * (s - self.lado_c))
        return area

    def obtener_nombre(self) -> str:
        return "Triángulo"