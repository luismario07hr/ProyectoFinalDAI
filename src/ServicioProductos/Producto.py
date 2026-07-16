from abc import ABC, abstractmethod 

class Producto(ABC):
    
    def __init__(self, id_producto: str, producto_nombre: str, producto_precio: float):
        self.id_producto = id_producto
        self.producto_nombre = producto_nombre
        self.producto_precio = producto_precio
        
    def producto_categoria(self) -> str: 
        return type(self).__name__
    
    @abstractmethod
    def verificar_tipo_dato_correcto(self, dato) -> bool: 
        raise NotImplementedError
    
    def __str__(self) -> str: 
        return f"{self.producto_categoria()}: {self.producto_nombre} (ID: {self.id_producto}) - ${self.producto_precio}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Producto):
            return NotImplemented
        return self.id_producto == other.id_producto
    
    def __hash__(self) -> int: 
        return hash(self.id_producto)
    
class ProductoPesable(Producto): 
    
    def __init__(self, id_producto: str, producto_nombre: str, producto_precio: float, producto_nacionalidad: str):
        super().__init__(id_producto, producto_nombre, producto_precio)
        self._nacionalidad = producto_nacionalidad
        
    def producto_nacionalidad(self) -> str: 
        return self._nacionalidad
    
    def verificar_tipo_dato_correcto(self, dato) -> bool: 
        return isinstance(dato, (int, float)) and not isinstance(dato, bool)
    
class ProductoNoPesable(Producto): 
    
    def __init__(self, id_producto: str, producto_nombre: str, producto_precio: float, producto_marca: str):
        super().__init__(id_producto, producto_nombre, producto_precio)
        self._marca = producto_marca
        
    def producto_marca(self) -> str: 
        return self._marca
    
    def verificar_tipo_dato_correcto(self, dato) -> bool: 
        if isinstance(dato, bool):
            return False
        if isinstance(dato, int):
            return True
        if isinstance(dato, float):
            return dato.is_integer()
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# 67