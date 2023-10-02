import SalaUrgencias
from Paciente import Paciente




if __name__ == '__main__':
    # Ejemplo de uso:
    sala = SalaUrgencias.SalaUrgencias()

    a = int(input("Ingrese el numero de pacientes: "))
    pacientes = []
    for _ in range(a):
        paciente = Paciente()
        pacientes.append(paciente)
    print(pacientes)

    for i in range(0, len(pacientes)):
        b = pacientes.pop()
        sala.ingresar_paciente(b)
    print(pacientes)


    # Llama al método para atender a los pacientes
    sala.atender_pacientes()
    sala.transicion_estado()

# See PyCharm help at httgbfgps://www.jetbrains.com/help/pycharm/
