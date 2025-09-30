import tkinter as tk
from tkinter import messagebox

class Rombo:
    def __init__(self, lado: float, d_mayor: float, d_menor: float):
        if min(lado, d_mayor, d_menor) <= 0:
            raise ValueError("Todos los valores deben ser positivos.")
        self.lado = lado
        self.d_mayor = d_mayor
        self.d_menor = d_menor

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def calcular_area(self) -> float:
        return (self.d_mayor * self.d_menor) / 2

def calcular():
    try:
        l = float(entry_lado.get())
        D = float(entry_dmayor.get())
        d = float(entry_dmenor.get())
        r = Rombo(l, D, d)
        resultado.set(f"Área: {r.calcular_area():.2f} | Perímetro: {r.calcular_perimetro():.2f}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Rombo")

tk.Label(ventana, text="Lado:").pack()
entry_lado = tk.Entry(ventana)
entry_lado.pack()

tk.Label(ventana, text="Diagonal mayor:").pack()
entry_dmayor = tk.Entry(ventana)
entry_dmayor.pack()

tk.Label(ventana, text="Diagonal menor:").pack()
entry_dmenor = tk.Entry(ventana)
entry_dmenor.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack()

ventana.mainloop()
