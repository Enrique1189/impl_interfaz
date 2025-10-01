import tkinter as tk
from tkinter import ttk, messagebox

# Importar clases de la carpeta figuras
from figuras.circulo import Circulo
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo
from figuras.triangulo_rectangulo import TrianguloRectangulo
from figuras.rombo import Rombo
from figuras.trapecio import Trapecio
from figuras.pentagono import Pentagono
from figuras.elipse import Elipse


# ------------------- FUNCIÓN DE CÁLCULO -------------------
def calcular():
    figura = figura_var.get()
    try:
        if figura == "Círculo":
            r = float(entry1.get())
            obj = Circulo(r)
        elif figura == "Cuadrado":
            l = float(entry1.get())
            obj = Cuadrado(l)
        elif figura == "Rectángulo":
            b = float(entry1.get())
            h = float(entry2.get())
            obj = Rectangulo(b, h)
        elif figura == "Triángulo":
            l = float(entry1.get())
            obj = Triangulo(l)
        elif figura == "Triángulo Rectángulo":
            c1 = float(entry1.get())
            c2 = float(entry2.get())
            obj = TrianguloRectangulo(c1, c2)
        elif figura == "Rombo":
            l = float(entry1.get())
            d1 = float(entry2.get())
            d2 = float(entry3.get())
            obj = Rombo(l, d1, d2)
        elif figura == "Trapecio":
            bm = float(entry1.get())
            bm2 = float(entry2.get())
            h = float(entry3.get())
            l1 = float(entry4.get())
            l2 = float(entry5.get())
            obj = Trapecio(bm, bm2, h, l1, l2)
        elif figura == "Pentágono":
            l = float(entry1.get())
            obj = Pentagono(l)
        elif figura == "Elipse":
            a = float(entry1.get())
            b = float(entry2.get())
            obj = Elipse(a, b)
        else:
            messagebox.showerror("Error", "Selecciona una figura")
            return

        # Mostrar resultados
        area = obj.calcular_area()
        perimetro = obj.calcular_perimetro()
        resultado_label.config(
            text=f"{obj.obtener_nombre()}\nÁrea: {area:.2f}\nPerímetro: {perimetro:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos")


# ------------------- FUNCIÓN PARA MOSTRAR CAMPOS -------------------
def actualizar_campos(*args):
    for w in [entry1, entry2, entry3, entry4, entry5,
              label1, label2, label3, label4, label5]:
        w.grid_remove()

    fig = figura_var.get()
    if fig == "Círculo":
        label1.config(text="Radio:")
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
    elif fig in ["Cuadrado", "Triángulo", "Pentágono"]:
        label1.config(text="Lado:")
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
    elif fig == "Rectángulo":
        label1.config(text="Base:")
        label2.config(text="Altura:")
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
        label2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)
    elif fig == "Triángulo Rectángulo":
        label1.config(text="Cateto 1:")
        label2.config(text="Cateto 2:")
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
        label2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)
    elif fig == "Rombo":
        label1.config(text="Lado:")
        label2.config(text="Diagonal Mayor:")
        label3.config(text="Diagonal Menor:")
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
        label2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)
        label3.grid(row=3, column=0)
        entry3.grid(row=3, column=1)
    elif fig == "Trapecio":
        label1.config(text="Base Mayor:")
        label2.config(text="Base Menor:")
        label3.config(text="Altura:")
        label4.config(text="Lado 1:")
        label5.config(text="Lado 2:")
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
        label2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)
        label3.grid(row=3, column=0)
        entry3.grid(row=3, column=1)
        label4.grid(row=4, column=0)
        entry4.grid(row=4, column=1)
        label5.grid(row=5, column=0)
        entry5.grid(row=5, column=1)
    elif fig == "Elipse":
        label1.config(text="Semieje a:")
        label2.config(text="Semieje b:")
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
        label2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)


# ------------------- INTERFAZ PRINCIPAL -------------------
root = tk.Tk()
root.title("Calculadora de Figuras")

# Menú desplegable
figura_var = tk.StringVar()
figura_var.trace("w", actualizar_campos)

ttk.Label(root, text="Selecciona la figura:").grid(row=0, column=0)
figura_menu = ttk.Combobox(root, textvariable=figura_var, state="readonly")
figura_menu["values"] = [
    "Círculo",
    "Cuadrado",
    "Rectángulo",
    "Triángulo",
    "Triángulo Rectángulo",
    "Rombo",
    "Trapecio",
    "Pentágono",
    "Elipse",
]
figura_menu.grid(row=0, column=1)

# Entradas y etiquetas
label1 = ttk.Label(root, text="")
label2 = ttk.Label(root, text="")
label3 = ttk.Label(root, text="")
label4 = ttk.Label(root, text="")
label5 = ttk.Label(root, text="")

entry1 = ttk.Entry(root)
entry2 = ttk.Entry(root)
entry3 = ttk.Entry(root)
entry4 = ttk.Entry(root)
entry5 = ttk.Entry(root)

# Botón calcular
calc_btn = ttk.Button(root, text="Calcular", command=calcular)
calc_btn.grid(row=6, column=0, columnspan=2, pady=10)

# Resultado
resultado_label = ttk.Label(root, text="", font=("Arial", 12))
resultado_label.grid(row=7, column=0, columnspan=2)

# Iniciar ventana
root.mainloop()
