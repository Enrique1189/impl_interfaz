#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder

import tkinter as tk
from tkinter import ttk, messagebox

# Importar figuras
from figuras.circulo import Circulo
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.triangulo import TrianguloEquilatero
from figuras.triangulo_rectangulo import TrianguloRectangulo
from figuras.rombo import Rombo
from figuras.trapecio import Trapecio
from figuras.pentagono import PentagonoRegular
from figuras.elipse import Elipse


class InterfazFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras Geométricas")

        self.figura_actual = tk.StringVar()
        self.entradas = {}

        # Lista de figuras
        self.figuras = {
            "Círculo": (Circulo, ["Radio"]),
            "Cuadrado": (Cuadrado, ["Lado"]),
            "Rectángulo": (Rectangulo, ["Base", "Altura"]),
            "Triángulo Equilátero": (TrianguloEquilatero, ["Lado"]),
            "Triángulo Rectángulo": (TrianguloRectangulo, ["Cateto 1", "Cateto 2"]),
            "Rombo": (Rombo, ["Lado", "Diagonal Mayor", "Diagonal Menor"]),
            "Trapecio": (Trapecio, ["Base Mayor", "Base Menor", "Altura", "Lado 1", "Lado 2"]),
            "Pentágono Regular": (PentagonoRegular, ["Lado"]),
            "Elipse": (Elipse, ["Semieje a", "Semieje b"]),
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

        # Botones
        botones_frame = ttk.Frame(self.root)
        botones_frame.pack(pady=10)

        self.boton_calcular = ttk.Button(botones_frame, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=0, column=0, padx=5)

        self.boton_limpiar = ttk.Button(botones_frame, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.grid(row=0, column=1, padx=5)

        self.resultado_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.resultado_label.pack(pady=10)

    def actualizar_campos(self, event=None):
        for widget in self.campos_frame.winfo_children():
            widget.destroy()

        self.entradas.clear()
        figura = self.figura_actual.get()
        _, campos = self.figuras[figura]

        for campo in campos:
            label = ttk.Label(self.campos_frame, text=f"{campo}:")
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
                text=f"{figura.obtener_nombre()}\nÁrea: {area:.2f} | Perímetro: {perimetro:.2f}"
            )

        except ValueError:
            messagebox.showerror("Error", "Todos los valores deben ser numéricos y positivos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar(self):
        # Borra todos los campos de entrada
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        # Borra el resultado
        self.resultado_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazFiguras(root)
    root.mainloop()

