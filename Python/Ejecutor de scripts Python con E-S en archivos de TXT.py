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

ruta_archivo_entrada = r'D:\VSC Programs\IV Semestre\Lenguaje de Programación II\Python\Input.txt'
ruta_archivo_salida = r'D:\VSC Programs\IV Semestre\Lenguaje de Programación II\Python\Output.txt'

codigo = leer_codigo_desde_archivo(ruta_archivo_entrada)

salida = ejecutar_codigo(codigo)

escribir_salida_en_archivo(salida, ruta_archivo_salida)

paint("Ejecución completada. ✨")
