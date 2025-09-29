class Rombo:
    def __init__(self, d_mayor, d_menor, lado):
        self.d_mayor = d_mayor
        self.d_menor = d_menor
        self.lado = lado

    def area(self):
        return (self.d_mayor * self.d_menor) / 2

    def perimetro(self):
        return 4 * self.lado


# Ejemplo
ro = Rombo(10, 6, 5)
print("Área del rombo:", ro.area())
print("Perímetro del rombo:", ro.perimetro())

