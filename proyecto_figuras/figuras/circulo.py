#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder
import math
from interfaces.figura import Figura # Asumiendo la existencia de esta interfaz/clase base

class Circulo(Figura):
    def _init_(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser un valor positivo.")
        self.radio = radio

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def obtener_nombre(self) -> str:
        return "Círculo"