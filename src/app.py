from flask import Flask, jsonify, request
from database import (
    obtener_productos, obtener_producto_por_id, insertar_producto,
    actualizar_producto, eliminar_producto,
    obtener_cuadros, obtener_cuadro_por_id, insertar_cuadro, 
    actualizar_estado_cuadro, actualizar_dinero_recibido_cuadro,
    obtener_detalles_por_cuadro, insertar_detalle_cuadro, actualizar_detalle_cuadro
)

app = Flask(__name__)

@app.get("/")
def inicio():
    return jsonify({"mensaje": "API de Inventario en funcionamiento"}), 200

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
    resultado = insertar_producto(producto)
    return jsonify(resultado), 201

@app.put("/productos/<string:id_producto>")
def actualizar_producto_endpoint(id_producto):
    producto = request.get_json()
    resultado = actualizar_producto(id_producto, producto)
    return jsonify(resultado), 200

@app.delete("/productos/<string:id_producto>")
def eliminar_producto_endpoint(id_producto):
    resultado = eliminar_producto(id_producto)
    return jsonify(resultado), 200

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
    resultado = insertar_cuadro(cuadro)
    return jsonify(resultado), 201

@app.put("/cuadros/<string:id_cuadro>/estado")
def actualizar_estado(id_cuadro):
    datos = request.get_json()
    resultado = actualizar_estado_cuadro(id_cuadro, datos.get("estado"))
    return jsonify(resultado), 200

@app.put("/cuadros/<string:id_cuadro>/dinero")
def actualizar_dinero(id_cuadro):
    datos = request.get_json()
    dinero = datos.get("dinero_recibido")
    if dinero is None:
        return jsonify({"error": "Se requiere el campo dinero_recibido"}), 400
    
    resultado = actualizar_dinero_recibido_cuadro(id_cuadro, dinero)
    return jsonify(resultado), 200

@app.get("/cuadros/<string:id_cuadro>/detalles")
def listar_detalles_cuadro(id_cuadro):
    return jsonify(obtener_detalles_por_cuadro(id_cuadro)), 200

@app.post("/cuadros/<string:id_cuadro>/detalles")
def insertar_detalle(id_cuadro):
    cuadro_actual = obtener_cuadro_por_id(id_cuadro)
    if cuadro_actual is None:
        return jsonify({"error": "Cuadro no encontrado"}), 404
        
    if cuadro_actual.get("estado") == "CERRADO":
        return jsonify({"error": "No se puede agregar detalles a un cuadro CERRADO"}), 403

    detalle = request.get_json()
    detalle["id_cuadro"] = id_cuadro 
    resultado = insertar_detalle_cuadro(detalle)
    return jsonify(resultado), 201

@app.put("/detalles/<uuid:id_detalle>")
def actualizar_detalle_endpoint(id_detalle):
    detalle = request.get_json()
    resultado = actualizar_detalle_cuadro(str(id_detalle), detalle)
    return jsonify(resultado), 200

@app.errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True)