import random

class Paciente:
    def __init__(self):
        self.nombre = self.generar_nombre()
        self.edad = random.randint(18, 90)
        self.sexo = random.choice(['Masculino', 'Femenino'])
        self.triage = self.triage()
        self.estado_salida = None
        self.medicamentos_pendientes = []

    def generar_nombre(self):
        nombres = ['Juan', 'Maria', 'Luis', 'Ana', 'Pedro', 'Laura', 'Carlos', 'Sofia']
        apellidos = ['Gomez', 'Rodriguez', 'Lopez', 'Perez', 'Martinez', 'Fernandez']
        nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"
        return nombre_completo

    def triage(self):
        triage = random.randint(1, 100)
        if triage <= 10:
            return "Codigo Azul"
        elif 10 < triage <= 30:
            return "Estabilidad Urgente"
        elif 30 < triage <= 70:
            return "Urgencias Normales"
        else:
            return "Urgencias Leves"

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nTriage: {self.triage}"

    def __repr__(self) -> str:  # este método
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nTriage: {self.triage}"


