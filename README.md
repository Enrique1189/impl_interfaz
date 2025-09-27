# impl_interfaz

#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder
import tkinter as tk

# ============== Clases de figuras ===================
class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura) / 2
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class TrianguloRectangulo:
    def __init__(self, base, altura, hipotenusa):
        self.base = base
        self.altura = altura
        self.hipotenusa = hipotenusa
    def calcular_area(self):
        return (self.base * self.altura) / 2
    def calcular_perimetro(self):
        return self.base + self.altura + self.hipotenusa

class Trapecio:
    def __init__(self, base_mayor, base_menor, lado1, lado2, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura
    def calcular_area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2
    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

class Rombo:
    def __init__(self, lado, diagonal_mayor, diagonal_menor):
        self.lado = lado
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2
    def calcular_perimetro(self):
        return 4 * self.lado

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado * self.lado
    def calcular_perimetro(self):
        return 4 * self.lado

class Pentagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema
    def calcular_area(self):
        return (self.calcular_perimetro() * self.apotema) / 2
    def calcular_perimetro(self):
        return 5 * self.lado

class Paralelogramo:
    def __init__(self, base, lado, altura):
        self.base = base
        self.lado = lado
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.lado)

class Hexagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema
    def calcular_area(self):
        return (self.calcular_perimetro() * self.apotema) / 2
    def calcular_perimetro(self):
        return 6 * self.lado

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return 3 * self.radio * self.radio  # aproximación
    def calcular_perimetro(self):
        return 6 * self.radio  # aproximación

# ----------------- Interfaz Tkinter -----------------
ventana = tk.Tk()
ventana.title("Calculadora de Figuras Geométricas")
ventana.geometry("650x600")
ventana.config(bg="#f0f0f0")

# Título
titulo = tk.Label(ventana, text="Calculadora de Figuras Geométricas", font=("Arial", 20, "bold"), bg="#f0f0f0")
titulo.pack(pady=15)

# Selección 
figura_var = tk.StringVar(value="Triangulo")
figuras = [
    "Triangulo", "TrianguloRectangulo", "Trapecio", "Rombo",
    "Rectangulo", "Cuadrado", "Pentagono", "Paralelogramo", "Hexagono", "Circulo"
]
tk.Label(ventana, text="Selecciona la figura:", font=("Arial", 14), bg="#f0f0f0").pack()
figura_menu = tk.OptionMenu(ventana, figura_var, *figuras)
figura_menu.config(font=("Arial", 12), width=20)
figura_menu.pack(pady=10)

entrada_frame = tk.Frame(ventana, bg="#f0f0f0")
entrada_frame.pack(pady=10)

resultado_label = tk.Label(ventana, text="", font=("Arial", 16), fg="#3333ff", bg="#f0f0f0")
resultado_label.pack(pady=15)

# Funciones
def limpiar_entradas():
    for widget in entrada_frame.winfo_children():
        widget.destroy()

def crear_entradas():
    limpiar_entradas()
    fig = figura_var.get()
    global entradas
    entradas = {}
    
    campos = []
    if fig == "Triangulo":
        campos = ["lado1", "lado2", "lado3", "base", "altura"]
    elif fig == "TrianguloRectangulo":
        campos = ["base", "altura", "hipotenusa"]
    elif fig == "Trapecio":
        campos = ["base_mayor", "base_menor", "lado1", "lado2", "altura"]
    elif fig == "Rombo":
        campos = ["lado", "diagonal_mayor", "diagonal_menor"]
    elif fig == "Rectangulo":
        campos = ["base", "altura"]
    elif fig == "Cuadrado":
        campos = ["lado"]
    elif fig == "Pentagono":
        campos = ["lado", "apotema"]
    elif fig == "Paralelogramo":
        campos = ["base", "lado", "altura"]
    elif fig == "Hexagono":
        campos = ["lado", "apotema"]
    elif fig == "Circulo":
        campos = ["radio"]
    
    for c in campos:
        tk.Label(entrada_frame, text=c + ":", font=("Arial", 12), bg="#f0f0f0").pack()
        entradas[c] = tk.Entry(entrada_frame, font=("Arial", 12))
        entradas[c].pack(pady=3)

def calcular():
    fig = figura_var.get()
    valores = {c: float(entradas[c].get()) for c in entradas}
    if fig == "Triangulo":
        figura = Triangulo(**valores)
    elif fig == "TrianguloRectangulo":
        figura = TrianguloRectangulo(**valores)
    elif fig == "Trapecio":
        figura = Trapecio(**valores)
    elif fig == "Rombo":
        figura = Rombo(**valores)
    elif fig == "Rectangulo":
        figura = Rectangulo(**valores)
    elif fig == "Cuadrado":
        figura = Cuadrado(**valores)
    elif fig == "Pentagono":
        figura = Pentagono(**valores)
    elif fig == "Paralelogramo":
        figura = Paralelogramo(**valores)
    elif fig == "Hexagono":
        figura = Hexagono(**valores)
    elif fig == "Circulo":
        figura = Circulo(**valores)

    area = figura.calcular_area()
    perimetro = figura.calcular_perimetro()
    resultado_label.config(text=f"Área: {area}  Perímetro: {perimetro}")


btn_crear = tk.Button(ventana, text="Crear Entradas", command=crear_entradas, font=("Arial", 14, "bold"), bg="#66ccff", width=20, height=2)
btn_crear.pack(pady=8)
btn_calcular = tk.Button(ventana, text="Calcular Área y Perímetro", command=calcular, font=("Arial", 14, "bold"), bg="#66ff66", width=25, height=2)
btn_calcular.pack(pady=8)

ventana.mainloop()
