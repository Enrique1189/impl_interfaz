from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        pass

    @abstractmethod
    def calcular_perimetro(self) -> float:
        pass

    @abstractmethod
    def obtener_nombre(self) -> str:
        pass
