import SalaUrgencias
import Paciente

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Ejemplo de uso:
    sala = SalaUrgencias.SalaUrgencias()
    for _ in range(50):
        paciente = Paciente.Paciente()
        sala.ingresar_paciente(paciente)

    # Llama al método para atender a los pacientes
    sala.atender_pacientes()

# See PyCharm help at httgbfgps://www.jetbrains.com/help/pycharm/
