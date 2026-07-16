from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def obtener_productos():
    respuesta = (supabase
                 .table("productos")
                 .select("*")
                 .order("id_producto")
                 .execute())
    
    return respuesta.data

def obtener_producto_por_id(id_producto: str):
    respuesta = (
        supabase
        .table("productos")
        .select("*")
        .eq("id_producto", id_producto)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None

def insertar_producto(producto: dict):
    response = (
        supabase
        .table("productos")
        .insert(producto)
        .execute()
    )
    return response.data

def actualizar_producto(id_producto: str, producto: dict):
    response = (
        supabase
        .table("productos")
        .update(producto)
        .eq("id_producto", id_producto)
        .execute()
    )
    return response.data

def eliminar_producto(id_producto: str):
    respuesta = (
        supabase
        .table("productos")
        .delete()
        .eq("id_producto", id_producto)
        .execute()
    )
    return respuesta.data

def obtener_cuadros():
    respuesta = (
        supabase
        .table("cuadros")
        .select("*")
        .order("fecha", desc=True)
        .execute()
    )
    return respuesta.data

def obtener_cuadro_por_id(id_cuadro: str):
    respuesta = (
        supabase
        .table("cuadros")
        .select("*")
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

def obtener_detalles_por_cuadro(id_cuadro: str):
    respuesta = (
        supabase
        .table("detalle_cuadro")
        .select("*")
        .eq("id_cuadro", id_cuadro)
        .execute()
    )
    return respuesta.data

def insertar_detalle_cuadro(detalle: dict):
    response = (
        supabase
        .table("detalle_cuadro")
        .insert(detalle)
        .execute()
    )
    return response.data