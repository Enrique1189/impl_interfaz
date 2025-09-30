from interfaces.figura import Figura

class Rectangulo(Figura):
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self) -> float:
        return self.ancho * self.alto

    def calcular_perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)

    def obtener_nombre(self) -> str:
        return "Rectángulo"
