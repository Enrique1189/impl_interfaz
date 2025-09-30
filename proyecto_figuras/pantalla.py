#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_perimetro(self) -> float:
        pass

    @abstractmethod
    def calcular_area(self) -> float:
        pass

    @abstractmethod
    def obtener_nombre(self) -> str:
        pass
import tkinter as tk
from tkinter import messagebox
import math

# ---------------- Clases de figuras ----------------
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_perimetro(self): return 2*math.pi*self.radio
    def calcular_area(self): return math.pi*self.radio**2

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def calcular_perimetro(self): return 4*self.lado
    def calcular_area(self): return self.lado**2

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_perimetro(self): return 2*(self.base+self.altura)
    def calcular_area(self): return self.base*self.altura

class Triangulo:
    def __init__(self, base, altura, lado1, lado2):
        self.base, self.altura, self.lado1, self.lado2 = base, altura, lado1, lado2
    def calcular_perimetro(self): return self.base+self.lado1+self.lado2
    def calcular_area(self): return (self.base*self.altura)/2

class Rombo:
    def __init__(self, d_mayor, d_menor, lado):
        self.d_mayor, self.d_menor, self.lado = d_mayor, d_menor, lado
    def calcular_perimetro(self): return 4*self.lado
    def calcular_area(self): return (self.d_mayor*self.d_menor)/2

class Trapecio:
    def __init__(self, b_mayor, b_menor, altura, lado1, lado2):
        self.b_mayor, self.b_menor, self.altura, self.lado1, self.lado2 = b_mayor, b_menor, altura, lado1, lado2
    def calcular_perimetro(self): return self.b_mayor+self.b_menor+self.lado1+self.lado2
    def calcular_area(self): return ((self.b_mayor+self.b_menor)*self.altura)/2

class Pentagono:
    def __init__(self, lado, apotema):
        self.lado, self.apotema = lado, apotema
    def calcular_perimetro(self): return 5*self.lado
    def calcular_area(self): return (self.calcular_perimetro()*self.apotema)/2

class Hexagono:
    def __init__(self, lado, apotema):
        self.lado, self.apotema = lado, apotema
    def calcular_perimetro(self): return 6*self.lado
    def calcular_area(self): return (self.calcular_perimetro()*self.apotema)/2

class Heptagono:
    def __init__(self, lado, apotema):
        self.lado, self.apotema = lado, apotema
    def calcular_perimetro(self): return 7*self.lado
    def calcular_area(self): return (self.calcular_perimetro()*self.apotema)/2

class Octagono:
    def __init__(self, lado, apotema):
        self.lado, self.apotema = lado, apotema
    def calcular_perimetro(self): return 8*self.lado
    def calcular_area(self): return (self.calcular_perimetro()*self.apotema)/2

# ---------------- Función genérica para crear ventana de figura ----------------
def crear_ventana(titulo, parametros, clase):
    def calcular():
        try:
            valores = [float(e.get()) for e in entradas]
            if any(v<=0 for v in valores): raise ValueError
            fig = clase(*valores)
            resultado.set(f"Perímetro: {fig.calcular_perimetro():.2f}\nÁrea: {fig.calcular_area():.2f}")
        except:
            messagebox.showerror("Error","Ingresa solo números positivos válidos")
    
    win = tk.Toplevel()
    win.title(titulo)
    entradas = []
    for param in parametros:
        tk.Label(win,text=param+":").pack()
        e = tk.Entry(win)
        e.pack()
        entradas.append(e)
    tk.Button(win,text="Calcular",command=calcular).pack(pady=5)
    resultado = tk.StringVar()
    tk.Label(win,textvariable=resultado).pack()

# ---------------- Ventana principal ----------------
ventana = tk.Tk()
ventana.title("Figuras Geométricas")
ventana.geometry("300x600")

# Botones para cada figura
tk.Button(ventana,text="Círculo", command=lambda: crear_ventana("Círculo", ["Radio"], Circulo)).pack(pady=5)
tk.Button(ventana,text="Cuadrado", command=lambda: crear_ventana("Cuadrado", ["Lado"], Cuadrado)).pack(pady=5)
tk.Button(ventana,text="Rectángulo", command=lambda: crear_ventana("Rectángulo", ["Base","Altura"], Rectangulo)).pack(pady=5)
tk.Button(ventana,text="Triángulo", command=lambda: crear_ventana("Triángulo", ["Base","Altura","Lado1","Lado2"], Triangulo)).pack(pady=5)
tk.Button(ventana,text="Rombo", command=lambda: crear_ventana("Rombo", ["Diagonal mayor","Diagonal menor","Lado"], Rombo)).pack(pady=5)
tk.Button(ventana,text="Trapecio", command=lambda: crear_ventana("Trapecio", ["Base mayor","Base menor","Altura","Lado1","Lado2"], Trapecio)).pack(pady=5)
tk.Button(ventana,text="Pentágono", command=lambda: crear_ventana("Pentágono", ["Lado","Apotema"], Pentagono)).pack(pady=5)
tk.Button(ventana,text="Hexágono", command=lambda: crear_ventana("Hexágono", ["Lado","Apotema"], Hexagono)).pack(pady=5)
tk.Button(ventana,text="Heptágono", command=lambda: crear_ventana("Heptágono", ["Lado","Apotema"], Heptagono)).pack(pady=5)
tk.Button(ventana,text="Octágono", command=lambda: crear_ventana("Octágono", ["Lado","Apotema"], Octagono)).pack(pady=5)

ventana.mainloop()
