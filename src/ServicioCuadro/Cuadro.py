from datetime import date
from src.ServicioCuadro.DetalleCuadro import DetalleCuadro 
from src.ServicioSucursal.Sucursal import Sucursal  # Importamos Sucursal para el tipado

class Cuadro:
    def __init__(self, id_cuadro: str, sucursal: Sucursal, fecha: date):
        # Atributos exactos del UML
        self.id_cuadro: str = id_cuadro
        self.sucursal: Sucursal = sucursal  
        self.detalles_producto_del_dia: list[DetalleCuadro] = []  
        self.fecha: date = fecha
        self.dinero_recibido: float = 0.0
        self.estado: str = "ABIERTO"
