#clearPrimera Versión
import psutil
import time
from datetime import datetime

# Función para mostrar el uso de CPU, memoria y disco
def mostrar_estadisticas():
    print("\n--- Estadísticas del Sistema ---")

    # Uso de CPU
    uso_cpu = psutil.cpu_percent(interval=1)
    print(f"Uso de CPU: {uso_cpu}%")

    # Uso de memoria
    memoria = psutil.virtual_memory()
    print(f"Uso de Memoria: {memoria.percent}% (Usado: {memoria.used / (1024**3):.2f} GB / Total: {memoria.total / (1024**3):.2f} GB)")

    # Uso de disco
    disco = psutil.disk_usage('/')
    print(f"Uso de Disco: {disco.percent}% (Usado: {disco.used / (1024**3):.2f} GB / Total: {disco.total / (1024**3):.2f} GB)")

# Función principal para actualizar y registrar las métricas
def monitorizar_sistema(duracion=30, intervalo=5):
    print("Iniciando monitorización del sistema...")
    inicio = datetime.now()
    
    try:
        while (datetime.now() - inicio).seconds < duracion:
            mostrar_estadisticas()
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nMonitorización detenida por el usuario.")
    finally:
        print("\nFinalizó la monitorización del sistema.")

# Ejecutar la monitorización (duración total de 30 segundos, con intervalos de 5 segundos)
if __name__ == "__main__":
    monitorizar_sistema(duracion=40, intervalo=3)

