class Cuadrado:
    def __init__ (self, lado):
        self.lado = lado

    def area (self):
        return self.lado ** 2

    def  perimetro (self):
        return 4 * self.lado

c = Cuadrado (5)
print ("Area del cuadrado:", c.area()) 
print("Perimetro del cuadrado:", c.perimetro())      