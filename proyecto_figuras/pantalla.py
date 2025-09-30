#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder
import tkinter as tk
from tkinter import ttk, messagebox

from figuras.circulo import Circulo
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo
from figuras.rombo import Rombo
from figuras.trapecio import Trapecio
from figuras.pentagono import Pentagono
from figuras.hexagono import Hexagono
from figuras.paralelogramo import Paralelogramo
from figuras.triangulorectangulo import TrianguloRectangulo


class CalculadoraFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras Geométricas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.figura_seleccionada = tk.StringVar()
        self.entradas = {}


        self.figuras = {
            "Círculo": (Circulo, ["radio"]),
            "Cuadrado": (Cuadrado, ["lado"]),
            "Rectángulo": (Rectangulo, ["base", "altura"]),
            "Triángulo": (Triangulo, ["base", "altura"]),
            "Triángulo Rectángulo": (TrianguloRectangulo, ["base", "altura"]),
            "Rombo": (Rombo, ["diagonal_mayor", "diagonal_menor", "lado"]),
            "Trapecio": (Trapecio, ["base_mayor", "base_menor", "altura", "lado1", "lado2"]),
            "Paralelogramo": (Paralelogramo, ["base", "altura", "lado"]),
            "Pentágono": (Pentagono, ["lado"]),
            "Hexágono": (Hexagono, ["lado"]),
        }

        self.crear_widgets()

    def crear_widgets(self):
        ttk.Label(self.root, text="Selecciona la figura:", font=("Arial", 12, "bold")).pack(pady=10)

        combo = ttk.Combobox(self.root, textvariable=self.figura_seleccionada,
                             values=list(self.figuras.keys()), state="readonly", width=25)
        combo.pack()
        combo.bind("<<ComboboxSelected>>", self.mostrar_campos)

        self.frame_campos = ttk.LabelFrame(self.root, text="Datos de la figura")
        self.frame_campos.pack(padx=20, pady=15, fill="x")

        boton_frame = tk.Frame(self.root)
        boton_frame.pack(pady=10)

        ttk.Button(boton_frame, text="Calcular", command=self.calcular).grid(row=0, column=0, padx=10)
        ttk.Button(boton_frame, text="Limpiar", command=self.limpiar).grid(row=0, column=1, padx=10)

    def mostrar_campos(self, event=None):

        for widget in self.frame_campos.winfo_children():
            widget.destroy()
        self.entradas.clear()

        figura = self.figura_seleccionada.get()
        _, campos = self.figuras[figura]

        for i, campo in enumerate(campos):
            ttk.Label(self.frame_campos, text=f"{campo.replace('_', ' ').capitalize()}:").grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = ttk.Entry(self.frame_campos, width=20)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entradas[campo] = entry

    def calcular(self):
        figura_nombre = self.figura_seleccionada.get()
        if not figura_nombre:
            messagebox.showwarning("Aviso", "Selecciona una figura.")
            return

        clase_figura, campos = self.figuras[figura_nombre]

        try:
            valores = []
            for campo in campos:
                valor = float(self.entradas[campo].get())
                if valor <= 0:
                    raise ValueError
                valores.append(valor)

            figura = clase_figura(*valores)
            area = figura.calcular_area()
            perimetro = figura.calcular_perimetro()

            messagebox.showinfo("Resultado", f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Los valores deben ser numéricos y positivos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar(self):
        for entry in self.entradas.values():
            entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraFiguras(root)
    root.mainloop()
