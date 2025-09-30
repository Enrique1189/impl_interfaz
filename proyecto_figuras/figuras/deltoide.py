from interfaces.figura import Figura

class Deltoide(Figura):
    def __init__(self, diagonal_mayor: float, diagonal_menor: float):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self) -> float:
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self) -> float:
        # Aproximación: se asume que los lados son simétricos
        lado1 = self.diagonal_mayor / 2
        lado2 = self.diagonal_menor / 2
        return 2 * (lado1 + lado2)

    def obtener_nombre(self) -> str:
        return "Deltoide"
