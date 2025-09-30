import tkinter as tk
from tkinter import messagebox

class Pentagono:
    def __init__(self, lado: float, apotema: float):
        if min(lado, apotema) <= 0:
            raise ValueError("Los valores deben ser positivos.")
        self.lado = lado
        self.apotema = apotema

    def calcular_perimetro(self) -> float:
        return 5 * self.lado

    def calcular_area(self) -> float:
        return (self.calcular_perimetro() * self.apotema) / 2

def calcular():
    try:
        l = float(entry_lado.get())
        a = float(entry_apotema.get())
        p = Pentagono(l, a)
        resultado.set(f"Área: {p.calcular_area():.2f} | Perímetro: {p.calcular_perimetro():.2f}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Pentágono")

tk.Label(ventana, text="Lado:").pack()
entry_lado = tk.Entry(ventana)
entry_lado.pack()

tk.Label(ventana, text="Apotema:").pack()
entry_apotema = tk.Entry(ventana)
entry_apotema.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack()

ventana.mainloop()
