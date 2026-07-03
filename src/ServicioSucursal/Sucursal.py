from ServicioGerente.Gerente import Gerente

class Sucursal:
    def __init__(self, id_sucursal: str, nombre: str, municipio: str, 
                 direccion: str, telefono: str, id_gerente: str, 
                 primer_nombre: str, segundo_nombre: str, 
                 primer_apellido: str, segundo_apellido: str, 
                 dui: str, celular: str):
        self.id = id_sucursal
        self.nombre = nombre
        self.municipio = municipio
        self.direccion = direccion 
        self.telefono = telefono
        self.gerente = Gerente(id_gerente, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, dui, celular)

    def __str__(self):
        return f"Sucursal: {self.nombre}, Municipio: {self.municipio} - Gerente: {self.gerente.primer_nombre}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Sucursal):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)