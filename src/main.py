"""
Mini aplicacion interactiva de consola para probar Cuadro y DetalleCuadro.
No usa funciones: todo el flujo esta escrito directamente como script.
"""

from datetime import date

from ServicioProductos.Producto import ProductoPesable, ProductoNoPesable
from ServicioGerente.Gerente import Gerente
from ServicioSucursal.Sucursal import Sucursal
from ServicioCuadro.DetalleCuadro import DetalleCuadro
from ServicioCuadro.Cuadro import Cuadro


# --- Datos de apoyo, creados de antemano ---
sucursal = Sucursal(
    id_sucursal="SUC001",
    nombre="Sucursal Centro",
    municipio="San Salvador",
    direccion="Av. Siempre Viva 123",
    telefono="2222-3333",
    id_gerente="GER001",
    primer_nombre="Carlos",
    segundo_nombre="Andres",
    primer_apellido="Ramirez",
    segundo_apellido="Lopez",
    dui="01234567-8",
    celular="7777-8888",
)
print("Objeto creado -> Sucursal:", sucursal)
print("Objeto creado -> Gerente:", sucursal.gerente)

chicharron = ProductoPesable("P001", "Chicharron", 1.50, "Guatemala")
gaseosa = ProductoNoPesable("P002", "Gaseosa 600ml", 0.75, "CocaCola")
print("Objeto creado -> Producto:", chicharron)
print("Objeto creado -> Producto:", gaseosa)

hoy = date.today()
cuadro = Cuadro(id_cuadro="CUA001", sucursal=sucursal, fecha=hoy)
print(f"Objeto creado -> Cuadro: id={cuadro.id_cuadro}, fecha={cuadro.fecha}")

detalle_chicharron = DetalleCuadro(producto=chicharron, fecha=hoy)
detalle_gaseosa = DetalleCuadro(producto=gaseosa, fecha=hoy)
print("Objeto creado -> DetalleCuadro para Chicharron")
print("Objeto creado -> DetalleCuadro para Gaseosa 600ml")

cuadro.agregar_detalle_producto(detalle_chicharron)
cuadro.agregar_detalle_producto(detalle_gaseosa)
print("Ambos DetalleCuadro fueron agregados al Cuadro.\n")


while True:
    print("""
========= MENU CUADRO =========
1. Registrar entrada       -> suma cantidad al inventario de un producto
2. Registrar venta         -> registra una venta y resta del inventario esperado
3. Registrar merma         -> registra perdida/dano de producto
4. Reportar cantidad final -> ingresa el conteo fisico real (peso/conteo)
5. Cerrar cuadro           -> congela el dia, ya no se pueden hacer mas cambios
6. Ver reporte del cuadro  -> muestra un diccionario con todos los movimientos
0. Salir                   -> termina el programa
================================
""")

    opcion = input("Elige una opcion: ").strip()

    match opcion:
        case "1":
            print("\nProductos disponibles:")
            for i, detalle in enumerate(cuadro.detalles_producto_del_dia, start=1):
                print(f"{i}. {detalle.producto.producto_nombre}")
            try:
                indice = int(input("Elige el numero del producto: ")) - 1
                detalle = cuadro.detalles_producto_del_dia[indice]
                cantidad = float(input("Cantidad de entrada: "))
                detalle.registrar_entrada_producto(cantidad)
                print(f"Entrada registrada: +{cantidad} para {detalle.producto.producto_nombre}")
            except (TypeError, ValueError, RuntimeError, IndexError) as e:
                print("Error:", e)

        case "2":
            print("\nProductos disponibles:")
            for i, detalle in enumerate(cuadro.detalles_producto_del_dia, start=1):
                print(f"{i}. {detalle.producto.producto_nombre}")
            try:
                indice = int(input("Elige el numero del producto: ")) - 1
                detalle = cuadro.detalles_producto_del_dia[indice]
                cantidad = float(input("Cantidad vendida: "))
                detalle.agregar_nueva_venta(cantidad)
                print(f"Venta registrada: {cantidad} de {detalle.producto.producto_nombre}")
            except (TypeError, ValueError, RuntimeError, IndexError) as e:
                print("Error:", e)

        case "3":
            print("\nProductos disponibles:")
            for i, detalle in enumerate(cuadro.detalles_producto_del_dia, start=1):
                print(f"{i}. {detalle.producto.producto_nombre}")
            try:
                indice = int(input("Elige el numero del producto: ")) - 1
                detalle = cuadro.detalles_producto_del_dia[indice]
                cantidad = float(input("Cantidad de merma: "))
                detalle.actualizar_cantidad_merma(cantidad)
                print(f"Merma registrada: {cantidad} de {detalle.producto.producto_nombre}")
            except (TypeError, ValueError, RuntimeError, IndexError) as e:
                print("Error:", e)

        case "4":
            print("\nProductos disponibles:")
            for i, detalle in enumerate(cuadro.detalles_producto_del_dia, start=1):
                print(f"{i}. {detalle.producto.producto_nombre}")
            try:
                indice = int(input("Elige el numero del producto: ")) - 1
                detalle = cuadro.detalles_producto_del_dia[indice]
                cantidad = float(input("Cantidad final contada: "))
                detalle.reportar_cantidad_final_registrada(cantidad)
                print(f"Cantidad final registrada para {detalle.producto.producto_nombre}: {cantidad}")
            except (TypeError, ValueError, RuntimeError, IndexError) as e:
                print("Error:", e)

        case "5":
            try:
                cuadro.cerrar_cuadro()
            except RuntimeError as e:
                print("Error:", e)

        case "6":
            print(cuadro.generar_reporte_cuadro())

        case "0":
            print("Saliendo...")
            break

        case _:
            print("Opcion invalida.")