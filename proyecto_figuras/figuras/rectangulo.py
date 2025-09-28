from interfaces.figura import Figura

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser positivas.")
        self.base = base
        self.altura = altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def calcular_area(self) -> float:
        return self.base * self.altura

    def obtener_nombre(self) -> str:
        return "Rectángulo"
