from datetime import date
from ServicioCuadro.DetalleCuadro import DetalleCuadro 
from ServicioSucursal.Sucursal import Sucursal  #importamos Sucursal para validar el uso de onjetos ya creados

class Cuadro:
    def __init__(self, id_cuadro: str, sucursal: Sucursal, fecha: date):
        self.id_cuadro = id_cuadro
        self.sucursal = sucursal  
        self.detalles_producto_del_dia: list[DetalleCuadro] = []  
        self.fecha = fecha
        self.dinero_recibido = 0.0
        self.estado = "ABIERTO"

    def comprobar_cuadro_esta_abierto(self) -> bool:
        return self.estado == "ABIERTO"

    def agregar_detalle_producto(self, detalle: DetalleCuadro) -> None:
        if not self.comprobar_cuadro_esta_abierto():
            raise RuntimeError("ERROR: No se pueden agregar productos, el cuadro está CERRADO")
        self.detalles_producto_del_dia.append(detalle)
        
    def generar_reporte_cuadro(self) -> dict:
        return {
            "id_cuadro": self.id_cuadro,
            "sucursal": self.sucursal.nombre,
            "fecha": self.fecha,
            "estado": self.estado,
            "dinero_recibido": self.dinero_recibido,
            "detalles_productos": [
                detalle.generar_reporte_movimientos() for detalle in self.detalles_producto_del_dia
            ],
        }    

    def cerrar_cuadro(self) -> None:
        if not self.comprobar_cuadro_esta_abierto():
            raise RuntimeError("ERROR: El cuadro ya se encuentra CERRADO")

        for detalle in self.detalles_producto_del_dia:
            if detalle.comprobar_cuadro_esta_abierto():
                detalle.cerrar_detalle_cuadro()

        self.estado = "CERRADO"
        print(f"Cuadro {self.id_cuadro} cerrado exitosamente.")

    def calcular_valor_monetario_esperado(self) -> float:
        if self.comprobar_cuadro_esta_abierto():
            raise RuntimeError("ERROR: El cuadro debe estar CERRADO para calcular el valor esperado")

        total_esperado = 0.0
        for detalle in self.detalles_producto_del_dia:
            total_esperado += detalle.calcular_total_vendido()
        return total_esperado

    def comprobar_diferencia(self) -> str:
        esperado = self.calcular_valor_monetario_esperado()
        diferencia = self.dinero_recibido - esperado

        if diferencia == 0:
            return "La caja cuadra perfectamente."
        elif diferencia > 0:
            return f"Sobrante en caja de: ${diferencia:.2f}"
        else:
            return f"Faltante en caja de: ${abs(diferencia):.2f}"