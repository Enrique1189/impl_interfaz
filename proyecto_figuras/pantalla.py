#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder

import tkinter as tk
from tkinter import ttk, messagebox
import math
from abc import ABC, abstractmethod

# Clase base abstracta
class Figura(ABC):
    @abstractmethod
    def calcular_perimetro(self) -> float:
        """Calcula el perímetro de la figura."""
        pass

    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula el área de la figura."""
        pass

    @abstractmethod
    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la figura."""
        pass

# Clases de figuras
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return math.pi * self.radio ** 2
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    def obtener_nombre(self):
        return "Círculo"

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado ** 2
    def calcular_perimetro(self):
        return 4 * self.lado
    def obtener_nombre(self):
        return "Cuadrado"

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    def obtener_nombre(self):
        return "Rectángulo"

class TrianguloEquilatero(Figura):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return (math.sqrt(3)/4) * self.lado**2
    def calcular_perimetro(self):
        return 3 * self.lado
    def obtener_nombre(self):
        return "Triángulo Equilátero"

class TrianguloRectangulo(Figura):
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2
        self.hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    def calcular_area(self):
        return (self.cateto1 * self.cateto2) / 2
    def calcular_perimetro(self):
        return self.cateto1 + self.cateto2 + self.hipotenusa
    def obtener_nombre(self):
        return "Triángulo Rectángulo"

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

class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
    def calcular_area(self):
        return ((self.base_mayor + self.base_menor)/2) * self.altura
    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2
    def obtener_nombre(self):
        return "Trapecio"

class PentagonoRegular(Figura):
    def __init__(self, lado):
        self.lado = lado
        self.apotema = lado / (2 * math.tan(math.pi/5))
    def calcular_area(self):
        return (5 * self.lado * self.apotema) / 2
    def calcular_perimetro(self):
        return 5 * self.lado
    def obtener_nombre(self):
        return "Pentágono Regular"

class Elipse(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calcular_area(self):
        return math.pi * self.a * self.b
    def calcular_perimetro(self):
        return math.pi * (3*(self.a+self.b) - math.sqrt((3*self.a+self.b)*(self.a+3*self.b)))
    def obtener_nombre(self):
        return "Elipse"

# Función para calcular
def calcular():
    figura = figura_var.get()
    try:
        if figura == "Círculo":
            r = float(entry1.get())
            obj = Circulo(r)
        elif figura == "Cuadrado":
            l = float(entry1.get())
            obj = Cuadrado(l)
        elif figura == "Rectángulo":
            b = float(entry1.get())
            h = float(entry2.get())
            obj = Rectangulo(b,h)
        elif figura == "Triángulo Equilátero":
            l = float(entry1.get())
            obj = TrianguloEquilatero(l)
        elif figura == "Triángulo Rectángulo":
            c1 = float(entry1.get())
            c2 = float(entry2.get())
            obj = TrianguloRectangulo(c1,c2)
        elif figura == "Rombo":
            l = float(entry1.get())
            d1 = float(entry2.get())
            d2 = float(entry3.get())
            obj = Rombo(l,d1,d2)
        elif figura == "Trapecio":
            bm = float(entry1.get())
            bm2 = float(entry2.get())
            h = float(entry3.get())
            l1 = float(entry4.get())
            l2 = float(entry5.get())
            obj = Trapecio(bm,bm2,h,l1,l2)
        elif figura == "Pentágono Regular":
            l = float(entry1.get())
            obj = PentagonoRegular(l)
        elif figura == "Elipse":
            a = float(entry1.get())
            b = float(entry2.get())
            obj = Elipse(a,b)
        else:
            messagebox.showerror("Error", "Selecciona una figura")
            return
        area = obj.calcular_area()
        perimetro = obj.calcular_perimetro()
        resultado_label.config(text=f"{obj.obtener_nombre()}\nÁrea: {area:.2f}\nPerímetro: {perimetro:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos")

# Función para mostrar los campos necesarios según la figura
def actualizar_campos(*args):
    for w in [entry1, entry2, entry3, entry4, entry5, label1, label2, label3, label4, label5]:
        w.grid_remove()
    fig = figura_var.get()
    if fig == "Círculo":
        label1.config(text="Radio:")
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
    elif fig == "Cuadrado" or fig == "Triángulo Equilátero" or fig == "Pentágono Regular":
        label1.config(text="Lado:")
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
    elif fig == "Rectángulo":
        label1.config(text="Base:")
        label2.config(text="Altura:")
        label1.grid(row=1,column=0)
        entry1.grid(row=1,column=1)
        label2.grid(row=2,column=0)
        entry2.grid(row=2,column=1)
    elif fig == "Triángulo Rectángulo":
        label1.config(text="Cateto 1:")
        label2.config(text="Cateto 2:")
        label1.grid(row=1,column=0)
        entry1.grid(row=1,column=1)
        label2.grid(row=2,column=0)
        entry2.grid(row=2,column=1)
    elif fig == "Rombo":
        label1.config(text="Lado:")
        label2.config(text="Diagonal Mayor:")
        label3.config(text="Diagonal Menor:")
        label1.grid(row=1,column=0)
        entry1.grid(row=1,column=1)
        label2.grid(row=2,column=0)
        entry2.grid(row=2,column=1)
        label3.grid(row=3,column=0)
        entry3.grid(row=3,column=1)
    elif fig == "Trapecio":
        label1.config(text="Base Mayor:")
        label2.config(text="Base Menor:")
        label3.config(text="Altura:")
        label4.config(text="Lado 1:")
        label5.config(text="Lado 2:")
        label1.grid(row=1,column=0)
        entry1.grid(row=1,column=1)
        label2.grid(row=2,column=0)
        entry2.grid(row=2,column=1)
        label3.grid(row=3,column=0)
        entry3.grid(row=3,column=1)
        label4.grid(row=4,column=0)
        entry4.grid(row=4,column=1)
        label5.grid(row=5,column=0)
        entry5.grid(row=5,column=1)
    elif fig == "Elipse":
        label1.config(text="Semieje a:")
        label2.config(text="Semieje b:")
        label1.grid(row=1,column=0)
        entry1.grid(row=1,column=1)
        label2.grid(row=2,column=0)
        entry2.grid(row=2,column=1)

# Ventana principal
root = tk.Tk()
root.title("Calculadora de Figuras")

figura_var = tk.StringVar()
figura_var.trace('w', actualizar_campos)

ttk.Label(root, text="Selecciona la figura:").grid(row=0,column=0)
figura_menu = ttk.Combobox(root, textvariable=figura_var)
figura_menu['values'] = ["Círculo","Cuadrado","Rectángulo","Triángulo Equilátero",
                         "Triángulo Rectángulo","Rombo","Trapecio","Pentágono Regular","Elipse"]
figura_menu.grid(row=0,column=1)

# Entradas y etiquetas
label1 = ttk.Label(root, text="")
label2 = ttk.Label(root, text="")
label3 = ttk.Label(root, text="")
label4 = ttk.Label(root, text="")
label5 = ttk.Label(root, text="")

entry1 = ttk.Entry(root)
entry2 = ttk.Entry(root)
entry3 = ttk.Entry(root)
entry4 = ttk.Entry(root)
entry5 = ttk.Entry(root)

# Botón de calcular
calc_btn = ttk.Button(root, text="Calcular", command=calcular)
calc_btn.grid(row=6, column=0, columnspan=2, pady=10)

# Resultado
resultado_label = ttk.Label(root, text="", font=("Arial", 12))
resultado_label.grid(row=7, column=0, columnspan=2)

root.mainloop()
