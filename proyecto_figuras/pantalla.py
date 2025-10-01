import tkinter as tk
from tkinter import ttk, messagebox
import math

# ====================================================================
# A. Importación de Clases de Figuras
# ====================================================================

try:
    from figuras.circulo import Circulo
    from figuras.Cuadrado import Cuadrado
    from figuras.rectangulo import Rectangulo
    from figuras.triangulo import Triangulo
    from figuras.trapecio import Trapecio
    from figuras.rombo import Rombo
    from figuras.paralelogramo import Paralelogramo
    from figuras.elipse import Elipse
    from figuras.PentagonoRegular import PentagonoRegular
    from figuras.hexagonoregular import HexagonoRegular
except ImportError as e:
    print(f"Error al importar clases de figuras. Revisa la ruta: {e}")

# ====================================================================
# B. Diccionario de Figuras y Parámetros
# ====================================================================

FIGURAS = {
    "Círculo": (Circulo, ["radio"]),
    "Cuadrado": (Cuadrado, ["lado"]),
    "Rectángulo": (Rectangulo, ["base", "altura"]),
    "Triángulo": (Triangulo, ["lado_a (Base)", "lado_b", "lado_c", "altura"]),
    "Trapecio": (Trapecio, ["base_mayor", "base_menor", "altura", "lado1", "lado2"]),
    "Rombo": (Rombo, ["diagonal_mayor", "diagonal_menor", "lado"]),
    "Paralelogramo": (Paralelogramo, ["base", "altura", "lado_adyacente"]),
    "Elipse": (Elipse, ["semieje_mayor", "semieje_menor"]),
    "Pentágono Regular": (PentagonoRegular, ["lado"]),
    "Hexágono Regular": (HexagonoRegular, ["lado"]),
}


class CalculadoraFiguras(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Geométrica con Tkinter")
        self.geometry("600x400")
        
        self.figure_entries = {}
        self.selected_figure = tk.StringVar(self)
        self.selected_figure.set("Selecciona una Figura")
        
        self.create_widgets()
        
    def create_widgets(self):
        control_frame = ttk.Frame(self, padding="10")
        control_frame.pack(fill='x')

        ttk.Label(control_frame, text="Figura:").pack(side=tk.LEFT, padx=5)
        
        figure_options = list(FIGURAS.keys())
        self.figure_combobox = ttk.Combobox(
            control_frame, 
            textvariable=self.selected_figure, 
            values=figure_options, 
            state="readonly"
        )
        self.figure_combobox.pack(side=tk.LEFT, fill='x', expand=True, padx=5)
        self.figure_combobox.bind("<<ComboboxSelected>>", self.show_parameters)

        self.param_frame = ttk.Frame(self, padding="10")
        self.param_frame.pack(fill='both', expand=True)

        self.result_frame = ttk.Frame(self, padding="10")
        self.result_frame.pack(fill='x')
        
        self.area_label = ttk.Label(self.result_frame, text="Área: ")
        self.area_label.pack(anchor='w', pady=2)
        
        self.perimeter_label = ttk.Label(self.result_frame, text="Perímetro: ")
        self.perimeter_label.pack(anchor='w', pady=2)
        
        self.calc_button = ttk.Button(self, text="Calcular", command=self.calculate)
        self.calc_button.pack(pady=10)

    def clear_parameters(self):
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        self.figure_entries.clear()

    def show_parameters(self, event):
        self.clear_parameters()
        self.area_label.config(text="Área: ")
        self.perimeter_label.config(text="Perímetro: ")
        
        figure_name = self.selected_figure.get()
        if figure_name in FIGURAS:
            _, params = FIGURAS[figure_name]
            
            for i, param in enumerate(params):
                row_frame = ttk.Frame(self.param_frame)
                row_frame.pack(fill='x', pady=2)
                
                ttk.Label(row_frame, text=f"{param}:").pack(side=tk.LEFT, padx=5, anchor='w')
                
                entry = ttk.Entry(row_frame)
                entry.pack(side=tk.RIGHT, fill='x', expand=True, padx=5)
                self.figure_entries[param] = entry
                
    def calculate(self):
        figure_name = self.selected_figure.get()
        if figure_name not in FIGURAS or figure_name == "Selecciona una Figura":
            messagebox.showwarning("Error", "Por favor, selecciona una figura primero.")
            return

        FigureClass, params = FIGURAS[figure_name]
        param_values = []
        
        try:
            for param in params:
                value_str = self.figure_entries[param].get()
                value = float(value_str)
                param_values.append(value)
                
        except ValueError:
            messagebox.showerror("Error de Entrada", "Todos los valores deben ser números válidos.")
            return
        
        try:
            figura_instance = FigureClass(*param_values) 
            
            area = figura_instance.calcular_area()
            perimetro = figura_instance.calcular_perimetro()
            
            self.area_label.config(text=f"Área: {area:.4f} unidades cuadradas")
            self.perimeter_label.config(text=f"Perímetro: {perimetro:.4f} unidades")
            
        except ValueError as e:
            messagebox.showerror("Error de Cálculo", str(e))
        except Exception as e:
            messagebox.showerror("Error Desconocido", f"Ocurrió un error: {e}")

# ====================================================================
# C. Ejecución de la Aplicación
# ====================================================================

if __name__ == "__main__":
    app = CalculadoraFiguras()
    app.mainloop()