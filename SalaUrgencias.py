import random
import time


class SalaUrgencias:
    def __init__(self):
        self.pacientes_a = []
        self.pacientes_b = []
        self.pacientes_c = []
        self.pacientes_d = []
        self.reloj = 0  # Inicializamos el reloj en 0

    def ingresar_paciente(self, paciente):
        if paciente.triage == "Codigo Azul":
            self.pacientes_a.append(paciente)
        elif paciente.triage == "Estabilidad Urgente":
            self.pacientes_b.append(paciente)
        elif paciente.triage == "Urgencias Normales":
            self.pacientes_c.append(paciente)
        else:
            self.pacientes_d.append(paciente)

    def atender_pacientes(self):
        estados = ['a', 'b', 'c', 'd']
        for estado in estados:
            print(f"Atendiendo pacientes en estado {estado}:")
            pacientes = self.obtener_pacientes_en_estado(estado)

            for paciente in pacientes:
                tiempo_espera = self.calcular_tiempo_espera(paciente.triage)
                print(
                    f"{paciente.nombre} en estado {estado} esperará {tiempo_espera} segundos para la atención médica.")
                time.sleep(tiempo_espera)  # Simular tiempo de espera

                # Simulamos un tratamiento médico básico en el estado actual
                self.realizar_tratamiento_medico(paciente, estado)

                # Movemos al paciente al siguiente estado si es necesario
                if estado == 'a':
                    self.pacientes_b.append(paciente)
                elif estado == 'b':
                    self.pacientes_c.append(paciente)
                elif estado == 'c':
                    self.pacientes_d.append(paciente)

                # Gestionamos la salida del paciente
                self.dar_de_alta(paciente)
        # Gestión del laboratorio
        self.gestionar_laboratorio()

    def obtener_pacientes_en_estado(self, estado):
        if estado == 'a':
            return self.pacientes_a
        elif estado == 'b':
            return self.pacientes_b
        elif estado == 'c':
            return self.pacientes_c
        else:
            return self.pacientes_d

    def calcular_tiempo_espera(self, triage):
        if triage == "Codigo Azul":
            return random.randint(1, 5)  # Pacientes críticos esperan de 1 a 5 minutos
        elif triage == "Estabilidad Urgente":
            return random.randint(10, 20)  # Pacientes estabilidad urgente esperan de 10 a 20 minutos
        elif triage == "Urgencias Normales":
            return random.randint(20, 40)  # Pacientes con urgencias normales esperan de 20 a 40 minutos
        else:
            return random.randint(40, 60)  # Pacientes con urgencias leves esperan de 40 a 60 minutos

    def realizar_tratamiento_medico(self, paciente, estado_actual):
        if estado_actual == 'a':
            tratamientos = [
                f"Realizó exámenes de sangre para {paciente.nombre}",
                f"Realizó una radiografía a {paciente.nombre}",
                f"Tomó muestras de orina de {paciente.nombre}"
            ]
        elif estado_actual == 'b':
            tratamientos = [
                f"Realizó pruebas diagnósticas a {paciente.nombre}",
                f"Realizó un ecocardiograma a {paciente.nombre}",
                f"Realizó una resonancia magnética a {paciente.nombre}"
            ]
        elif estado_actual == 'c':
            tratamientos = [
                f"Realizó procesos curativos a {paciente.nombre}",
                f"Administró medicamentos a {paciente.nombre}",
                f"Realizó una cirugía menor a {paciente.nombre}"
            ]
        else:
            tratamientos = [
                f"Realizó estabilización de dolencias y monitoreo de signos vitales en una franja de tiempo a {paciente.nombre}",
                f"Monitoreó los signos vitales de {paciente.nombre} durante una hora",
                f"Realizó pruebas de respuesta neuromuscular a {paciente.nombre}"
            ]

        tratamiento_elegido = random.choice(tratamientos)
        print(tratamiento_elegido)

    def dar_de_alta(self, paciente):
        opciones_salida = [
            "Alta",
            "Alta con medicamento",
            "Alta Voluntaria",
            "Remitido para Hospitalización",
            "Remitido a Médico Especialista",
            "Morgue"
        ]
        paciente.estado_salida = random.choice(opciones_salida)

        if paciente.estado_salida == "Alta con medicamento":
            paciente.medicamentos_pendientes.append("Medicamento XYZ")  # Ejemplo de medicamento

    def gestionar_laboratorio(self):
        medicamentos_acumulados = []
        for paciente in self.pacientes_a:
            if paciente.estado_salida == "Alta con medicamento":
                medicamentos_acumulados.extend(paciente.medicamentos_pendientes)
                paciente.medicamentos_pendientes = []

        # Si hay al menos 10 órdenes acumuladas, el farmacéutico las toma para atender a los pacientes
        if len(medicamentos_acumulados) >= 10:
            print("El farmacéutico está atendiendo las órdenes de medicamentos acumuladas.")
            # Aquí puedes agregar la lógica para procesar las órdenes del laboratorio



