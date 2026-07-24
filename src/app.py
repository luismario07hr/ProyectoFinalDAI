from flask import Flask, jsonify, request
from database import (
    obtener_gerentes, obtener_gerente_por_id, insertar_gerente,
    obtener_sucursales, obtener_sucursal_por_id, insertar_sucursal,
    obtener_productos, obtener_producto_por_id, insertar_producto_completo,
    actualizar_producto, eliminar_producto,
    obtener_cuadros, obtener_cuadro_por_id, insertar_cuadro, 
    actualizar_estado_cuadro, actualizar_dinero_recibido_cuadro,
    obtener_detalles_por_cuadro, insertar_detalle_cuadro, actualizar_detalle_cuadro, 
    obtener_detalle_por_id
)

app = Flask(__name__)

# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

def contiene_negativos(datos: dict) -> bool:
    """Verifica si algún valor numérico en el diccionario es menor que cero."""
    for valor in datos.values():
        if isinstance(valor, (int, float)) and valor < 0:
            return True
    return False

@app.get("/")
def inicio():
    return jsonify({"mensaje": "API de Inventario en funcionamiento"}), 200

# ==========================================
# ENDPOINTS GERENTES Y SUCURSALES
# ==========================================

@app.get("/gerentes")
def listar_gerentes():
    return jsonify(obtener_gerentes()), 200

@app.post("/gerentes")
def crear_gerente():
    datos = request.get_json()
    if obtener_gerente_por_id(datos.get("id_gerente")):
        return jsonify({"error": "El ID de gerente ya existe"}), 409
    return jsonify(insertar_gerente(datos)), 201

@app.get("/sucursales")
def listar_sucursales():
    return jsonify(obtener_sucursales()), 200

@app.post("/sucursales")
def crear_sucursal():
    datos = request.get_json()
    if not obtener_gerente_por_id(datos.get("id_gerente")):
        return jsonify({"error": "El gerente especificado no existe"}), 404
    if obtener_sucursal_por_id(datos.get("id_sucursal")):
        return jsonify({"error": "El ID de sucursal ya existe"}), 409
    return jsonify(insertar_sucursal(datos)), 201

# ==========================================
# ENDPOINTS PRODUCTOS
# ==========================================

@app.get("/productos")
def listar_productos():
    return jsonify(obtener_productos()), 200

@app.get("/productos/<string:id_producto>")
def consultar_producto(id_producto):
    producto = obtener_producto_por_id(id_producto)
    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(producto), 200

@app.post("/productos")
def insertar_producto_endpoint():
    producto = request.get_json()
    
    if contiene_negativos(producto):
        return jsonify({"error": "No se permiten valores numéricos negativos"}), 400
    
    if obtener_producto_por_id(producto.get("id_producto")):
        return jsonify({"error": "El ID de producto ya existe"}), 409

    tipo = producto.get("tipo_producto")
    if tipo not in ["PESABLE", "NO_PESABLE"]:
        return jsonify({"error": "El tipo_producto debe ser PESABLE o NO_PESABLE"}), 400
        
    if tipo == "PESABLE" and "nacionalidad" not in producto:
        return jsonify({"error": "Los productos pesables requieren el campo 'nacionalidad'"}), 400
        
    if tipo == "NO_PESABLE" and "marca" not in producto:
        return jsonify({"error": "Los productos no pesables requieren el campo 'marca'"}), 400

    resultado = insertar_producto_completo(producto)
    return jsonify(resultado), 201

@app.put("/productos/<string:id_producto>")
def actualizar_producto_endpoint(id_producto):
    producto = request.get_json()
    
    if contiene_negativos(producto):
        return jsonify({"error": "No se permiten valores numéricos negativos"}), 400
        
    # Verificar que exista antes de actualizar
    if obtener_producto_por_id(id_producto) is None:
        return jsonify({"error": "Producto no encontrado"}), 404
        
    resultado = actualizar_producto(id_producto, producto)
    return jsonify(resultado), 200

@app.delete("/productos/<string:id_producto>")
def eliminar_producto_endpoint(id_producto):
    if obtener_producto_por_id(id_producto) is None:
        return jsonify({"error": "Producto no encontrado"}), 404
        
    resultado = eliminar_producto(id_producto)
    return jsonify(resultado), 200

# ==========================================
# ENDPOINTS CUADROS
# ==========================================

@app.get("/cuadros")
def listar_cuadros():
    return jsonify(obtener_cuadros()), 200

@app.get("/cuadros/<string:id_cuadro>")
def consultar_cuadro(id_cuadro):
    cuadro = obtener_cuadro_por_id(id_cuadro)
    if cuadro is None:
        return jsonify({"error": "Cuadro no encontrado"}), 404
    return jsonify(cuadro), 200

@app.post("/cuadros")
def insertar_cuadro_endpoint():
    cuadro = request.get_json()
    
    if contiene_negativos(cuadro):
        return jsonify({"error": "No se permiten valores numéricos negativos"}), 400
        
    if not obtener_sucursal_por_id(cuadro.get("id_sucursal")):
        return jsonify({"error": "La sucursal especificada no existe"}), 404

    if obtener_cuadro_por_id(cuadro.get("id_cuadro")):
        return jsonify({"error": "El ID de cuadro ya existe"}), 409

    resultado = insertar_cuadro(cuadro)
    return jsonify(resultado), 201

@app.put("/cuadros/<string:id_cuadro>/estado")
def actualizar_estado(id_cuadro):
    datos = request.get_json()
    nuevo_estado = datos.get("estado")
    
    if nuevo_estado == "ABIERTO":
        return jsonify({"error": "No está permitido regresar un cuadro al estado ABIERTO"}), 403
        
    # Verificar existencia del cuadro
    if obtener_cuadro_por_id(id_cuadro) is None:
        return jsonify({"error": "Cuadro no encontrado"}), 404
        
    resultado = actualizar_estado_cuadro(id_cuadro, nuevo_estado)
    return jsonify(resultado), 200

@app.put("/cuadros/<string:id_cuadro>/dinero")
def actualizar_dinero(id_cuadro):
    datos = request.get_json()
    dinero = datos.get("dinero_recibido")
    
    if dinero is None:
        return jsonify({"error": "Se requiere el campo dinero_recibido"}), 400
    
    if isinstance(dinero, (int, float)) and dinero < 0:
        return jsonify({"error": "No se permiten valores numéricos negativos"}), 400
    
    cuadro_actual = obtener_cuadro_por_id(id_cuadro)
    if cuadro_actual is None:
        return jsonify({"error": "Cuadro no encontrado"}), 404
        
    if cuadro_actual.get("estado") == "CERRADO":
        return jsonify({"error": "No se puede editar el dinero de un cuadro CERRADO"}), 403
    
    resultado = actualizar_dinero_recibido_cuadro(id_cuadro, dinero)
    return jsonify(resultado), 200

# ==========================================
# ENDPOINTS DETALLES CUADRO
# ==========================================

@app.get("/cuadros/<string:id_cuadro>/detalles")
def listar_detalles_cuadro(id_cuadro):
    if obtener_cuadro_por_id(id_cuadro) is None:
        return jsonify({"error": "Cuadro no encontrado"}), 404
    return jsonify(obtener_detalles_por_cuadro(id_cuadro)), 200

@app.post("/cuadros/<string:id_cuadro>/detalles")
def insertar_detalle(id_cuadro):
    detalle = request.get_json()
    
    if contiene_negativos(detalle):
        return jsonify({"error": "No se permiten valores numéricos negativos"}), 400
        
    cuadro_actual = obtener_cuadro_por_id(id_cuadro)
    if cuadro_actual is None:
        return jsonify({"error": "Cuadro no encontrado"}), 404
        
    if cuadro_actual.get("estado") == "CERRADO":
        return jsonify({"error": "No se puede agregar detalles a un cuadro CERRADO"}), 403

    if not obtener_producto_por_id(detalle.get("id_producto")):
        return jsonify({"error": "El producto referenciado no existe"}), 404

    detalle["id_cuadro"] = id_cuadro 
    resultado = insertar_detalle_cuadro(detalle)
    return jsonify(resultado), 201

@app.put("/detalles/<uuid:id_detalle>")
def actualizar_detalle_endpoint(id_detalle):
    id_det_str = str(id_detalle)
    detalle = request.get_json()
    
    if contiene_negativos(detalle):
        return jsonify({"error": "No se permiten valores numéricos negativos"}), 400
    
    detalle_actual = obtener_detalle_por_id(id_det_str)
    if detalle_actual is None:
        return jsonify({"error": "Detalle no encontrado"}), 404
        
    if detalle_actual.get("estado") == "CERRADO":
        return jsonify({"error": "No se puede editar un detalle que ya está CERRADO"}), 403
        
    id_cuadro = detalle_actual.get("id_cuadro")
    cuadro_actual = obtener_cuadro_por_id(id_cuadro)
    
    if cuadro_actual and cuadro_actual.get("estado") == "CERRADO":
        return jsonify({"error": "No se puede editar un detalle porque su cuadro padre está CERRADO"}), 403

    resultado = actualizar_detalle_cuadro(id_det_str, detalle)
    return jsonify(resultado), 200

# ==========================================
# MANEJO DE ERRORES GLOBALES
# ==========================================

@app.errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True)