from interfaces.figura import Figura

class Rombo(Figura):
    def __init__(self, diagonal_mayor: float, diagonal_menor: float, lado: float):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def calcular_area(self) -> float:
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def obtener_nombre(self) -> str:
        return "Rombo"
