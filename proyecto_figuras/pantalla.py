#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder
import tkinter as tk

# Clases de las Figuras
class Cuadrado:
    def __init__(self, lado, _=0):
        self.lado = lado
    def area(self):
        return self.lado * self.lado
    def perimetro(self):
        return 4 * self.lado

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2
    def perimetro(self):
        return self.base * 3

class Rombo:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
    def area(self):
        return (self.d1 * self.d2) / 2
    def perimetro(self):
        return 4 * (self.d1 / 2)

class Pentagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema
    def area(self):
        return (5 * self.lado * self.apotema) / 2
    def perimetro(self):
        return 5 * self.lado

class Hexagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema
    def area(self):
        return (6 * self.lado * self.apotema) / 2
    def perimetro(self):
        return 6 * self.lado

class Heptagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema
    def area(self):
        return (7 * self.lado * self.apotema) / 2
    def perimetro(self):
        return 7 * self.lado

class Octagono:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema
    def area(self):
        return (8 * self.lado * self.apotema) / 2
    def perimetro(self):
        return 8 * self.lado

class Circulo:
    def __init__(self, radio, _=0):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio * self.radio
    def perimetro(self):
        return 2 * 3.1416 * self.radio


# ==========================
# Clase de la Interfaz
# ==========================

class Pantalla:
    def __init__(self):
        self.FIGURAS = {
            "Cuadrado": Cuadrado,
            "Rectángulo": Rectangulo,
            "Triángulo": Triangulo,
            "Rombo": Rombo,
            "Pentágono": Pentagono,
            "Hexágono": Hexagono,
            "Heptágono": Heptagono,
            "Octágono": Octagono,
            "Círculo": Circulo
        }

        self.ventana = tk.Tk()
        self.ventana.title("Figuras Geométricas")
        self.ventana.geometry("500x600")

        font_titulo = ("Arial", 18, "bold")
        font_texto = ("Arial", 14)
        font_resultado = ("Arial", 16, "bold")

        tk.Label(self.ventana, text="FIGURAS GEOMÉTRICAS", font=font_titulo).pack(pady=15)

        # Selección de figura
        tk.Label(self.ventana, text="Selecciona la figura:", font=font_texto).pack(pady=5)
        self.figura_seleccionada = tk.StringVar()
        self.figura_seleccionada.set(list(self.FIGURAS.keys())[0])
        tk.OptionMenu(self.ventana, self.figura_seleccionada, *self.FIGURAS.keys(), command=self.actualizar_entradas).pack(pady=5)

        # Labels y entradas dinámicas
        self.labels = []
        self.entries = []

        for i in range(2): # máximo 2 entradas necesarias
            label = tk.Label(self.ventana, font=font_texto)
            label.pack(pady=5)
            entry = tk.Entry(self.ventana, font=font_texto, width=20)
            entry.pack(pady=5)
            self.labels.append(label)
            self.entries.append(entry)

        tk.Button(self.ventana, text="Calcular", font=font_texto, bg="lightblue",
                  command=self.calcular).pack(pady=15)

        self.resultado = tk.StringVar()
        tk.Label(self.ventana, textvariable=self.resultado, font=font_resultado, fg="green").pack(pady=15)

        self.actualizar_entradas(self.figura_seleccionada.get())
        self.ventana.mainloop()

    def actualizar_entradas(self, figura):
        """Actualiza los labels y entradas según la figura seleccionada"""
        # Ocultar por defecto
        for label, entry in zip(self.labels, self.entries):
            label.pack_forget()
            entry.pack_forget()
            entry.delete(0, tk.END)

        if figura == "Cuadrado":
            self.labels[0].config(text="Lado:")
            self.labels[0].pack(pady=5)
            self.entries[0].pack(pady=5)

        elif figura == "Círculo":
            self.labels[0].config(text="Radio:")
            self.labels[0].pack(pady=5)
            self.entries[0].pack(pady=5)

        elif figura in ["Rectángulo", "Triángulo"]:
            self.labels[0].config(text="Base:")
            self.labels[1].config(text="Altura:")
            for i in range(2):
                self.labels[i].pack(pady=5)
                self.entries[i].pack(pady=5)

        elif figura == "Rombo":
            self.labels[0].config(text="Diagonal 1:")
            self.labels[1].config(text="Diagonal 2:")
            for i in range(2):
                self.labels[i].pack(pady=5)
                self.entries[i].pack(pady=5)

        else: # Pentágono, Hexágono, Heptágono, Octágono
            self.labels[0].config(text="Lado:")
            self.labels[1].config(text="Apotema:")
            for i in range(2):
                self.labels[i].pack(pady=5)
                self.entries[i].pack(pady=5)

    def calcular(self):
        nombre = self.figura_seleccionada.get()
        v1 = float(self.entries[0].get())
        v2 = float(self.entries[1].get()) if self.entries[1].winfo_ismapped() else 0
        figura = self.FIGURAS[nombre](v1, v2)
        self.resultado.set(f"Área: {figura.area()} | Perímetro: {figura.perimetro()}")


# ==========================
# Ejecutar la app
# ==========================

if __name__ == "__main__":
    Pantalla()
	
