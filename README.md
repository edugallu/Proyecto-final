# Monitorización de Sistema en Tiempo Real

Este script permite la monitorización en tiempo real de los recursos del sistema, como la CPU, la memoria y el uso del disco. El script recopila las métricas a intervalos regulares y las presenta visualmente en gráficos dinámicos. Además, guarda las estadísticas en un archivo de log para su posterior análisis. También emite advertencias si los valores de uso de CPU, memoria o disco superan los umbrales definidos.

## Requisitos

Para ejecutar este script, necesitas tener instaladas las siguientes librerías:

- `psutil`: Librería para obtener estadísticas del sistema, como el uso de la CPU, memoria y disco.
- `matplotlib`: Librería para la creación de gráficos en tiempo real.

Puedes instalar las librerías necesarias usando `pip`:

```bash
pip install psutil matplotlib
```
# Características

-`Monitorización en Tiempo Real`: 
Mide y visualiza el uso de la CPU, la memoria y el disco a intervalos regulares.
Archivos de Log: Guarda las métricas en un archivo de texto, lo que permite analizar los datos más tarde.

-`Gráficos Dinámicos`: Los gráficos se actualizan en tiempo real para mostrar el uso de los recursos del sistema.

-`Advertencias de Umbral`: Se emiten advertencias si el uso de algún recurso supera el umbral predeterminado.

# Descripción del Código

**Funciones**

`mostrar_estadisticas()`

Esta función obtiene las estadísticas de uso de la CPU, la memoria y el disco en tiempo real.

`Entrada`: Ninguna.

`Salida`: Tres valores flotantes correspondientes al uso de CPU, memoria y disco, expresados como porcentajes.

`verificar_umbral(uso_cpu, uso_memoria, uso_disco, umbral_cpu=80, umbral_memoria=80, umbral_disco=80)`

Verifica si el uso de la CPU, la memoria o el disco supera los umbrales definidos. Si se supera algún umbral, imprime una advertencia en la consola.

-`Entrada`:

- `uso_cpu: Porcentaje de uso de CPU.`

- `uso_memoria: Porcentaje de uso de memoria.`

- `uso_disco: Porcentaje de uso de disco.`

- `umbral_cpu: Umbral para el uso de CPU (por defecto 80%).`

- `umbral_memoria: Umbral para el uso de memoria (por defecto 80%).`

- `umbral_disco: Umbral para el uso de disco (por defecto 80%).`

-`Salida`: 
Imprime advertencias en consola si el uso de algún recurso supera su respectivo umbral.

`monitorizar_sistema(intervalo=2, archivo_log="metrics_log.txt")`

Esta función monitoriza el sistema en tiempo real, recopilando las estadísticas de CPU, memoria y disco a intervalos regulares. Los resultados se guardan en un archivo de log y los gráficos se actualizan en tiempo real.

-`Entrada`:

- `intervalo`: Intervalo de tiempo (en segundos) entre cada medición de los recursos del sistema. El valor por defecto es 2 segundos.

- `archivo_log`: Nombre del archivo de log en el que se guardarán las métricas. El valor por defecto es metrics_log.txt.

- `Salida`: Muestra las estadísticas en consola, actualiza los gráficos y guarda los datos en el archivo de log.

**Excepciones y Manejo de Errores**

El código maneja excepciones como la interrupción del programa por parte del usuario (Ctrl+C) y otros errores generales. Cuando el script es detenido por el usuario, imprime un mensaje y cierra correctamente los gráficos.

## Ejecución

Para ejecutar este script, sigue estos pasos:

Clona este repositorio o descarga el archivo del script en tu máquina local.
Asegúrate de tener instaladas las dependencias (psutil y matplotlib) ejecutando el siguiente comando:
```bash
pip install psutil matplotlib
```
Ejecuta el script en tu terminal o línea de comandos con:
```bash
python nombre_del_script.py
```
El script comenzará a monitorizar el sistema, mostrando las estadísticas de uso de CPU, memoria y disco, y generará un archivo de log en la ubicación especificada.

## Personalización

Puedes personalizar diversos aspectos del script según tus necesidades:

- `Umbrales de Alerta`: Modifica los valores de los umbrales en la función verificar_umbral(). Los valores por defecto son 80% para la CPU, la memoria y el disco.

- `Intervalo de Medición`: Cambia el valor del parámetro intervalo en la llamada a monitorizar_sistema() para ajustar el tiempo entre cada medición (en segundos).

- `Archivo de Log`: Cambia el nombre del archivo de log proporcionando un nuevo nombre como argumento en monitorizar_sistema().

**Ejemplo de Uso**

Si deseas monitorizar el sistema con un intervalo de 5 segundos y guardar las métricas en un archivo de log llamado system_metrics.log, puedes ejecutar el siguiente código en el script:
```bash
monitorizar_sistema(intervalo=5, archivo_log="system_metrics.log")
```
**Salida Esperada**

Al ejecutar el script, verás las siguientes salidas:

- `En la Consola`: Las métricas de uso de CPU, memoria y disco se imprimirán en la consola con la fecha y hora actualizadas. Además, si el uso de algún recurso supera el umbral configurado, aparecerá una advertencia.

Ejemplo:
```bash
Datos: 2025-01-26 12:00:02, CPU: 45.23%, Memoria: 62.14%, Disco: 58.50%
```
- `Gráficos`: Se abrirá una ventana con tres gráficos que muestran el uso de CPU, memoria y disco a lo largo del tiempo.

- `Archivo de Log`: Se generará un archivo metrics_log.txt (o el nombre que hayas configurado) con las métricas guardadas en el siguiente formato:
```bash
Fecha y Hora, Uso CPU (%), Uso Memoria (%), Uso Disco (%)
2025-01-26 12:00:02, 45.23, 62.14, 58.50
2025-01-26 12:00:04, 46.30, 63.21, 60.00
```
## Capturas de Pantalla

Aquí hay un ejemplo de cómo se verán los gráficos generados:

- `Gráfico de Uso de CPU`
- `Gráfico de Uso de Memoria`
- `Gráfico de Uso de Disco`

## Advertencias

- `Superación de Umbrales`: Si el uso de la CPU, memoria o disco supera el umbral predeterminado (80%), el script imprimirá una advertencia en la consola.

Ejemplo de advertencia:
```bash
⚠ Advertencia: Uso de CPU (85.42%) ha superado el umbral de 80%
```

## Contribuciones

Si deseas contribuir a este proyecto, puedes hacerlo de las siguientes maneras:

- `Abrir un issue`: Si encuentras algún error o tienes una idea para mejorar el proyecto, abre un issue.

-`Enviar un Pull Request`: Si tienes una mejora o corrección, siéntete libre de enviar un pull request con tu cambio.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.