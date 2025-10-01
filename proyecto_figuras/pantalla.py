import tkinter as tk
from tkinter import ttk, messagebox

# Importa tus figuras aquí
from figuras.circulo import Circulo
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo
from figuras.rombo import Rombo
from figuras.trapecio import Trapecio
from figuras.paralelogramo import Paralelogramo
from figuras.pentagono import Pentagono
from figuras.hexagono import Hexagono
from figuras.elipse import Elipse

# Diccionario con nombre de figura y los campos necesarios
FIGURAS = {
    "Círculo": ["Radio"],
    "Cuadrado": ["Lado"],
    "Rectángulo": ["Base", "Altura"],
    "Triángulo": ["Base", "Altura", "Lado 1", "Lado 2"],
    "Rombo": ["Diagonal mayor", "Diagonal menor", "Lado"],
    "Trapecio": ["Base mayor", "Base menor", "Altura", "Lado 1", "Lado 2"],
    "Paralelogramo": ["Base", "Altura", "Lado"],
    "Pentágono": ["Lado", "Apotema"],
    "Hexágono": ["Lado", "Apotema"],
    "Elipse": ["Eje mayor", "Eje menor"]
}

# Crear figura con datos introducidos
def crear_figura(nombre, valores):
    try:
        valores = [float(v) for v in valores]
        if nombre == "Círculo":
            return Circulo(*valores)
        elif nombre == "Cuadrado":
            return Cuadrado(*valores)
        elif nombre == "Rectángulo":
            return Rectangulo(*valores)
        elif nombre == "Triángulo":
            return Triangulo(*valores)
        elif nombre == "Rombo":
            return Rombo(*valores)
        elif nombre == "Trapecio":
            return Trapecio(*valores)
        elif nombre == "Paralelogramo":
            return Paralelogramo(*valores)
        elif nombre == "Pentágono":
            return Pentagono(*valores)
        elif nombre == "Hexágono":
            return Hexagono(*valores)
        elif nombre == "Elipse":
            return Elipse(*valores)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

# Actualizar campos dinámicos
def actualizar_campos(event=None):
    for widget in frame_campos.winfo_children():
        widget.destroy()
    entradas.clear()
    campos = FIGURAS[combo_figura.get()]
    for campo in campos:
        label = tk.Label(frame_campos, text=campo)
        label.pack()
        entry = tk.Entry(frame_campos)
        entry.pack()
        entradas.append(entry)

# Calcular área y perímetro
def calcular():
    figura_nombre = combo_figura.get()
    valores = [e.get() for e in entradas]
    if any(v.strip() == "" for v in valores):
        messagebox.showwarning("Advertencia", "Complete todos los campos.")
        return

    figura = crear_figura(figura_nombre, valores)
    if figura:
        resultado = f"Figura: {figura.obtener_nombre()}\nÁrea: {figura.calcular_area():.2f}\nPerímetro: {figura.calcular_perimetro():.2f}"
        label_resultado.config(text=resultado)

# Interfaz principal
app = tk.Tk()
app.title("Calculadora de Figuras")
app.geometry("400x600")

tk.Label(app, text="Seleccione una figura:").pack()
combo_figura = ttk.Combobox(app, values=list(FIGURAS.keys()))
combo_figura.pack()
combo_figura.set("Círculo")
combo_figura.bind("<<ComboboxSelected>>", actualizar_campos)

frame_campos = tk.Frame(app)
frame_campos.pack(pady=10)
entradas = []
actualizar_campos()

tk.Button(app, text="Calcular", command=calcular).pack(pady=10)

label_resultado = tk.Label(app, text="Resultado aparecerá aquí", wraplength=380, justify="left")
label_resultado.pack(pady=20)

app.mainloop()
