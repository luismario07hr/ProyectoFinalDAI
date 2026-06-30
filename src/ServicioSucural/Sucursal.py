class Sucursal:
    def __init__(self, id_sucursal: str, nombre: str, municipio: str, 
                 direccion: str, gerente: Gerente, telefono: str):
        self.id = id_sucursal
        self.nombre = nombre
        self.municipio = municipio
        self.direccion = direccion
        # Relación de composición con la clase Gerente
        self.gerente = gerente 
        self.telefono = telefono

    def __str__(self):
        return f"Sucursal: {self.nombre}, Municipio: {self.municipio} - Gerente: {self.gerente.primer_nombre}"