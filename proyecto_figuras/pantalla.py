#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder

import tkinter as tk
from tkinter import messagebox

# Importar clases de figuras
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo
from figuras.trapecio import Trapecio
from figuras.hexagono import Hexagono
from figuras.rombo import Rombo
from figuras.pentagono import Pentagono
from figuras.deltoide import Deltoide
from figuras.heptagono import Heptagono
# Circulo lo dejamos sin modificar
from figuras.circulo import Circulo


class Pantalla:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de Figuras Geométricas")
        self.root.geometry("400x400")
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        tk.Label(self.root, text="Seleccione una figura:").pack(pady=10)

        figuras = [
            "Cuadrado", "Rectángulo", "Triángulo", "Trapecio",
            "Hexágono", "Círculo", "Rombo", "Pentágono",
            "Deltoide", "Heptágono"
        ]

        self.figura_var = tk.StringVar(value=figuras[0])
        figura_menu = tk.OptionMenu(self.root, self.figura_var, *figuras)
        figura_menu.pack(pady=10)

        tk.Button(self.root, text="Ingresar Datos", command=self.ingresar_datos).pack(pady=10)

    def ingresar_datos(self):
        figura = self.figura_var.get()
        if figura == "Cuadrado":
            self.ventana_datos("Cuadrado", ["Lado"], self.calcular_cuadrado)
        elif figura == "Rectángulo":
            self.ventana_datos("Rectángulo", ["Ancho", "Alto"], self.calcular_rectangulo)
        elif figura == "Triángulo":
            self.ventana_datos("Triángulo", ["Base", "Altura", "Lado 1", "Lado 2"], self.calcular_triangulo)
        elif figura == "Trapecio":
            self.ventana_datos("Trapecio", ["Base Mayor", "Base Menor", "Altura", "Lado 1", "Lado 2"], self.calcular_trapecio)
        elif figura == "Hexágono":
            self.ventana_datos("Hexágono", ["Lado", "Apotema"], self.calcular_hexagono)
        elif figura == "Círculo":
            self.ventana_datos("Círculo", ["Radio"], self.calcular_circulo)
        elif figura == "Rombo":
            self.ventana_datos("Rombo", ["Diagonal Mayor", "Diagonal Menor", "Lado"], self.calcular_rombo)
        elif figura == "Pentágono":
            self.ventana_datos("Pentágono", ["Lado", "Apotema"], self.calcular_pentagono)
        elif figura == "Deltoide":
            self.ventana_datos("Deltoide", ["Diagonal Mayor", "Diagonal Menor"], self.calcular_deltoide)
        elif figura == "Heptágono":
            self.ventana_datos("Heptágono", ["Lado", "Apotema"], self.calcular_heptagono)

    def ventana_datos(self, titulo, campos, callback):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)

        entries = {}
        for campo in campos:
            tk.Label(ventana, text=campo).pack(pady=5)
            entry = tk.Entry(ventana)
            entry.pack(pady=5)
            entries[campo] = entry

        def on_submit():
            try:
                valores = {campo: float(entries[campo].get()) for campo in campos}
                callback(valores)
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

        tk.Button(ventana, text="Calcular", command=on_submit).pack(pady=10)

    # ================= Cálculos =================

    def calcular_cuadrado(self, valores):
        figura = Cuadrado(valores["Lado"])
        self.mostrar_resultados(figura)

    def calcular_rectangulo(self, valores):
        figura = Rectangulo(valores["Ancho"], valores["Alto"])
        self.mostrar_resultados(figura)

    def calcular_triangulo(self, valores):
        figura = Triangulo(valores["Base"], valores["Altura"], valores["Lado 1"], valores["Lado 2"])
        self.mostrar_resultados(figura)

    def calcular_trapecio(self, valores):
        figura = Trapecio(valores["Base Menor"], valores["Base Mayor"], valores["Altura"], valores["Lado 1"], valores["Lado 2"])
        self.mostrar_resultados(figura)

    def calcular_hexagono(self, valores):
        figura = Hexagono(valores["Lado"], valores["Apotema"])
        self.mostrar_resultados(figura)

    def calcular_circulo(self, valores):
        figura = Circulo(valores["Radio"])
        # Intentamos soportar ambas variantes (area/perimetro o calcular_area/calcular_perimetro)
        try:
            area = figura.calcular_area()
            perimetro = figura.calcular_perimetro()
        except AttributeError:
            area = figura.area()
            perimetro = figura.perimetro()
        messagebox.showinfo("Resultados", f"Círculo\nPerímetro: {perimetro}\nÁrea: {area}")

    def calcular_rombo(self, valores):
        figura = Rombo(valores["Diagonal Mayor"], valores["Diagonal Menor"], valores["Lado"])
        self.mostrar_resultados(figura)

    def calcular_pentagono(self, valores):
        figura = Pentagono(valores["Lado"], valores["Apotema"])
        self.mostrar_resultados(figura)

    def calcular_deltoide(self, valores):
        figura = Deltoide(valores["Diagonal Mayor"], valores["Diagonal Menor"])
        self.mostrar_resultados(figura)

    def calcular_heptagono(self, valores):
        figura = Heptagono(valores["Lado"], valores["Apotema"])
        self.mostrar_resultados(figura)

    # ================= Mostrar =================

    def mostrar_resultados(self, figura):
        perimetro = figura.calcular_perimetro()
        area = figura.calcular_area()
        nombre = figura.obtener_nombre()
        messagebox.showinfo("Resultados", f"{nombre}\nPerímetro: {perimetro}\nÁrea: {area}")


if __name__ == "__main__":
    Pantalla()
