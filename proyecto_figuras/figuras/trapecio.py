# figuras/trapecio.py
from interfaces.figura import Figura

class Trapecio(Figura):
    def __init__(self, base_mayor: float, base_menor: float, altura: float, lado_izquierdo: float, lado_derecho: float):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0 or lado_izquierdo <= 0 or lado_derecho <= 0:
            raise ValueError("Las bases, altura y los lados deben ser valores positivos.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado_izquierdo = lado_izquierdo
        self.lado_derecho = lado_derecho

    def calcular_perimetro(self) -> float:
        # El perímetro es la suma de las longitudes de los 4 lados
        return self.base_mayor + self.base_menor + self.lado_izquierdo + self.lado_derecho

    def calcular_area(self) -> float:
        # Fórmula del área de un trapecio: (base_mayor + base_menor) * altura / 2
        return (self.base_mayor + self.base_menor) * self.altura / 2

    def obtener_nombre(self) -> str:
        return "Trapecio"
