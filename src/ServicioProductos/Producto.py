from abc import ABC, abstractmethod # Para crear clases abstractas xd

class Producto(ABC): # Es la clase para cualquier producto
    
    def __init__(self, id_producto: str, producto_nombre: str, producto_precio: float):
        self.id_producto = id_producto
        self.producto_nombre = producto_nombre
        self.producto_precio = producto_precio
        
    def producto_categoria(self) -> str: # Devuelve la categoria del producto
        return type(self).__name__
    
    @abstractmethod
    def verificar_tipo_dato_correcto(self, dato) -> bool: # Verifica que el tipo de dato sea el correcto
        raise NotImplementedError
    
    def __str__(self) -> str: 
        return f"{self.producto_categoria()}: {self.producto_nombre} (ID: {self.id_producto}) - ${self.producto_precio}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Producto):
            return NotImplemented
        return self.id_producto == other.id_producto
    
    def __hash__(self) -> int: 
        return hash(self.id_producto)
    
class ProductoPesable(Producto): # Son los productos que se venden por peso, como las frutas, verduras, carnes y tal
    
    def __init__(self, id_producto: str, producto_nombre: str, producto_precio: float, producto_nacionalidad: str):
        super().__init__(id_producto, producto_nombre, producto_precio)
        self._nacionalidad = producto_nacionalidad
        
    def producto_nacionalidad(self) -> str: # Lo que hace que basicamente se devuelva la nacionalidad o origen del producto
        return self._nacionalidad
    
    def verificar_tipo_dato_correcto(self, dato) -> bool: # Valida una cantidad para un producto pesable, el peso admite decimales
        return isinstance(dato, (int, float)) and not isinstance(dato, bool)
    
class ProductoNoPesable(Producto): # Son todos los productos que se venden por unidades como las bebidas, enlatados, etc
    
    def __init__(self, id_producto: str, producto_nombre: str, producto_precio: float, producto_marca: str):
        super().__init__(id_producto, producto_nombre, producto_precio)
        self._marca = producto_marca
        
    def producto_marca(self) -> str: # Esto hace que se devuelva la marca del produto
        return self._marca
    
    def verificar_tipo_dato_correcto(self, dato) -> bool: # Los productos no pesables se venden por unidad, solo enteros
        return isinstance(dato, int) and not isinstance(dato, bool)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# 67