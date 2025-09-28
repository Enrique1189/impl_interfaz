#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinderimport tkinter as tk
import tkinter as tk
from tkinter import ttk, messagebox

from figuras.circulo import Circulo
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo
from figuras.rombo import Rombo
from figuras.trapecio import Trapecio
from figuras.paralelogramo import Paralelogramo
from figuras.pentagono import Pentagono
from figuras.hexagono import Hexagono
from figuras.ovalo import Ovalo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas")
        self.geometry("500x400")
        self.resizable(False, False)

        self.figura_actual = None
        self.param_entries = {}

        self.crear_widgets()

    def crear_widgets(self):
        ttk.Label(self, text="Selecciona una figura:", font=("Arial", 12)).pack(pady=10)

        self.combo_figuras = ttk.Combobox(self, state="readonly", values=[
            "Círculo", "Cuadrado", "Rectángulo", "Triángulo",
            "Rombo", "Trapecio", "Paralelogramo", "Pentágono",
            "Hexágono", "Óvalo"
        ])
        self.combo_figuras.pack()
        self.combo_figuras.bind("<<ComboboxSelected>>", self.mostrar_parametros)

        self.param_frame = ttk.Frame(self)
        self.param_frame.pack(pady=20)

        self.boton_calcular = ttk.Button(self, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(pady=10)

        self.resultado_label = ttk.Label(self, text="", font=("Arial", 11), wraplength=400, justify="center")
        self.resultado_label.pack()

    def limpiar_parametros(self):
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        self.param_entries.clear()

    def mostrar_parametros(self, event):
        self.limpiar_parametros()
        figura = self.combo_figuras.get()

        parametros = {
            "Círculo": ["radio"],
            "Cuadrado": ["lado"],
            "Rectángulo": ["base", "altura"],
            "Triángulo": ["lado1", "lado2", "lado3"],
            "Rombo": ["diagonal_mayor", "diagonal_menor", "lado"],
            "Trapecio": ["base_mayor", "base_menor", "altura", "lado1", "lado2"],
            "Paralelogramo": ["base", "altura", "lado"],
            "Pentágono": ["lado", "apotema"],
            "Hexágono": ["lado", "apotema"],
            "Óvalo": ["eje_mayor", "eje_menor"]
        }

        for param in parametros.get(figura, []):
            label = ttk.Label(self.param_frame, text=f"{param.capitalize()}:")
            label.pack()
            entry = ttk.Entry(self.param_frame)
            entry.pack()
            self.param_entries[param] = entry

    def calcular(self):
        figura = self.combo_figuras.get()
        if not figura:
            messagebox.showwarning("Advertencia", "Selecciona una figura.")
            return

        try:
            valores = [float(entry.get()) for entry in self.param_entries.values()]
        except ValueError:
            messagebox.showerror("Error", "Todos los parámetros deben ser números válidos.")
            return

        try:
            # Crear la figura
            if figura == "Círculo":
                obj = Circulo(*valores)
            elif figura == "Cuadrado":
                obj = Cuadrado(*valores)
            elif figura == "Rectángulo":
                obj = Rectangulo(*valores)
            elif figura == "Triángulo":
                obj = Triangulo(*valores)
            elif figura == "Rombo":
                obj = Rombo(*valores)
            elif figura == "Trapecio":
                obj = Trapecio(*valores)
            elif figura == "Paralelogramo":
                obj = Paralelogramo(*valores)
            elif figura == "Pentágono":
                obj = Pentagono(*valores)
            elif figura == "Hexágono":
                obj = Hexagono(*valores)
            elif figura == "Óvalo":
                obj = Ovalo(*valores)
            else:
                raise ValueError("Figura no reconocida")

            area = obj.calcular_area()
            perimetro = obj.calcular_perimetro()

            self.resultado_label.config(
                text=f"Figura: {obj.obtener_nombre()}\nÁrea: {area:.2f}\nPerímetro: {perimetro:.2f}"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = App()
    app.mainloop()
