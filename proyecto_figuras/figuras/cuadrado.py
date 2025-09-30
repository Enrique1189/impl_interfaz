import tkinter as tk
from tkinter import messagebox

class Cuadrado:
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def calcular_area(self) -> float:
        return self.lado ** 2

def calcular():
    try:
        l = float(entry_lado.get())
        c = Cuadrado(l)
        resultado.set(f"Área: {c.calcular_area():.2f} | Perímetro: {c.calcular_perimetro():.2f}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Cuadrado")

tk.Label(ventana, text="Lado:").pack()
entry_lado = tk.Entry(ventana)
entry_lado.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack()

ventana.mainloop()
