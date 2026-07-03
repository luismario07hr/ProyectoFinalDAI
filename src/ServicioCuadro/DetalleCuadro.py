from ServicioProductos.Producto import Producto 
from datetime import date

class DetalleCuadro():
    def __init__(self, producto: Producto, fecha: date):
        self.producto = producto
        self._fecha = fecha
        self._cantidad_inicial = 0.0
        self._cantidad_entrada = 0.0
        self._cantidad_salida = 0.0
        self._cantidad_vendida = 0.0
        self._cantidad_merma = 0.0
        self._cantidad_final_registrada = 0.0
        self._cantidad_devuelta = 0.0
        self._estado = "ABIERTO"

    def comprobar_cuadro_esta_abierto(self) -> bool:
        return self._estado == "ABIERTO"

    def verificar_no_sea_numero_negativo(self, numero) -> bool:
        return numero >= 0

    def _validar_movimiento(self, cantidad) -> None:
        if not self.producto.verificar_tipo_dato_correcto(cantidad):
            raise TypeError(f"ERROR: tipo de dato invalido para {self.producto.producto_categoria()}")
        if not self.verificar_no_sea_numero_negativo(cantidad):
            raise ValueError("ERROR: no se puede ingresar numeros negativos")
        if not self.comprobar_cuadro_esta_abierto():
            raise RuntimeError("ERROR: El cuadro ya no admite modificaciones")

    def asignar_cantidad_inicial(self, cantidad_inicial) -> None:
        self._validar_movimiento(cantidad_inicial)
        self._cantidad_inicial = cantidad_inicial

    def registrar_entrada_producto(self, cantidad) -> None:
        self._validar_movimiento(cantidad)
        self._cantidad_entrada += cantidad

    def registrar_salida_producto(self, cantidad) -> None:
        self._validar_movimiento(cantidad)
        self._cantidad_salida += cantidad

    def actualizar_cantidad_merma(self, merma) -> None:
        self._validar_movimiento(merma)
        self._cantidad_merma += merma

    def agregar_nueva_venta(self, cantidad_vendida) -> None:
        self._validar_movimiento(cantidad_vendida)
        self._cantidad_vendida += cantidad_vendida

    def registrar_devolucion_producto(self, cantidad_devuelta) -> None:
        self._validar_movimiento(cantidad_devuelta)
        self._cantidad_devuelta += cantidad_devuelta

    def reportar_cantidad_final_registrada(self, cantidad_final) -> None:
        self._validar_movimiento(cantidad_final)
        self._cantidad_final_registrada = cantidad_final

    def calcular_total_vendido(self) -> float:
        if self.comprobar_cuadro_esta_abierto():
            raise RuntimeError("ERROR: El cuadro debe estar cerrado para calcular el total vendido")
        return self._cantidad_vendida * self.producto.producto_precio

    def calcular_cantidad_final_esperada(self):
        return (self._cantidad_inicial
                + self._cantidad_entrada
                + self._cantidad_devuelta
                - self._cantidad_salida
                - self._cantidad_vendida
                - self._cantidad_merma)

    def comprobar_diferencia_inventario(self) -> str:
        if self.comprobar_cuadro_esta_abierto():
            raise RuntimeError("ERROR: El cuadro debe estar cerrado para comprobar el inventario")

        esperada = self.calcular_cantidad_final_esperada()
        diferencia = self._cantidad_final_registrada - esperada

        if diferencia == 0:
            return "El inventario cuadra perfectamente."
        elif diferencia > 0:
            return f"Sobrante de inventario: {diferencia:.2f}"
        else:
            return f"Faltante de inventario: {abs(diferencia):.2f}"
        
    def generar_reporte_movimientos(self) -> dict:
        return {
            "producto": self.producto.producto_nombre,
            "categoria": self.producto.producto_categoria(),
            "fecha": self._fecha,
            "estado": self._estado,
            "cantidad_inicial": self._cantidad_inicial,
            "entradas": self._cantidad_entrada,
            "salidas": self._cantidad_salida,
            "vendido": self._cantidad_vendida,
            "merma": self._cantidad_merma,
            "devoluciones": self._cantidad_devuelta,
            "cantidad_final_registrada": self._cantidad_final_registrada,
            "cantidad_final_esperada": self.calcular_cantidad_final_esperada(),
        } 

    def cerrar_detalle_cuadro(self) -> None:
        if not self.comprobar_cuadro_esta_abierto():
            raise RuntimeError("ERROR: El cuadro ya se encuentra cerrado")
        self._estado = "CERRADO"