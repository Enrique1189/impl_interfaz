#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder
import tkinter as tk
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo
from figuras.rombo import Rombo
from figuras.pentagono import Pentagono
from figuras.hexagono import Hexagono
from figuras.heptagono import Heptagono
from figuras.octagono import Octagono
from figuras.circulo import Circulo  # Asegúrate de tenerlo

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

        tk.Label(self.ventana, text="Selecciona la figura:", font=font_texto).pack(pady=5)
        self.figura_seleccionada = tk.StringVar()
        self.figura_seleccionada.set(list(self.FIGURAS.keys())[0])
        tk.OptionMenu(self.ventana, self.figura_seleccionada, *self.FIGURAS.keys(), command=self.actualizar_entradas).pack(pady=5)

        self.labels = []
        self.entries = []
        for _ in range(2):
            label = tk.Label(self.ventana, font=font_texto)
            label.pack(pady=5)
            entry = tk.Entry(self.ventana, font=font_texto, width=20)
            entry.pack(pady=5)
            self.labels.append(label)
            self.entries.append(entry)

        tk.Button(self.ventana, text="Calcular", font=font_texto, bg="lightblue", command=self.calcular).pack(pady=15)

        self.resultado = tk.StringVar()
        tk.Label(self.ventana, textvariable=self.resultado, font=font_resultado, fg="green").pack(pady=15)

        self.actualizar_entradas(self.figura_seleccionada.get())
        self.ventana.mainloop()

    def actualizar_entradas(self, figura):
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
            self.labels[0].config(text="Diagonal mayor:")
            self.labels[1].config(text="Diagonal menor:")
            for i in range(2):
                self.labels[i].pack(pady=5)
                self.entries[i].pack(pady=5)
        else:
            self.labels[0].config(text="Lado:")
            self.labels[1].config(text="Apotema:")
            for i in range(2):
                self.labels[i].pack(pady=5)
                self.entries[i].pack(pady=5)

    def calcular(self):
        figura_nombre = self.figura_seleccionada.get()
        try:
            v1 = float(self.entries[0].get())
            v2 = float(self.entries[1].get()) if self.entries[1].winfo_ismapped() else 0
            figura = self.FIGURAS[figura_nombre](v1, v2)
            area = figura.area()
            perimetro = figura.perimetro()
            self.resultado.set(f"Área: {area:.2f} | Perímetro: {perimetro:.2f}")
        except Exception as e:
            self.resultado.set(f"Error: {str(e)}")

if __name__ == "__main__":
    Pantalla()

