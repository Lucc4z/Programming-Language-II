# Ejecutor de Scripts Python con E/S en Archivos de TXT

El **Ejecutor de Scripts Python con E/S en Archivos de TXT** es una herramienta diseñada para leer, ejecutar y almacenar la salida de scripts Python desde archivos de texto. Esta herramienta es ideal para tareas de automatización, procesamiento en lote y generación de registros de ejecución.

## ¿Qué hace?

- **Lectura de Código**: Obtiene el contenido de un archivo de texto que contiene un script Python.
- **Ejecución del Script**: Ejecuta el script Python dentro de un entorno controlado.
- **Almacenamiento de Salida**: Redirige la salida estándar del script, almacenando todo lo que normalmente se imprimiría en la consola.
- **Escritura de Salida**: Guarda la salida del script en un archivo de texto especificado, creando un registro persistente.

## ¿Cómo funciona el ejecutor?

### 1. Lectura del Archivo de Entrada

```python
def leer_codigo_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        codigo = archivo.read()
    return codigo

### 2. Redirección de la Salida Estándar

```python
old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout

### 3. Ejecución del Script

```python
local_vars = {
    "loki": loki,
    "cadena": cadena,
    "dino": dino,
    "integrales": integrales,
    "paint": paint,
    "metro": metro,
    "camaleon": camaleon,
    "europa": europa,
    "asistencia": asistencia,
    "union": lambda a, b: a + b
}
exec(codigo, {}, local_vars)

### 4. Restauración de la Salida Estándar

```python
sys.stdout = old_stdout

### 5. Escritura del Archivo de Salida

```python
def escribir_salida_en_archivo(salida, ruta_archivo_salida):
    with open(ruta_archivo_salida, 'w', encoding='utf-8') as archivo:
        archivo.write(salida)

## Código Completo:

```python
import sys
import io
import itertools as loki
import nltk as cadena
from lark import Lark as dino
import math as integrales
paint = print
metro = len
camaleon = range
europa = map
asistencia = list

def leer_codigo_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        codigo = archivo.read()
    return codigo

def escribir_salida_en_archivo(salida, ruta_archivo_salida):
    with open(ruta_archivo_salida, 'w', encoding='utf-8') as archivo:
        archivo.write(salida)

def ejecutar_codigo(codigo):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    try:
        local_vars = {
            "loki": loki,
            "cadena": cadena,
            "dino": dino,
            "integrales": integrales,
            "paint": paint,
            "metro": metro,
            "camaleon": camaleon,
            "europa": europa,
            "asistencia": asistencia,
            "union": lambda a, b: a + b
        }
        exec(codigo, {}, local_vars)
    except Exception as e:
        return f"Error al ejecutar el código: {e}"
    finally:
        sys.stdout = old_stdout
        salida = new_stdout.getvalue()
        return salida

ruta_archivo_entrada = r'D:\VSC Programs\IV Semestre\Lenguaje de Programaci´on II\Python\Input.txt'
ruta_archivo_salida = r'D:\VSC Programs\IV Semestre\Lenguaje de Programaci´on II\Python\Output.txt'

codigo = leer_codigo_desde_archivo(ruta_archivo_entrada)
salida = ejecutar_codigo(codigo)
escribir_salida_en_archivo(salida, ruta_archivo_salida)

paint("Ejecución completada.")
