from ServicioProductos.Productos import Producto 
from datetime import date

class DetalleCuadro():
    def __init__(self, id: str, producto: Producto, fecha: date ):
        self.id = id
        self.producto = producto
        self.fecha = fecha #En el proximo commit este debe dejar de existir
        self._cantidad_entrada = 0.0
        self._cantidad_salida = 0.0
        self._cantidad_vendida = 0.0
        self._cantidad_merma = 0.0
        self._cantidad_finao = 0.0
        self._registrar_devolucion = 0.0
        self._estado = "ABIERTO"
        
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, type(self)):
            return NotImplemented
        
        return self.id == value.id

    def __hash__(self) -> int:
        return hash(self.id)
    
    def __str__(self):
        return f"Producto: {self.producto.nombre} con fecha {self.fecha}"    

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
        
    def generar_reporte(self) -> str:
        
        nombre_prod = self.producto.nombre 
        
        reporte = (
            f"=== REPORTE DE MOVIMIENTOS ===\n"
            f"Producto: {nombre_prod}\n"
            f"Estado del Cuadro: {self._estado}\n"
            f"------------------------------\n"
            f"Entradas:       {self._cantidad_entrada:.2f}\n"
            f"Salidas:        {self._cantidad_salida:.2f}\n"
            f"Ventas:         {self._cantidad_vendida:.2f}\n"
            f"Devoluciones:   {self._registrar_devolucion:.2f}\n"
            f"Merma:          {self._cantidad_merma:.2f}\n"
            f"------------------------------\n"
            f"TOTAL FINAL:    {self._cantidad_finao:.2f}\n"
            f"=============================="
        )
        
        return reporte 