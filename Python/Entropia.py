import math
from collections import Counter

def calcular_entropia(texto):
    frecuencia = Counter(texto)
    total_caracteres = len(texto)
    
    probabilidades = [frec / total_caracteres for frec in frecuencia.values()]
    
    entropia = -sum(p * math.log2(p) for p in probabilidades)
    
    return entropia

def leer_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

nombre_archivo = 'D:/VSC Programs/IV Semestre/Lenguaje de Programación II/Python/I Unidad/Como.txt'
texto = leer_archivo(nombre_archivo)
entropia = calcular_entropia(texto)
print(f'La entropía del texto es: {entropia}')

