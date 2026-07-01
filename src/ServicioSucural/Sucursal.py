from ServicioGerente.Gerente import Gerente

class Sucursal:
    def __init__(self, id_sucursal: str, nombre: str, municipio: str, 
                 direccion: str, telefono: str, primer_nombre: str, segundo_nombre: str, 
                 primer_apellido: str, segundo_apellido: str, 
                 dui: str, celular: str):
        self.id = id_sucursal
        self.nombre = nombre
        self.municipio = municipio
        self.direccion = direccion 
        self.telefono = telefono
        self.gerente = Gerente(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, dui, celular)

    def __str__(self):
        return f"Sucursal: {self.nombre}, Municipio: {self.municipio} - Gerente: {self.gerente.primer_nombre}"