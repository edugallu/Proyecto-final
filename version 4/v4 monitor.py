import psutil
import time
from datetime import datetime
import matplotlib.pyplot as plt

# Función para mostrar el uso de CPU, memoria y disco
def mostrar_estadisticas():
    # Uso de CPU
    uso_cpu = psutil.cpu_percent(interval=1)
    
    # Uso de memoria
    memoria = psutil.virtual_memory()
    
    # Uso de disco
    disco = psutil.disk_usage('/')
    
    return uso_cpu, memoria.percent, disco.percent

# Función principal para actualizar y registrar las métricas en tiempo real
def monitorizar_sistema(intervalo=2):
    print("Iniciando monitorización en tiempo real del sistema...")

    # Listas para guardar los datos
    tiempos = []
    uso_cpu_list = []
    uso_memoria_list = []
    uso_disco_list = []
    
    # Configuración de la figura para gráficos en tiempo real
    plt.ion()  # Activamos el modo interactivo de matplotlib
    fig, axs = plt.subplots(3, 1, figsize=(10, 6))
    
    # Establecemos títulos de los gráficos
    axs[0].set_title('Uso de CPU (%)')
    axs[1].set_title('Uso de Memoria (%)')
    axs[2].set_title('Uso de Disco (%)')
    
    # Etiquetas y límites de los gráficos
    axs[0].set_xlabel('Tiempo (segundos)')
    axs[0].set_ylabel('Uso de CPU (%)')
    axs[1].set_xlabel('Tiempo (segundos)')
    axs[1].set_ylabel('Uso de Memoria (%)')
    axs[2].set_xlabel('Tiempo (segundos)')
    axs[2].set_ylabel('Uso de Disco (%)')
    
    # Inicia el bucle de monitorización indefinida
    try:
        while True:
            # Guardamos el tiempo actual y las métricas
            tiempo = len(tiempos) * intervalo  # El tiempo se calcula según los intervalos
            uso_cpu, uso_memoria, uso_disco = mostrar_estadisticas()
            
            tiempos.append(tiempo)
            uso_cpu_list.append(uso_cpu)
            uso_memoria_list.append(uso_memoria)
            uso_disco_list.append(uso_disco)
            
            # Actualizamos los gráficos agregando nuevos puntos
            axs[0].plot(tiempos, uso_cpu_list, label="Uso de CPU (%)", color='tab:red')
            axs[1].plot(tiempos, uso_memoria_list, label="Uso de Memoria (%)", color='tab:blue')
            axs[2].plot(tiempos, uso_disco_list, label="Uso de Disco (%)", color='tab:green')
            
            # Establecer límites dinámicos para evitar que los gráficos se queden fuera de rango
            axs[0].set_ylim(0, 100)
            axs[1].set_ylim(0, 100)
            axs[2].set_ylim(0, 100)
            
            # Añadir una pausa para que el gráfico se actualice
            plt.pause(intervalo)
    except KeyboardInterrupt:
        print("\nMonitorización detenida por el usuario.")
    finally:
        # Desactivamos el modo interactivo
        plt.ioff()
        plt.show()

# Ejecutar la monitorización indefinida (con intervalos de 2 segundos)
if __name__ == "__main__":
    monitorizar_sistema(intervalo=2)
