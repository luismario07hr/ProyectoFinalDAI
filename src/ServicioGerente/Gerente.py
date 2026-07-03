class Gerente:
    def __init__(self, id: str, primer_nombre: str, segundo_nombre: str, 
                 primer_apellido: str, segundo_apellido: str, 
                 dui: str, celular: str):
        self.id = id
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.dui = dui
        self.celular = celular

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} (DUI: {self.dui})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Gerente):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)