from interfaces.figura import Figura

class Rombo(Figura):
    def __init__(self, lado: float, diagonal_mayor: float, diagonal_menor: float):
        if lado <= 0 or diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("Las dimensiones deben ser positivas.")
        self.lado = lado
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def calcular_area(self) -> float:
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def obtener_nombre(self) -> str:
        return "Rombo"
