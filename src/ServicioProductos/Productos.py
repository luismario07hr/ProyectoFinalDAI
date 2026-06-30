from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def verificar_tipo_dato_correcto(self, dato: float) -> bool:
        pass
    
class ProductoPesable(Producto):
    def __init__(self):
        super().__init__()
        
    def verificar_tipo_dato_correcto(self, dato: float) -> bool:
        pass   
    
class ProductoNoPesable(Producto):
    def __init__(self):
        super().__init__()
        
    def verificar_tipo_dato_correcto(self, dato: float) -> bool:
        pass   
    
