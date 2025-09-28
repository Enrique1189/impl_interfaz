#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder

import tkinter as tk
from tkinter import ttk, messagebox
import math

class Figura:
    def calcular_perimetro(self):
        pass
    def calcular_area(self):
        pass
    def obtener_nombre(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser un valor positivo.")
        self.radio = radio
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    def obtener_nombre(self):
        return "Círculo"

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        if not self._es_triangulo_valido(lado1, lado2, lado3):
            raise ValueError("Los lados no forman un triángulo válido.")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def _es_triangulo_valido(self, a, b, c):
        return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def obtener_nombre(self):
        return "Triángulo"

class Hexagono(Figura):
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_perimetro(self):
        return 6 * self.lado

    def calcular_area(self):
        apotema = self.lado * math.sqrt(3) / 2
        return (self.calcular_perimetro() * apotema) / 2

    def obtener_nombre(self):
        return "Hexágono"

class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Las dimensiones deben ser positivas.")
        if base_menor >= base_mayor:
            raise ValueError("La base menor debe ser menor que la base mayor.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def calcular_perimetro(self):
        lado = math.sqrt(((self.base_mayor - self.base_menor) / 2) ** 2 + self.altura ** 2)
        return self.base_mayor + self.base_menor + 2 * lado

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

    def obtener_nombre(self):
        return "Trapecio"

class TrianguloEquilatero(Figura):
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_area(self):
        return (math.sqrt(3) / 4) * (self.lado ** 2)

    def obtener_nombre(self):
        return "Triángulo Equilátero"

class Rombo(Figura):
    def __init__(self, lado, diagonal_mayor, diagonal_menor):
        if lado <= 0 or diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("Las dimensiones deben ser positivas.")
        self.lado = lado
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_perimetro(self):
        return 4 * self.lado

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def obtener_nombre(self):
        return "Rombo"

class Heptagono(Figura):
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_perimetro(self):
        return 7 * self.lado

    def calcular_area(self):
        apotema = self.lado / (2 * math.tan(math.pi / 7))
        return (self.calcular_perimetro() * apotema) / 2

    def obtener_nombre(self):
        return "Heptágono"

class TrapecioEscaleno(Figura):
    def __init__(self, base_mayor, base_menor, lado1, lado2, altura):
        lados = [base_mayor, base_menor, lado1, lado2]
        if any(l <= 0 for l in lados) or altura <= 0:
            raise ValueError("Las dimensiones deben ser positivas.")
        if base_menor >= base_mayor:
            raise ValueError("La base menor debe ser menor que la base mayor.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura

    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

    def obtener_nombre(self):
        return "Trapecio Escaleno"

class Cuadrado(Figura):
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_perimetro(self):
        return 4 * self.lado

    def calcular_area(self):
        return self.lado ** 2

    def obtener_nombre(self):
        return "Cuadrado"

class Pentagono(Figura):
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_perimetro(self):
        return 5 * self.lado

    def calcular_area(self):
        apotema = self.lado / (2 * math.tan(math.pi / 5))
        return (self.calcular_perimetro() * apotema) / 2

    def obtener_nombre(self):
        return "Pentágono"

FIGURAS = {
    "Círculo": Circulo,
    "Triángulo": Triangulo,
    "Hexágono": Hexagono,
    "Trapecio": Trapecio,
    "Triángulo Equilátero": TrianguloEquilatero,
    "Rombo": Rombo,
    "Heptágono": Heptagono,
    "Trapecio Escaleno": TrapecioEscaleno,
    "Cuadrado": Cuadrado,
    "Pentágono": Pentagono
}

CAMPOS_POR_FIGURA = {
    "Círculo": ["radio"],
    "Triángulo": ["lado1", "lado2", "lado3"],
    "Hexágono": ["lado"],
    "Trapecio": ["base_mayor", "base_menor", "altura"],
    "Triángulo Equilátero": ["lado"],
    "Rombo": ["lado", "diagonal_mayor", "diagonal_menor"],
    "Heptágono": ["lado"],
    "Trapecio Escaleno": ["base_mayor", "base_menor", "lado1", "lado2", "altura"],
    "Cuadrado": ["lado"],
    "Pentágono": ["lado"]
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas")
        self.geometry("450x450")
        self.resizable(False, False)

        ttk.Label(self, text="Seleccione la figura:").pack(pady=10)
        self.figura_var = tk.StringVar(value="Círculo")
        figura_menu = ttk.OptionMenu(self, self.figura_var, "Círculo", *FIGURAS.keys(), command=self.mostrar_campos)
        figura_menu.pack()

        self.campos_frame = ttk.Frame(self)
        self.campos_frame.pack(pady=10)

        self.btn_calcular = ttk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.pack(pady=10)

        self.result_area = ttk.Label(self, text="", font=("Arial", 12))
        self.result_area.pack()
        self.result_perimetro = ttk.Label(self, text="", font=("Arial", 12))
        self.result_perimetro.pack()

        self.entries = {}
        self.mostrar_campos("Círculo")

    def mostrar_campos(self, figura_nombre):
        for widget in self.campos_frame.winfo_children():
            widget.destroy()
        self.entries = {}

        campos = CAMPOS_POR_FIGURA.get(figura_nombre, [])
        for i, campo in enumerate(campos):
            label = ttk.Label(self.campos_frame, text=campo.replace('_', ' ').capitalize() + ":")
            label.grid(row=i, column=0, sticky="w", padx=5, pady=3)
            entry = ttk.Entry(self.campos_frame)
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.entries[campo] = entry

    def calcular(self):
        figura_nombre = self.figura_var.get()
        try:
            valores = {}
            for campo, entry in self.entries.items():
                valor = float(entry.get())
                if valor <= 0:
                    raise ValueError(f"El valor de '{campo}' debe ser positivo.")
                valores[campo] = valor

            clase_figura = FIGURAS[figura_nombre]

            if figura_nombre == "Triángulo":
                if not clase_figura._es_triangulo_valido(clase_figura, valores["lado1"], valores["lado2"], valores["lado3"]):
                    raise ValueError("Los lados no forman un triángulo válido.")
                figura = clase_figura(valores["lado1"], valores["lado2"], valores["lado3"])
            else:
                figura = clase_figura(**valores)

            area = figura.calcular_area()
            perimetro = figura.calcular_perimetro()

            self.result_area.config(text=f"Área: {area:.2f}")
            self.result_perimetro.config(text=f"Perímetro: {perimetro:.2f}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "Datos inválidos, por favor verifica.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
