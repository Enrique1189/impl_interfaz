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
from figuras.romboide import Romboide
from figuras.trapecio import Trapecio
from figuras.pentagono import Pentagono
from figuras.hexagono import Hexagono
from figuras.octagono import Octagono



class InterfazFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras Geométricas")

        self.figura_actual = tk.StringVar()
        self.entradas = {}

        # Lista de figuras
        self.figuras = {
            "Círculo": (Circulo, ["radio"]),
            "Cuadrado": (Cuadrado, ["lado"]),
            "Triangulo": (Triangulo, ["Base", "altura"]),
            "Rectángulo": (Rectangulo, ["base", "altura"]),
            "Rombo": (Rombo, ["diagonal_mayor", "diagonal_menor", "lado"]),
            "Romboide": (Romboide, ["base", "altura", "lado"]),
            "Trapecio": (Trapecio, ["base_mayor", "base_menor", "altura", "lado1", "lado2"]),
            "Pentágono": (Pentagono, ["lado"]),
            "Hexágono": (Hexagono, ["lado"]),  
            "Octágono": (Octagono, ["lado"]),
        }

        self.crear_widgets()

    def crear_widgets(self):
        ttk.Label(self.root, text="Selecciona una figura:").pack(pady=5)

        figuras_combobox = ttk.Combobox(
            self.root, textvariable=self.figura_actual,
            values=list(self.figuras.keys()), state="readonly"
        )
        figuras_combobox.pack(pady=5)
        figuras_combobox.bind("<<ComboboxSelected>>", self.actualizar_campos)

        self.campos_frame = ttk.Frame(self.root)
        self.campos_frame.pack(pady=10)

        self.boton_calcular = ttk.Button(
            self.root, text="Calcular", command=self.calcular
        )
        self.boton_calcular.pack(pady=10)

        self.resultado_label = ttk.Label(self.root, text="")
        self.resultado_label.pack(pady=10)

    def actualizar_campos(self, event=None):
        for widget in self.campos_frame.winfo_children():
            widget.destroy()

        self.entradas.clear()
        figura = self.figura_actual.get()
        _, campos = self.figuras[figura]

        for campo in campos:
            label = ttk.Label(self.campos_frame, text=f"{campo.capitalize()}:")
            label.pack()
            entrada = ttk.Entry(self.campos_frame)
            entrada.pack()
            self.entradas[campo] = entrada

    def calcular(self):
        figura_nombre = self.figura_actual.get()
        if not figura_nombre:
            messagebox.showerror("Error", "Selecciona una figura.")
            return

        clase_figura, campos = self.figuras[figura_nombre]

        try:
            valores = []
            for campo in campos:
                entrada_texto = self.entradas[campo].get()
                valor = float(entrada_texto)
                if valor <= 0:
                    raise ValueError
                valores.append(valor)

            figura = clase_figura(*valores)
            area = figura.calcular_area()
            perimetro = figura.calcular_perimetro()

            self.resultado_label.config(
                text=f"Área: {area:.2f} | Perímetro: {perimetro:.2f}"
            )

        except ValueError:
            messagebox.showerror("Error", "Todos los valores deben ser numéricos y positivos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazFiguras(root)
    root.mainloop()




