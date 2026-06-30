from ServicioProductos.Productos import Producto 
from datetime import date

class DetalleCuadro():
    def __init__(self, producto: Producto, fecha: date ):
        self.producto = producto
        self.fecha = fecha #En el proximo commit este debe dejar de existir
        self._cantidad_entrada = 0.0
        self._cantidad_salida = 0.0
        self._cantidad_vendida = 0.0
        self._cantidad_merma = 0.0
        self._cantidad_finao = 0.0
        self._registrar_devolucion = 0.0
        self._estado = "ABIERTO"

    def _comprobar_cuadro_esta_abierto(self) -> bool:
        return self._estado == "ABIERTO"

    def _verificar_no_sea_numero_negativo(self, numero) -> bool:
        return numero >= 0

    def _validar_movimiento(self, cantidad: float) -> None:
        if not self._verificar_no_sea_numero_negativo(cantidad):
            raise ValueError("ERROR: no se puede ingresar numeros negativos")
        if not self._comprobar_cuadro_esta_abierto():
            raise RuntimeError("ERROR: El detalle cuadro del producto ya no admite modificaciones")

    def registrar_entrada_producto(self, cantidad: float) -> None:
        self._validar_movimiento(cantidad)
        self._cantidad_entrada += cantidad

    def registrar_salida_producto(self, cantidad: float) -> None:
        self._validar_movimiento(cantidad)
        self._cantidad_salida += cantidad

    def actualizar_cantidad_merma(self, merma: float) -> None:
        self._validar_movimiento(merma)
        self._cantidad_merma += merma

    def agregar_nueva_venta(self, cantidad_vendida: float) -> None:
        self._validar_movimiento(cantidad_vendida)
        self._cantidad_vendida += cantidad_vendida

    def calcular_total_vendido(self) -> float:
        pass

    def cerrar_detalle_cuadro(self) -> None:
        self._estado = "CERRADO"