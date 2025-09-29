import tkinter as tk
from tkinter import ttk, messagebox
import math

# =========================
# CLASES DE FIGURAS
# =========================
class Figura:
    def area(self): raise NotImplementedError
    def perimetro(self): raise NotImplementedError

class Cuadrado(Figura):
    def __init__(self, lado): self.lado = lado
    def area(self): return self.lado ** 2
    def perimetro(self): return 4 * self.lado

class Rectangulo(Figura):
    def __init__(self, base, altura): self.base, self.altura = base, altura
    def area(self): return self.base * self.altura
    def perimetro(self): return 2 * (self.base + self.altura)

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base, self.altura = base, altura
        self.lado1, self.lado2, self.lado3 = lado1, lado2, lado3
    def area(self): return (self.base * self.altura) / 2
    def perimetro(self): return self.lado1 + self.lado2 + self.lado3

class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor, self.base_menor, self.altura = base_mayor, base_menor, altura
        self.lado1, self.lado2 = lado1, lado2
    def area(self): return ((self.base_mayor + self.base_menor) * self.altura) / 2
    def perimetro(self): return self.base_mayor + self.base_menor + self.lado1 + self.lado2

class Pentagono(Figura):
    def __init__(self, lado, apotema): self.lado, self.apotema = lado, apotema
    def area(self): return (5 * self.lado * self.apotema) / 2
    def perimetro(self): return 5 * self.lado

class Hexagono(Figura):
    def __init__(self, lado, apotema): self.lado, self.apotema = lado, apotema
    def area(self): return (6 * self.lado * self.apotema) / 2
    def perimetro(self): return 6 * self.lado

class Heptagono(Figura):
    def __init__(self, lado, apotema): self.lado, self.apotema = lado, apotema
    def area(self): return (7 * self.lado * self.apotema) / 2
    def perimetro(self): return 7 * self.lado

class Octagono(Figura):
    def __init__(self, lado, apotema): self.lado, self.apotema = lado, apotema
    def area(self): return (8 * self.lado * self.apotema) / 2
    def perimetro(self): return 8 * self.lado

class Rombo(Figura):
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor, self.diagonal_menor, self.lado = diagonal_mayor, diagonal_menor, lado
    def area(self): return (self.diagonal_mayor * self.diagonal_menor) / 2
    def perimetro(self): return 4 * self.lado

class Circulo(Figura):
    def __init__(self, radio): self.radio = radio
    def area(self): return math.pi * self.radio ** 2
    def perimetro(self): return 2 * math.pi * self.radio

# =========================
# INTERFAZ
# =========================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Figuras Geométricas")

        ttk.Label(root, text="Selecciona una figura:").pack(pady=10)

        self.figuras = [
            "Cuadrado", "Rectángulo", "Triángulo", "Trapecio",
            "Pentágono", "Hexágono", "Heptágono", "Octágono", "Rombo", "Círculo"
        ]

        for fig in self.figuras:
            ttk.Button(root, text=fig, command=lambda f=fig: self.abrir_figura(f)).pack(pady=3, fill="x", padx=20)

    def abrir_figura(self, figura):
        win = tk.Toplevel(self.root)
        win.title(figura)
        ttk.Label(win, text=f"{figura} - Ingresa los datos").pack(pady=10)

        campos = []
        if figura == "Cuadrado": campos = ["lado"]
        elif figura == "Rectángulo": campos = ["base", "altura"]
        elif figura == "Triángulo": campos = ["base", "altura", "lado1", "lado2", "lado3"]
        elif figura == "Trapecio": campos = ["base_mayor", "base_menor", "altura", "lado1", "lado2"]
        elif figura in ["Pentágono","Hexágono","Heptágono","Octágono"]: campos = ["lado", "apotema"]
        elif figura == "Rombo": campos = ["diagonal_mayor","diagonal_menor","lado"]
        elif figura == "Círculo": campos = ["radio"]

        entradas = {}
        for c in campos:
            frame = ttk.Frame(win); frame.pack(pady=2, padx=10, fill="x")
            ttk.Label(frame, text=c).pack(side="left")
            e = ttk.Entry(frame); e.pack(side="right", fill="x", expand=True)
            entradas[c] = e

        resultado = ttk.Label(win, text="", font=("Arial", 11))
        resultado.pack(pady=10)

        def calcular():
            try:
                valores = {k: float(v.get()) for k, v in entradas.items()}
                if figura == "Cuadrado": f = Cuadrado(valores["lado"])
                elif figura == "Rectángulo": f = Rectangulo(valores["base"], valores["altura"])
                elif figura == "Triángulo": f = Triangulo(valores["base"], valores["altura"], valores["lado1"], valores["lado2"], valores["lado3"])
                elif figura == "Trapecio": f = Trapecio(valores["base_mayor"], valores["base_menor"], valores["altura"], valores["lado1"], valores["lado2"])
                elif figura == "Pentágono": f = Pentagono(valores["lado"], valores["apotema"])
                elif figura == "Hexágono": f = Hexagono(valores["lado"], valores["apotema"])
                elif figura == "Heptágono": f = Heptagono(valores["lado"], valores["apotema"])
                elif figura == "Octágono": f = Octagono(valores["lado"], valores["apotema"])
                elif figura == "Rombo": f = Rombo(valores["diagonal_mayor"], valores["diagonal_menor"], valores["lado"])
                elif figura == "Círculo": f = Circulo(valores["radio"])
                else: return
                resultado.config(text=f"Área: {f.area():.2f}\nPerímetro: {f.perimetro():.2f}")
            except ValueError:
                messagebox.showerror("Error", "Debes ingresar valores numéricos")

        ttk.Button(win, text="Calcular", command=calcular).pack(pady=5)
        ttk.Button(win, text="Cerrar", command=win.destroy).pack(pady=5)

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
