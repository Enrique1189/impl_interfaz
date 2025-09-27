#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder



import tkinter as tk
from tkinter import ttk, messagebox
import math

# Definimos las clases de figuras (simplificadas sin herencia aquí para hacerlo autónomo)
class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser positivo")
        self.radio = radio
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    def calcular_area(self):
        return math.pi * self.radio ** 2
    def obtener_nombre(self):
        return "Círculo"

class Cuadrado:
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo")
        self.lado = lado
    def calcular_perimetro(self):
        return 4 * self.lado
    def calcular_area(self):
        return self.lado ** 2
    def obtener_nombre(self):
        return "Cuadrado"

class Elipse:
    def __init__(self, radio_mayor, radio_menor):
        if radio_mayor <= 0 or radio_menor <= 0:
            raise ValueError("Los radios deben ser positivos")
        self.radio_mayor = radio_mayor
        self.radio_menor = radio_menor
    def calcular_perimetro(self):
        h = ((self.radio_mayor - self.radio_menor)**2) / ((self.radio_mayor + self.radio_menor)**2)
        return math.pi * (self.radio_mayor + self.radio_menor) * (1 + (3*h)/(10 + math.sqrt(4 - 3*h)))
    def calcular_area(self):
        return math.pi * self.radio_mayor * self.radio_menor
    def obtener_nombre(self):
        return "Elipse"

class Paralelogramo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser positivos")
        self.base = base
        self.altura = altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    def calcular_area(self):
        return self.base * self.altura
    def obtener_nombre(self):
        return "Paralelogramo"

class Rectangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser positivos")
        self.base = base
        self.altura = altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    def calcular_area(self):
        return self.base * self.altura
    def obtener_nombre(self):
        return "Rectángulo"

class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor):
        if diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("Las diagonales deben ser positivas")
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
    def calcular_perimetro(self):
        lado = ((self.diagonal_mayor/2)**2 + (self.diagonal_menor/2)**2)**0.5
        return 4 * lado
    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor)/2
    def obtener_nombre(self):
        return "Rombo"

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Las dimensiones deben ser positivas")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
    def calcular_perimetro(self):
        lado_oblicuo = math.sqrt((self.base_mayor - self.base_menor)**2 + self.altura**2)
        return self.base_mayor + self.base_menor + 2*lado_oblicuo
    def calcular_area(self):
        return 0.5 * (self.base_mayor + self.base_menor) * self.altura
    def obtener_nombre(self):
        return "Trapecio"

class TrianguloRectangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser positivos")
        self.base = base
        self.altura = altura
    def calcular_perimetro(self):
        hipotenusa = math.sqrt(self.base**2 + self.altura**2)
        return self.base + self.altura + hipotenusa
    def calcular_area(self):
        return 0.5 * self.base * self.altura
    def obtener_nombre(self):
        return "Triángulo Rectángulo"

# Diccionario para facilitar la creación de instancias
FIGURAS = {
    "Círculo": {"clase": Circulo, "parametros": ["Radio"]},
    "Cuadrado": {"clase": Cuadrado, "parametros": ["Lado"]},
    "Elipse": {"clase": Elipse, "parametros": ["Radio Mayor", "Radio Menor"]},
    "Paralelogramo": {"clase": Paralelogramo, "parametros": ["Base", "Altura"]},
    "Rectángulo": {"clase": Rectangulo, "parametros": ["Base", "Altura"]},
    "Rombo": {"clase": Rombo, "parametros": ["Diagonal Mayor", "Diagonal Menor"]},
    "Trapecio": {"clase": Trapecio, "parametros": ["Base Mayor", "Base Menor", "Altura"]},
    "Triángulo Rectángulo": {"clase": TrianguloRectangulo, "parametros": ["Base", "Altura"]},
}

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas")
        self.geometry("400x400")
        self.resizable(False, False)

        # Selección figura
        self.lbl_figura = tk.Label(self, text="Seleccione la figura:")
        self.lbl_figura.pack(pady=5)

        self.figura_var = tk.StringVar()
        self.figura_combo = ttk.Combobox(self, textvariable=self.figura_var, state="readonly")
        self.figura_combo['values'] = list(FIGURAS.keys())
        self.figura_combo.bind("<<ComboboxSelected>>", self.mostrar_campos)
        self.figura_combo.pack(pady=5)

        # Frame para parámetros
        self.param_frame = tk.Frame(self)
        self.param_frame.pack(pady=10)

        self.campos = {}  # Para guardar los campos de entrada

        # Botón calcular
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.pack(pady=10)

        # Resultados
        self.resultado_text = tk.Text(self, height=6, width=40, state="disabled")
        self.resultado_text.pack(pady=10)

    def mostrar_campos(self, event=None):
        # Limpiar campos anteriores
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        self.campos.clear()

        figura = self.figura_var.get()
        if figura:
            parametros = FIGURAS[figura]["parametros"]
            for param in parametros:
                lbl = tk.Label(self.param_frame, text=param + ":")
                lbl.pack()
                ent = tk.Entry(self.param_frame)
                ent.pack()
                self.campos[param] = ent

    def calcular(self):
        figura = self.figura_var.get()
        if not figura:
            messagebox.showerror("Error", "Seleccione una figura")
            return
        try:
            # Obtener valores de entrada
            valores = []
            for param in FIGURAS[figura]["parametros"]:
                val_str = self.campos[param].get()
                val = float(val_str)
                valores.append(val)

            # Crear instancia y calcular
            clase_figura = FIGURAS[figura]["clase"]
            instancia = clase_figura(*valores)
            nombre = instancia.obtener_nombre()
            area = instancia.calcular_area()
            perimetro = instancia.calcular_perimetro()

            self.resultado_text.config(state="normal")
            self.resultado_text.delete("1.0", tk.END)
            self.resultado_text.insert(tk.END, f"Figura: {nombre}\n")
            self.resultado_text.insert(tk.END, f"Área: {area:.2f}\n")
            self.resultado_text.insert(tk.END, f"Perímetro: {perimetro:.2f}\n")
            self.resultado_text.config(state="disabled")

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
