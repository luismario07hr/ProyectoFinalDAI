from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ==========================================
# 1. GERENTES
# ==========================================

def obtener_gerentes():
    respuesta = (
        supabase
        .table("gerentes")
        .select("*")
        .order("id_gerente")
        .execute()
    )
    return respuesta.data

def obtener_gerente_por_id(id_gerente: str):
    respuesta = (
        supabase
        .table("gerentes")
        .select("*")
        .eq("id_gerente", id_gerente)
        .execute()
    )
    if respuesta.data:
        return respuesta.data[0]
    return None

def insertar_gerente(gerente: dict):
    response = (
        supabase
        .table("gerentes")
        .insert(gerente)
        .execute()
    )
    return response.data

# ==========================================
# 2. SUCURSALES
# ==========================================

def obtener_sucursales():
    respuesta = (
        supabase
        .table("sucursales")
        .select("*, gerentes(primer_nombre, primer_apellido)")
        .order("id_sucursal")
        .execute()
    )
    return respuesta.data

def obtener_sucursal_por_id(id_sucursal: str):
    respuesta = (
        supabase
        .table("sucursales")
        .select("*, gerentes(primer_nombre, primer_apellido)")
        .eq("id_sucursal", id_sucursal)
        .execute()
    )
    if respuesta.data:
        return respuesta.data[0]
    return None

def insertar_sucursal(sucursal: dict):
    response = (
        supabase
        .table("sucursales")
        .insert(sucursal)
        .execute()
    )
    return response.data

# ==========================================
# 3. PRODUCTOS (PADRE + PESABLES / NO PESABLES)
# ==========================================

def obtener_productos():
    respuesta = (
        supabase
        .table("productos")
        .select("*, productos_pesables(nacionalidad), productos_no_pesables(marca)")
        .order("id_producto")
        .execute()
    )
    return respuesta.data

def obtener_producto_por_id(id_producto: str):
    respuesta = (
        supabase
        .table("productos")
        .select("*, productos_pesables(nacionalidad), productos_no_pesables(marca)")
        .eq("id_producto", id_producto)
        .execute()
    )
    if respuesta.data:
        return respuesta.data[0]
    return None

def insertar_producto_completo(datos: dict):
    tipo = datos.get("tipo_producto")
    
    # 1. Registro base en la tabla productos
    producto_base = {
        "id_producto": datos["id_producto"],
        "nombre": datos["nombre"],
        "precio": datos["precio"],
        "tipo_producto": tipo
    }
    supabase.table("productos").insert(producto_base).execute()
    
    # 2. Registro especializado en tabla hija
    if tipo == "PESABLE":
        detalle_pesable = {
            "id_producto": datos["id_producto"],
            "nacionalidad": datos["nacionalidad"]
        }
        supabase.table("productos_pesables").insert(detalle_pesable).execute()
        
    elif tipo == "NO_PESABLE":
        detalle_no_pesable = {
            "id_producto": datos["id_producto"],
            "marca": datos["marca"]
        }
        supabase.table("productos_no_pesables").insert(detalle_no_pesable).execute()
        
    return datos

def actualizar_producto(id_producto: str, producto: dict):
    # Separamos campos que pertenecen a tablas hijas si venían en el payload
    nacionalidad = producto.pop("nacionalidad", None)
    marca = producto.pop("marca", None)
    
    # Actualizar tabla padre productos
    if producto:
        supabase.table("productos").update(producto).eq("id_producto", id_producto).execute()
        
    # Actualizar tabla hija según corresponda
    if nacionalidad:
        supabase.table("productos_pesables").update({"nacionalidad": nacionalidad}).eq("id_producto", id_producto).execute()
        
    if marca:
        supabase.table("productos_no_pesables").update({"marca": marca}).eq("id_producto", id_producto).execute()
        
    return obtener_producto_por_id(id_producto)

def eliminar_producto(id_producto: str):
    # Por las restricciones ON DELETE CASCADE de tu SQL, borrar en 'productos' elimina en las hijas
    respuesta = (
        supabase
        .table("productos")
        .delete()
        .eq("id_producto", id_producto)
        .execute()
    )
    return respuesta.data

# ==========================================
# 4. CUADROS DE INVENTARIO
# ==========================================

def obtener_cuadros():
    respuesta = (
        supabase
        .table("cuadros")
        .select("*, sucursales(nombre, municipio)")
        .order("fecha", desc=True)
        .execute()
    )
    return respuesta.data

def obtener_cuadro_por_id(id_cuadro: str):
    respuesta = (
        supabase
        .table("cuadros")
        .select("*, sucursales(nombre, municipio)")
        .eq("id_cuadro", id_cuadro)
        .execute()
    )
    if respuesta.data:
        return respuesta.data[0]
    return None

def insertar_cuadro(cuadro: dict):
    response = (
        supabase
        .table("cuadros")
        .insert(cuadro)
        .execute()
    )
    return response.data

def actualizar_estado_cuadro(id_cuadro: str, estado: str):
    response = (
        supabase
        .table("cuadros")
        .update({"estado": estado})
        .eq("id_cuadro", id_cuadro)
        .execute()
    )
    return response.data

def actualizar_dinero_recibido_cuadro(id_cuadro: str, dinero_recibido: float):
    response = (
        supabase
        .table("cuadros")
        .update({"dinero_recibido": dinero_recibido})
        .eq("id_cuadro", id_cuadro)
        .execute()
    )
    return response.data

# ==========================================
# 5. DETALLE CUADRO (MOVIMIENTOS)
# ==========================================

def obtener_detalles_por_cuadro(id_cuadro: str):
    respuesta = (
        supabase
        .table("detalle_cuadro")
        .select("*, productos(nombre, precio, tipo_producto)")
        .eq("id_cuadro", id_cuadro)
        .execute()
    )
    return respuesta.data

def obtener_detalle_por_id(id_detalle: str):
    respuesta = (
        supabase
        .table("detalle_cuadro")
        .select("*, productos(nombre, precio, tipo_producto)")
        .eq("id_detalle", id_detalle)
        .execute()
    )
    if respuesta.data:
        return respuesta.data[0]
    return None

def insertar_detalle_cuadro(detalle: dict):
    response = (
        supabase
        .table("detalle_cuadro")
        .insert(detalle)
        .execute()
    )
    return response.data

def actualizar_detalle_cuadro(id_detalle: str, detalle: dict):
    # Protegemos las llaves foráneas para mantener integridad referencial
    campos_excluidos = {"id_detalle", "id_cuadro", "id_producto"}
    datos_actualizar = {k: v for k, v in detalle.items() if k not in campos_excluidos}

    response = (
        supabase
        .table("detalle_cuadro")
        .update(datos_actualizar)
        .eq("id_detalle", id_detalle)
        .execute()
    )
    return response.data