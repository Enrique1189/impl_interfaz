
import tkinter as tk
from tkinter import ttk, messagebox

# Importar todas las figuras
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo
from figuras.trapecio import Trapecio
from figuras.pentagono import Pentagono
from figuras.hexagono import Hexagono
from figuras.heptagono import Heptagono
from figuras.octagono import Octagono
from figuras.rombo import Rombo
from figuras.circulo import Circulo

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras Geométricas")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()