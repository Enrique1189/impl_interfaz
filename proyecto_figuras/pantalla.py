import tkinter as tk
from tkinter import ttk, messagebox

from figuras.circulo import Circulo
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo
from figuras.rombo import Rombo
from figuras.trapecio import Trapecio
from figuras.pentagono import Pentagono
from figuras.hexagono import Hexagono
from figuras.octagono import Octagono

FIGURAS = {
    "Círculo": Circulo,
    "Cuadrado": Cuadrado,
    "Rectángulo": Rectangulo,
    "Triángulo": Triangulo,
    "Rombo": Rombo,
    "Trapecio": Trapecio,
    "Pentágono": Pentagono,
    "Hexágono": Hexagono,
    "Octágono": Octagono
}

root = tk.Tk()
root.title("Calculadora de Figuras")
root.geometry("400x400")

figura_seleccionada = tk.StringVar()
entrada1 = tk.StringVar()
entrada2 = tk.StringVar()
entrada3 = tk.StringVar()
entrada4 = tk.StringVar()

def calcular():
    try:
        nombre = figura_seleccionada.get()
        clase = FIGURAS[nombre]
        
        if nombre == "Círculo":
            f = clase(float(entrada1.get()))
        elif nombre == "Cuadrado" or nombre == "Triángulo" or nombre == "Pentágono" or nombre == "Hexágono" or nombre == "Octágono":
            f = clase(float(entrada1.get()))
        elif nombre == "Rectángulo":
            f = clase(float(entrada1.get()), float(entrada2.get()))
        elif nombre == "Rombo":
            f = clase(float(entrada1.get()), float(entrada2.get()), float(entrada3.get()))
        elif nombre == "Trapecio":
            f = clase(float(entrada1.get()), float(entrada2.get()), float(entrada3.get()), float(entrada4.get()))
        else:
            messagebox.showerror("Error", "Figura no reconocida")
            return
        
        # Mostrar resultados
        resultado.config(text=f"Área: {f.calcular_area():.2f}\nPerímetro: {f.calcular_perimetro():.2f}")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", "Datos inválidos")


ttk.Label(root, text="Selecciona la figura:").pack(pady=5)
figura_menu = ttk.Combobox(root, textvariable=figura_seleccionada, values=list(FIGURAS.keys()))
figura_menu.pack(pady=5)
figura_menu.current(0)

ttk.Label(root, text="Entrada 1:").pack()
entrada1_entry = ttk.Entry(root, textvariable=entrada1)
entrada1_entry.pack()

ttk.Label(root, text="Entrada 2:").pack()
entrada2_entry = ttk.Entry(root, textvariable=entrada2)
entrada2_entry.pack()

ttk.Label(root, text="Entrada 3:").pack()
entrada3_entry = ttk.Entry(root, textvariable=entrada3)
entrada3_entry.pack()

ttk.Label(root, text="Entrada 4:").pack()
entrada4_entry = ttk.Entry(root, textvariable=entrada4)
entrada4_entry.pack()

ttk.Button(root, text="Calcular", command=calcular).pack(pady=10)

resultado = ttk.Label(root, text="Área: \nPerímetro: ", font=("Arial", 12))
resultado.pack(pady=10)

root.mainloop()
