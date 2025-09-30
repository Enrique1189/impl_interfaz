from tkinter import *
from tkinter import ttk, messagebox
import math 


from figuras.circulo import Circulo
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.rombo import Rombo
from figuras.paralelogramo import Paralelogramo
from figuras.poligono import PoligonoRegular 
from figuras.elipse import Elipse
from figuras.hexagono import Hexagono # Cambié 'exagono' a 'hexagono' para consistencia

class CalculadoraFiguras(Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas")
        self.geometry("650x550")
        
        # Diccionario que mapea la figura, su Clase y sus parámetros de entrada.
        # ¡ESTO DEBE COINCIDIR EXACTAMENTE CON EL __INIT__ DE CADA CLASE!
        self.FIGURAS = {
            "Círculo": (Circulo, ["Radio"]),
            "Cuadrado": (Cuadrado, ["Lado"]),
            "Rectángulo": (Rectangulo, ["Base", "Altura"]),
            "Rombo": (Rombo, ["Diagonal Mayor", "Diagonal Menor"]),
            "Paralelogramo": (Paralelogramo, ["Base", "Altura", "Lado Adyacente"]),
            "Polígono Reg.": (PoligonoRegular, ["Número de Lados", "Longitud del Lado"]),
            "Elipse": (Elipse, ["Semieje Mayor (a)", "Semieje Menor (b)"]),
            "Hexágono": (Hexagono, ["Lado"]),
        }

        self.frames = {}
        self.current_inputs = {} 
        
        self.crear_frames_base()
        self.mostrar_frame("MenuPrincipal")

    def crear_frames_base(self):
        # Configuración de estilos
        style = ttk.Style(self)
        style.theme_use('clam')
        # Tema oscuro/moderno para Tkinter
        style.configure('TFrame', background='#252526')
        style.configure('TLabel', background='#252526', foreground='#d4d4d4', font=('Arial', 10))
        style.configure('TButton', background='#569cd6', foreground='white', font=('Arial', 10, 'bold'))
        style.map('TButton', background=[('active', '#4b8cc4')])

        container = ttk.Frame(self, style='TFrame')
        container.pack(side="top", fill="both", expand=True)

        self.frames["MenuPrincipal"] = self.create_menu_frame(container)
        
        # Crea todas las pantallas de cálculo por adelantado
        for nombre in self.FIGURAS.keys():
            self.frames[nombre] = self.create_calculo_frame(container, nombre)

        for name, frame in self.frames.items():
            frame.grid(row=0, column=0, sticky="nsew")

    def mostrar_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def create_menu_frame(self, parent):
        frame = ttk.Frame(parent, padding="20", style='TFrame')
        
        ttk.Label(frame, text="Menú Principal: Cálculo de Figuras", font=('Arial', 18, 'bold')).pack(pady=20)
        
        button_frame = ttk.Frame(frame, style='TFrame')
        button_frame.pack(pady=10)

        row, col = 0, 0
        for i, nombre in enumerate(self.FIGURAS.keys()):
            # Uso de lambda con default argument para evitar el error de late binding
            btn = ttk.Button(button_frame, text=f"{i+1}. {nombre}", width=22, 
                             command=lambda n=nombre: self.mostrar_frame(n))
            btn.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col > 2: 
                col = 0
                row += 1

        return frame

    def create_calculo_frame(self, parent, nombre_figura):
        """Crea la pantalla de cálculo específica y las variables de resultado."""
        FiguraClase, parametros = self.FIGURAS.get(nombre_figura)
        
        frame = ttk.Frame(parent, padding="30", style='TFrame')
        ttk.Label(frame, text=f"Cálculo de {nombre_figura}", font=('Arial', 16, 'bold', 'underline')).pack(pady=10)

        input_container = ttk.Frame(frame, style='TFrame')
        input_container.pack(pady=20)
        
        self.current_inputs[nombre_figura] = {} 
        
        # 1. Crear Labels y Entries para los inputs
        for i, param in enumerate(parametros):
            ttk.Label(input_container, text=f"{param}:").grid(row=i, column=0, padx=10, pady=8, sticky="w")
            var = StringVar()
            entry = ttk.Entry(input_container, textvariable=var, width=25)
            entry.grid(row=i, column=1, padx=10, pady=8)
            self.current_inputs[nombre_figura][param] = var 
        
        # 2. Área de resultados 
        ttk.Label(frame, text="--- Resultados ---", font=('Arial', 12, 'italic')).pack(pady=15)
        
        area_var = StringVar(value="--")
        perimetro_var = StringVar(value="--")
        
        # Almacenamos las variables de resultado en el diccionario de inputs
        self.current_inputs[nombre_figura]['area_var'] = area_var
        self.current_inputs[nombre_figura]['perimetro_var'] = perimetro_var
        
        ttk.Label(frame, text="Área:").pack()
        ttk.Label(frame, textvariable=area_var, font=('Arial', 14, 'bold'), foreground='#4ec9b0').pack()
        ttk.Label(frame, text="Perímetro:").pack()
        ttk.Label(frame, textvariable=perimetro_var, font=('Arial', 14, 'bold'), foreground='#4ec9b0').pack()

        # Botón para llamar a la función de cálculo
        ttk.Button(frame, text="Calcular Área y Perímetro", 
                   command=lambda f=FiguraClase, p=parametros, n=nombre_figura: self.calcular(f, p, n)).pack(pady=20)
        ttk.Button(frame, text="← Volver al Menú", command=lambda: self.mostrar_frame("MenuPrincipal")).pack()

        return frame

    def calcular(self, FiguraClase, parametros, nombre_figura):
        """Ejecuta el cálculo real llamando a la clase de la figura y actualiza el frame actual."""
        
        valores = []
        try:
            input_vars = self.current_inputs[nombre_figura]
            for param in parametros:
                # 1. Obtener el valor y validar que es un float positivo
                valor = float(input_vars[param].get()) 
                if valor <= 0:
                    # Permite al usuario saber qué campo específico tiene el error
                    raise ValueError(f"El campo '{param}' debe ser un valor numérico positivo.")
                valores.append(valor)

            # 2. Instanciar y Calcular (Llamada a las clases de figuras)
            figura_instance = FiguraClase(*valores) 
            area = figura_instance.calcular_area()
            perimetro = figura_instance.calcular_perimetro()

            # 3. Mostrar resultados con formato (2 decimales)
            input_vars['area_var'].set(f"{area:.2f} u²")
            input_vars['perimetro_var'].set(f"{perimetro:.2f} u")

        except ValueError as e:
            # Captura errores de entrada no válida (texto, vacío o números <= 0)
            messagebox.showerror("Error de Entrada", f"Error en {nombre_figura}: {str(e)}")
        except Exception as e:
            # Captura errores de implementación (si falta una fórmula en la clase, por ejemplo)
            messagebox.showerror("Error de Cálculo/Lógica", f"Ocurrió un error inesperado en {nombre_figura}: {e}")


if __name__ == "__main__":
    # Bloque que invoca la aplicación e inicia el bucle principal de Tkinter.
    app = CalculadoraFiguras()
    app.mainloop();
