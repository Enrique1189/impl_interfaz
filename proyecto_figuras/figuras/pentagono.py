import tkinter as tk

class Pentagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def calcular_perimetro(self):
        return 5 * self.lado

    def calcular_area(self):
        return (self.calcular_perimetro() * self.apotema) / 2

ventana = tk.Tk()
ventana.title("Calculadora de Figuras Geométricas")
ventana.geometry("650x400")
ventana.config(bg="#f0f0f0")

titulo = tk.Label(ventana, text="Pentagono", font=("Arial",20,"bold"), bg="#f0f0f0")
titulo.pack(pady=15)

entrada_frame = tk.Frame(ventana, bg="#f0f0f0")
entrada_frame.pack(pady=10)

entradas = {}
campos = ["lado","apotema"]
for c in campos:
    tk.Label(entrada_frame, text=c + ":", font=("Arial",12), bg="#f0f0f0").pack()
    entradas[c] = tk.Entry(entrada_frame, font=("Arial",12))
    entradas[c].pack(pady=3)

resultado_label = tk.Label(ventana, text="", font=("Arial",16), fg="#3333ff", bg="#f0f0f0")
resultado_label.pack(pady=15)

def calcular():
    try:
        valores = {c: float(entradas[c].get()) for c in entradas}
        figura = Pentagono(**valores)
        resultado_label.config(text=f"Área: {figura.calcular_area():.2f}  Perímetro: {figura.calcular_perimetro():.2f}")
    except ValueError:
        resultado_label.config(text="Por favor ingrese todos los valores correctamente")

btn_calcular = tk.Button(ventana, text="Calcular Área y Perímetro", command=calcular, font=("Arial",14,"bold"), bg="#66ff66", width=25, height=2)
btn_calcular.pack(pady=8)

ventana.mainloop()
