from interfaces.figura import Figura

class Rombo(Figura):
    def __init__(self, lado, diag_mayor, diag_menor):
        self.lado = lado
        self.diag_mayor = diag_mayor
        self.diag_menor = diag_menor

    def calcular_area(self):
        return (self.diag_mayor * self.diag_menor) / 2

    def calcular_perimetro(self):
        return 4 * self.lado

    def obtener_nombre(self):
        return "Rombo"
