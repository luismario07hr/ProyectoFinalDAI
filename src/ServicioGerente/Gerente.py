class Gerente:
    def __init__(self, primer_nombre: str, segundo_nombre: str, 
                 primer_apellido: str, segundo_apellido: str, 
                 gerente_dui: str, gerente_celular: str):
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.gerente_dui = gerente_dui
        # Aunque el UML no especifica el tipo explícito para el celular, 
        # se asume 'str' por buenas prácticas (para incluir guiones o códigos de área).
        self.gerente_celular = gerente_celular

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} (DUI: {self.gerente_dui})"