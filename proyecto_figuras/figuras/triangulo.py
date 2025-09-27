import tkinter as tk

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
ventana = tk.Tk()
ventana.title("Calculadora de Triángulo")
ventana.geometry("400x400")
ventana.config(bg="#f0f0f0")

titulo = tk.Label(ventana, text="Triángulo", font=("Arial", 20, "bold"), bg="#f0f0f0")
titulo.pack(pady=15)

entrada_frame = tk.Frame(ventana, bg="#f0f0f0")
entrada_frame.pack(pady=10)

entradas = {}

for campo in ["lado1", "lado2", "lado3", "base", "altura"]:
    tk.Label(entrada_frame, text=f"{campo}:", font=("Arial", 12), bg="#f0f0f0").pack()
    entradas[campo] = tk.Entry(entrada_frame, font=("Arial", 12))
    entradas[campo].pack(pady=3)

resultado_label = tk.Label(ventana, text="", font=("Arial", 16), fg="#3333ff", bg="#f0f0f0")
resultado_label.pack(pady=15)

def calcular():
    try:
        valores = {c: float(entradas[c].get()) for c in entradas}
        triangulo = Triangulo(**valores)
        area = triangulo.calcular_area()
        perimetro = triangulo.calcular_perimetro()
        resultado_label.config(text=f"Área: {area:.2f}  Perímetro: {perimetro:.2f}")
    except ValueError:
        resultado_label.config(text="Por favor ingresa todos los valores correctamente.")

btn_calcular = tk.Button(ventana, text="Calcular Área y Perímetro", command=calcular, 
                         font=("Arial", 14, "bold"), bg="#66ff66", width=25, height=2)
btn_calcular.pack(pady=8)

ventana.mainloop()
