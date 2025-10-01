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
from figuras.octagono import Octagono

import sys
import traceback


def mostrar_error(exctype, value, tb):
    mensaje = ''.join(traceback.format_exception(exctype, value, tb))
    print(mensaje)
    messagebox.showerror("Error inesperado", mensaje)


sys.excepthook = mostrar_error


class InterfazFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras Geométricas")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#474242")

        self.figura_actual = tk.StringVar()
        self.entradas = {}

        self.figuras = {
            "Círculo": (Circulo, ["radio"]),
            "Cuadrado": (Cuadrado, ["lado"]),
            "Triángulo Rectángulo": (Triangulo, ["base", "altura"]),
            "Rectángulo": (Rectangulo, ["base", "altura"]),
            "Rombo": (Rombo, ["diagonal_mayor", "diagonal_menor", "lado"]),
            "Trapecio": (Trapecio, ["base_mayor", "base_menor", "altura", "lado1", "lado2"]),
            "Pentágono": (Pentagono, ["lado"]),
            "Hexágono": (Hexagono, ["lado"]),
            "Octágono": (Octagono, ["lado"]),
        }

        self.crear_widgets()

    def crear_widgets(self):
        
        titulo = ttk.Label(
            self.root,
            text="Calculadora de Figuras Geométricas",
            font=("Helvetica", 18, "bold"),
            background="#f5f5f5",
            foreground="#333",
        )
        titulo.pack(pady=(20, 10))

        
        seleccion_frame = ttk.Frame(self.root)
        seleccion_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(
            seleccion_frame,
            text="Selecciona una figura:",
            font=("Helvetica", 12),
            background="#f5f5f5",
            foreground="#555"
        ).pack(anchor="w")

        figuras_combobox = ttk.Combobox(
            seleccion_frame,
            textvariable=self.figura_actual,
            values=list(self.figuras.keys()),
            state="readonly",
            font=("Helvetica", 11)
        )
        figuras_combobox.pack(fill="x", pady=6)
        figuras_combobox.bind("<<ComboboxSelected>>", self.actualizar_campos)

        
        self.campos_frame = ttk.LabelFrame(
            self.root,
            text="Parámetros",
            padding=(15, 10),
            style="Campos.TLabelframe"
        )
        self.campos_frame.pack(padx=20, pady=15, fill="both", expand=True)

        
        self.boton_calcular = ttk.Button(
            self.root, text="Calcular", command=self.calcular
        )
        self.boton_calcular.pack(pady=(10, 15), ipadx=10, ipady=5)

        
        self.resultado_label = ttk.Label(
            self.root,
            text="",
            font=("Helvetica", 14, "bold"),
            background="#f5f5f5",
            foreground="#007ACC",
            justify="center"
        )
        self.resultado_label.pack(pady=10)

    
        estilo = ttk.Style()
        estilo.configure(
            "Campos.TLabelframe",
            background="#f5f5f5",
            font=("Helvetica", 12, "bold"),
            foreground="#444"
        )
        estilo.configure(
            "TLabel",
            background="#504949",
            font=("Helvetica", 11),
            foreground="#333"
        )
        estilo.configure(
            "TEntry",
            font=("Helvetica", 11)
        )
        estilo.configure(
            "TButton",
            font=("Helvetica", 12, "bold")
        )

    def actualizar_campos(self, event=None):
        for widget in self.campos_frame.winfo_children():
            widget.destroy()

        self.entradas.clear()
        figura = self.figura_actual.get()
        if not figura:
            return
        _, campos = self.figuras[figura]

        for campo in campos:
            label = ttk.Label(self.campos_frame, text=f"{campo.replace('_', ' ').capitalize()}:")
            label.pack(anchor="w", padx=5, pady=(8, 2))
            entrada = ttk.Entry(self.campos_frame)
            entrada.pack(fill="x", padx=5, pady=(0, 5))
            self.entradas[campo] = entrada

    def calcular(self):
        figura_nombre = self.figura_actual.get()
        if not figura_nombre:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una figura.")
            return

        figura_clase, campos = self.figuras[figura_nombre]

        valores = {}
        try:
            for campo in campos:
                valor_str = self.entradas[campo].get()
                if valor_str.strip() == "":
                    raise ValueError(f"El campo '{campo.replace('_', ' ')}' no puede estar vacío.")
                valor = float(valor_str)
                if valor <= 0:
                    raise ValueError(f"El valor de '{campo.replace('_', ' ')}' debe ser mayor que cero.")
                valores[campo] = valor
        except ValueError as e:
            messagebox.showerror("Error de entrada", f"Entrada inválida: {e}")
            return

    
        print(f"Creando {figura_nombre} con valores: {valores}")

        try:
            figura_obj = figura_clase(**valores)
        except TypeError as e:
            messagebox.showerror("Error", f"Error al crear la figura: {e}")
            print(f"Error TypeError: {e}")
            return
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear la figura: {e}")
            print(f"Error general: {e}")
            return

        try:
            area = figura_obj.area()
            perimetro = figura_obj.perimetro()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo calcular: {e}")
            print(f"Error cálculo: {e}")
            return

        resultado_texto = f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}"
        self.resultado_label.config(text=resultado_texto)


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazFiguras(root)
    root.mainloop()
