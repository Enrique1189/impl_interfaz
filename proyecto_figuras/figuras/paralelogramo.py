import tkinter as tk
from tkinter import messagebox

class Paralelogramo:
    def __init__(self, base: float, lado: float, altura: float):
        if min(base, lado, altura) <= 0:
            raise ValueError("Los valores deben ser positivos.")
        self.base = base
        self.lado = lado
        self.altura = altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.lado)

    def calcular_area(self) -> float:
        return self.base * self.altura

def calcular():
    try:
        b = float(entry_base.get())
        l = float(entry_lado.get())
        h = float(entry_altura.get())
        p = Paralelogramo(b, l, h)
        resultado.set(f"Área: {p.calcular_area():.2f} | Perímetro: {p.calcular_perimetro():.2f}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Paralelogramo")

tk.Label(ventana, text="Base:").pack()
entry_base = tk.Entry(ventana)
entry_base.pack()

tk.Label(ventana, text="Lado:").pack()
entry_lado = tk.Entry(ventana)
entry_lado.pack()

tk.Label(ventana, text="Altura:").pack()
entry_altura = tk.Entry(ventana)
entry_altura.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack()

ventana.mainloop()
