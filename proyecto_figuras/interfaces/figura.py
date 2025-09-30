# interfaces/figura.py
from abc import ABC, abstractmethod

class Figura(ABC):
    """
    Clase base abstracta para todas las figuras geométricas.
    Define los métodos abstractos para calcular el perímetro y el área.
    """

    @abstractmethod
    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro de la figura.
        Debe ser implementado por las subclases.
        """
        pass

    @abstractmethod
    def calcular_area(self) -> float:
        """
        Calcula el área de la figura.
        Debe ser implementado por las subclases.
        """
        pass

    @abstractmethod
    def obtener_nombre(self) -> str:
        """
        Devuelve el nombre de la figura.
        """
        pass