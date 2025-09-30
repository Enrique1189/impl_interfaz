import tkinter as tk
from tkinter import messagebox

class Trapecio:
    def __init__(self, base_mayor: float, base_menor: float, altura: float, lado1: float, lado2: float):
        if min(base_mayor, base_menor, altura, lado1, lado2) <= 0:
            raise ValueError("Todos los valores deben ser positivos.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_perimetro(self) -> float:
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

    def calcular_area(self) -> float:
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

def calcular():
    try:
        B = float(entry_bmayor.get())
        b = float(entry_bmenor.get())
        h = float(entry_altura.get())
        l1 = float(entry_lado1.get())
        l2 = float(entry_lado2.get())
        t = Trapecio(B, b, h, l1, l2)
        resultado.set(f"Área: {t.calcular_area():.2f} | Perímetro: {t.calcular_perimetro():.2f}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Trapecio")

tk.Label(ventana, text="Base mayor:").pack()
entry_bmayor = tk.Entry(ventana)
entry_bmayor.pack()

tk.Label(ventana, text="Base menor:").pack()
entry_bmenor = tk.Entry(ventana)
entry_bmenor.pack()

tk.Label(ventana, text="Altura:").pack()
entry_altura = tk.Entry(ventana)
entry_altura.pack()

tk.Label(ventana, text="Lado 1:").pack()
entry_lado1 = tk.Entry(ventana)
entry_lado1.pack()

tk.Label(ventana, text="Lado 2:").pack()
entry_lado2 = tk.Entry(ventana)
entry_lado2.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack()

ventana.mainloop()
