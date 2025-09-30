import tkinter as tk
from tkinter import messagebox

class TrianguloRectangulo:
    def __init__(self, base, altura, hipotenusa):
        self.base = base
        self.altura = altura
        self.hipotenusa = hipotenusa

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.hipotenusa

def interfaz_triangulo_rectangulo():
    def calcular():
        try:
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            hipo = float(entry_hipotenusa.get())
            t = TrianguloRectangulo(base, altura, hipo)
            area = t.calcular_area()
            perimetro = t.calcular_perimetro()
            messagebox.showinfo("Resultados", f"Área: {area}\nPerímetro: {perimetro}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos.")

    ventana = tk.Tk()
    ventana.title("Triángulo Rectángulo")

    tk.Label(ventana, text="Base").pack()
    entry_base = tk.Entry(ventana)
    entry_base.pack()

    tk.Label(ventana, text="Altura").pack()
    entry_altura = tk.Entry(ventana)
    entry_altura.pack()

    tk.Label(ventana, text="Hipotenusa").pack()
    entry_hipotenusa = tk.Entry(ventana)
    entry_hipotenusa.pack()

    tk.Button(ventana, text="Calcular", command=calcular).pack()
    ventana.mainloop()

interfaz_triangulo_rectangulo()
