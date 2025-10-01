#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder

#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinder
import math
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_perimetro(self) -> float:
        pass

    @abstractmethod
    def calcular_area(self) -> float:
        pass

    @abstractmethod
    def obtener_nombre(self) -> str:
        pass

class Circulo(Figura):
    def __init__(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser un valor positivo.")
        self.radio = radio

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def obtener_nombre(self) -> str:
        return "Círculo"

class Cuadrado(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def obtener_nombre(self) -> str:
        return "Cuadrado"

class Hexagono(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 6 * self.lado

    def calcular_area(self) -> float:
        apotema = self.lado / (2 * math.tan(math.pi / 6))
        return 6 * self.lado * apotema / 2

    def obtener_nombre(self) -> str:
        return "Hexágono"

class Paralelogramo(Figura):
    def __init__(self, base: float, altura: float, lado: float):
        if base <= 0 or altura <= 0 or lado <= 0:
            raise ValueError("La base, altura y el lado deben ser valores positivos.")
        self.base = base
        self.altura = altura
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.lado)

    def calcular_area(self) -> float:
        return self.base * self.altura

    def obtener_nombre(self) -> str:
        return "Paralelogramo"

class Pentagono(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 5 * self.lado

    def calcular_area(self) -> float:
        apotema = self.lado / (2 * math.tan(math.pi / 5))
        return 5 * self.lado * apotema / 2

    def obtener_nombre(self) -> str:
        return "Pentágono"

class Rectangulo(Figura):
    def __init__(self, largo: float, ancho: float):
        if largo <= 0 or ancho <= 0:
            raise ValueError("El largo y el ancho deben ser valores positivos.")
        self.largo = largo
        self.ancho = ancho

    def calcular_perimetro(self) -> float:
        return 2 * (self.largo + self.ancho)

    def calcular_area(self) -> float:
        return self.largo * self.ancho

    def obtener_nombre(self) -> str:
        return "Rectángulo"

class Rombo(Figura):
    def __init__(self, diagonal_mayor: float, diagonal_menor: float):
        if diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("Las diagonales deben ser valores positivos.")
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_perimetro(self) -> float:
        lado = ((self.diagonal_mayor ** 2 + self.diagonal_menor ** 2) / 4) ** 0.5
        return 4 * lado

    def calcular_area(self) -> float:
        return 0.5 * self.diagonal_mayor * self.diagonal_menor

    def obtener_nombre(self) -> str:
        return "Rombo"

class Trapecio(Figura):
    def __init__(self, base_mayor: float, base_menor: float, altura: float):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Las bases y la altura deben ser valores positivos.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def calcular_perimetro(self) -> float:
        lado_lateral = ((self.base_mayor - self.base_menor) ** 2 + self.altura ** 2) ** 0.5
        return self.base_mayor + self.base_menor + 2 * lado_lateral

    def calcular_area(self) -> float:
        return 0.5 * (self.base_mayor + self.base_menor) * self.altura

    def obtener_nombre(self) -> str:
        return "Trapecio"

class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser valores positivos.")
        self.base = base
        self.altura = altura

    def calcular_perimetro(self) -> float:
        return 3 * self.base 

    def calcular_area(self) -> float:
        return 0.5 * self.base * self.altura

    def obtener_nombre(self) -> str:
        return "Triángulo"

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas")
        self.geometry("400x380")
        self.figuras = {
            "Círculo": Circulo,
            "Cuadrado": Cuadrado,
            "Hexágono": Hexagono,
            "Paralelogramo": Paralelogramo,
            "Pentágono": Pentagono,
            "Rectángulo": Rectangulo,
            "Rombo": Rombo,
            "Trapecio": Trapecio,
            "Triángulo": Triangulo
        }
        self.crear_widgets()

    def crear_widgets(self):
        ttk.Label(self, text="Seleccione la figura:").pack(pady=5)
        self.figura_var = tk.StringVar()
        self.figura_var.set("Seleccione figura")
        opciones = list(self.figuras.keys())

        self.optionmenu_figuras = tk.OptionMenu(self, self.figura_var, *opciones, command=self.mostrar_campos)
        self.optionmenu_figuras.pack(pady=5)

        self.campos_frame = ttk.Frame(self)
        self.campos_frame.pack(pady=10)

        self.calcular_btn = ttk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_btn.pack(pady=5)

        self.resultado_label = ttk.Label(self, text="", font=("Arial", 12))
        self.resultado_label.pack(pady=10)

        self.mensaje_label = ttk.Label(self, text="", foreground="red")
        self.mensaje_label.pack(pady=5)

    def limpiar_campos(self):
        for widget in self.campos_frame.winfo_children():
            widget.destroy()
        self.resultado_label.config(text="")
        self.mensaje_label.config(text="")

    def mostrar_campos(self, figura_seleccionada):
        self.limpiar_campos()
        figura = figura_seleccionada

        if figura not in self.figuras:
            return

        campos_por_figura = {
            "Círculo": ["Radio"],
            "Cuadrado": ["Lado"],
            "Hexágono": ["Lado"],
            "Paralelogramo": ["Base", "Altura", "Lado"],
            "Pentágono": ["Lado"],
            "Rectángulo": ["Largo", "Ancho"],
            "Rombo": ["Diagonal mayor", "Diagonal menor"],
            "Trapecio": ["Base mayor", "Base menor", "Altura"],
            "Triángulo": ["Base", "Altura"]
        }

        self.entradas = {}
        for campo in campos_por_figura[figura]:
            ttk.Label(self.campos_frame, text=campo + ":").pack()
            entrada = ttk.Entry(self.campos_frame)
            entrada.pack()
            self.entradas[campo] = entrada

    def calcular(self):
        figura = self.figura_var.get()
        if figura not in self.figuras:
            self.mensaje_label.config(text="Por favor, seleccione una figura.")
            return
        try:
            valores = {campo: float(self.entradas[campo].get()) for campo in self.entradas}

            cls = self.figuras[figura]
            if figura == "Paralelogramo":
                f = cls(valores["Base"], valores["Altura"], valores["Lado"])
            elif figura == "Rectángulo":
                f = cls(valores["Largo"], valores["Ancho"])
            elif figura == "Rombo":
                f = cls(valores["Diagonal mayor"], valores["Diagonal menor"])
            elif figura == "Trapecio":
                f = cls(valores["Base mayor"], valores["Base menor"], valores["Altura"])
            elif figura == "Triángulo":
                f = cls(valores["Base"], valores["Altura"])
            else:
                f = cls(next(iter(valores.values())))

            perimetro = f.calcular_perimetro()
            area = f.calcular_area()

            self.resultado_label.config(text=f"{figura}:\nPerímetro = {perimetro:.2f}\nÁrea = {area:.2f}")
            self.mensaje_label.config(text="") 

        except ValueError:
            self.mensaje_label.config(text=f"Error")
            self.resultado_label.config(text="")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
