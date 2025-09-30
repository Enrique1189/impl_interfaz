import tkinter as tk
from tkinter import messagebox

class Rectangulo:
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("Valores inválidos.")
        self.base = base
        self.altura = altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def calcular_area(self) -> float:
        return self.base * self.altura

def calcular():
    try:
        b = float(entry_base.get())
        h = float(entry_altura.get())
        r = Rectangulo(b, h)
        resultado.set(f"Área: {r.calcular_area():.2f} | Perímetro: {r.calcular_perimetro():.2f}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Rectángulo")

tk.Label(ventana, text="Base:").pack()
entry_base = tk.Entry(ventana)
entry_base.pack()

tk.Label(ventana, text="Altura:").pack()
entry_altura = tk.Entry(ventana)
entry_altura.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack()

ventana.mainloop()
