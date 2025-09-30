import tkinter as tk
from tkinter import messagebox

class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

def interfaz_triangulo():
    def calcular():
        try:
            l1 = float(entry_lado1.get())
            l2 = float(entry_lado2.get())
            l3 = float(entry_lado3.get())
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            t = Triangulo(l1, l2, l3, base, altura)
            area = t.calcular_area()
            perimetro = t.calcular_perimetro()
            messagebox.showinfo("Resultados", f"Área: {area}\nPerímetro: {perimetro}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa solo números.")

    ventana = tk.Tk()
    ventana.title("Triángulo")

    tk.Label(ventana, text="Lado 1").pack()
    entry_lado1 = tk.Entry(ventana)
    entry_lado1.pack()

    tk.Label(ventana, text="Lado 2").pack()
    entry_lado2 = tk.Entry(ventana)
    entry_lado2.pack()

    tk.Label(ventana, text="Lado 3").pack()
    entry_lado3 = tk.Entry(ventana)
    entry_lado3.pack()

    tk.Label(ventana, text="Base").pack()
    entry_base = tk.Entry(ventana)
    entry_base.pack()

    tk.Label(ventana, text="Altura").pack()
    entry_altura = tk.Entry(ventana)
    entry_altura.pack()

    tk.Button(ventana, text="Calcular", command=calcular).pack()
    ventana.mainloop()


interfaz_triangulo()
