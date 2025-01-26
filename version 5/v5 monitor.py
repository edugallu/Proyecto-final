import os
import psutil
import time
from datetime import datetime
import matplotlib.pyplot as plt

def mostrar_estadisticas():
    uso_cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage('/')
    return uso_cpu, memoria.percent, disco.percent

def monitorizar_sistema(intervalo=2, archivo_log="metrics_log.txt"):
    print("Iniciando monitorización en tiempo real del sistema...")
    print("El archivo de log se guardará en:", os.path.abspath(archivo_log))
    
    try:
        with open(archivo_log, "w") as log:
            log.write("Fecha y Hora, Uso CPU (%), Uso Memoria (%), Uso Disco (%)\\n")
            tiempos = []
            uso_cpu_list = []
            uso_memoria_list = []
            uso_disco_list = []

            plt.ion()
            fig, axs = plt.subplots(3, 1, figsize=(10, 6))
            axs[0].set_title('Uso de CPU (%)')
            axs[1].set_title('Uso de Memoria (%)')
            axs[2].set_title('Uso de Disco (%)')
            axs[0].set_xlabel('Tiempo (segundos)')
            axs[1].set_xlabel('Tiempo (segundos)')
            axs[2].set_xlabel('Tiempo (segundos)')

            try:
                while True:
                    tiempo = len(tiempos) * intervalo
                    uso_cpu, uso_memoria, uso_disco = mostrar_estadisticas()

                    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log.write(f"{fecha_hora}, {uso_cpu:.2f}, {uso_memoria:.2f}, {uso_disco:.2f}\\n")
                    log.flush()
                    print(f"Datos escritos: {fecha_hora}, {uso_cpu:.2f}, {uso_memoria:.2f}, {uso_disco:.2f}")

                    tiempos.append(tiempo)
                    uso_cpu_list.append(uso_cpu)
                    uso_memoria_list.append(uso_memoria)
                    uso_disco_list.append(uso_disco)

                    axs[0].plot(tiempos, uso_cpu_list, color='tab:red')
                    axs[1].plot(tiempos, uso_memoria_list, color='tab:blue')
                    axs[2].plot(tiempos, uso_disco_list, color='tab:green')

                    axs[0].set_ylim(0, 100)
                    axs[1].set_ylim(0, 100)
                    axs[2].set_ylim(0, 100)

                    plt.pause(intervalo)
            except KeyboardInterrupt:
                print("\\nMonitorización detenida por el usuario.")
    except Exception as e:
        print(f"Error al abrir o escribir en el archivo log: {e}")
    finally:
        plt.ioff()
        plt.show()

if __name__ == "__main__":
    monitorizar_sistema(intervalo=2)
