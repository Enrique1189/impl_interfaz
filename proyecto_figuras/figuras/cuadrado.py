class Cuadrado:
    def __init__(self, lado, _=0):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado