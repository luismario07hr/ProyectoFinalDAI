from datetime import date
from src.ServicioCuadro.DetalleCuadro import DetalleCuadro 
from src.ServicioSucursal.Sucursal import Sucursal  #importamos Sucursal para validar el uso de onjetos ya creados

class Cuadro:
    def __init__(self, id_cuadro: str, sucursal: Sucursal, fecha: date):
        #atributos 
        self.id_cuadro: str = id_cuadro
        self.sucursal: Sucursal = sucursal  
        self.detalles_producto_del_dia: list[DetalleCuadro] = []  
        self.fecha: date = fecha
        self.dinero_recibido: float = 0.0
        self.estado: str = "ABIERTO"

    def calcular_valor_monetario_esperado(self) -> float:
        """Suma el total vendido de cada producto registrado en el día."""
        total_esperado = 0.0
        for detalle in self.detalles_producto_del_dia:
            total_esperado += detalle.calcular_total_vendido()
        return total_esperado
    
    def comprobar_diferencia(self) -> str:
        """Calcula la diferencia entre el dinero recibido y el valor monetario esperado."""
        esperado = self.calcular_valor_monetario_esperado()
        diferencia = self.dinero_recibido - esperado

        if diferencia == 0:
            return "La caja cuadra perfectamente."
        elif diferencia > 0:
            return f"Sobrante en caja de: ${diferencia:.2f}"
        else:
            return f"Faltante en caja de: ${abs(diferencia):.2f}"