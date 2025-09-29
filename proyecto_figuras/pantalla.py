# Aquí se desarrolla la implementación de las clases de figuras
# en una interfaz gráfica usando Tkinter

# interfaz_tkinter.py
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


class InterfazFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras")

        self.figura_actual = tk.StringVar()
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
        ttk.Label(self.root, text="Selecciona la figura:").grid(row=0, column=0, padx=5, pady=5)

        combo = ttk.Combobox(self.root, textvariable=self.figura_actual,
                             values=list(self.figuras.keys()), state="readonly")
        combo.grid(row=0, column=1, padx=5, pady=5)
        combo.bind("<<ComboboxSelected>>", self.mostrar_campos)

        self.frame_campos = ttk.LabelFrame(self.root, text="Datos de la figura")
        self.frame_campos.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        ttk.Button(self.root, text="Calcular", command=self.calcular).grid(row=2, column=0, pady=10)
        ttk.Button(self.root, text="Limpiar", command=self.limpiar).grid(row=2, column=1, pady=10)

    def mostrar_campos(self, event=None):
        for widget in self.frame_campos.winfo_children():
            widget.destroy()

        self.entradas.clear()
        figura = self.figura_actual.get()
        _, campos = self.figuras[figura]

        for i, campo in enumerate(campos):
            ttk.Label(self.frame_campos, text=f"{campo.capitalize()}:").grid(row=i, column=0, padx=5, pady=5)
            entrada = ttk.Entry(self.frame_campos)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.entradas[campo] = entrada

    def calcular(self):
        figura_nombre = self.figura_actual.get()
        if not figura_nombre:
            messagebox.showwarning("Aviso", "Selecciona una figura.")
            return

        clase_figura, campos = self.figuras[figura_nombre]

        try:
            valores = []
            for campo in campos:
                texto = self.entradas[campo].get()
                valor = float(texto)
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
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazFiguras(root)
    root.mainloop()
