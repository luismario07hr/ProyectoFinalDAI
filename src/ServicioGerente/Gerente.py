class Gerente:
    def __init__(self, primer_nombre: str, segundo_nombre: str, 
                 primer_apellido: str, segundo_apellido: str, 
                 dui: str, celular: str):
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.dui = dui
        self.celular = celular

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} (DUI: {self.gerente_dui})"