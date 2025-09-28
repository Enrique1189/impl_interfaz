from interfaces.figura import Figura

class Rombo(Figura):
    def __init__(self, diagonal_mayor: float, diagonal_menor: float, lado: float):
        if min(diagonal_mayor, diagonal_menor, lado) <= 0:
            raise ValueError("Todos los valores deben ser positivos.")
        self.D = diagonal_mayor
        self.d = diagonal_menor
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def calcular_area(self) -> float:
        return (self.D * self.d) / 2

    def obtener_nombre(self) -> str:
        return "Rombo"
