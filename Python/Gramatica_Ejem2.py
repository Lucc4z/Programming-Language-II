class Simbolo:
    def __init__(self, nombre, producciones):
        self.nombre = nombre
        self.producciones = producciones

    def generar_palabras(self, gramatica, max_depth=10):
        if max_depth == 0:
            return []
        palabras = []
        for produccion in self.producciones:
            if any(simbolo in produccion for simbolo in gramatica.simbolos):
                for simbolo, simbolo_obj in gramatica.simbolos.items():
                    if simbolo in produccion:
                        reemplazos = simbolo_obj.generar_palabras(gramatica, max_depth-1)
                        for reemplazo in reemplazos:
                            palabras.append(produccion.replace(simbolo, reemplazo, 1))
            else:
                palabras.append(produccion)
        return palabras

class Gramatica:
    def __init__(self, alfabeto, terminales, producciones):
        self.alfabeto = alfabeto
        self.terminales = terminales
        self.simbolos = {nombre: Simbolo(nombre, prod) for nombre, prod in producciones.items()}

    def mostrar_lenguajes(self):
        for nombre, simbolo in self.simbolos.items():
            print(f'Lenguaje para {nombre}: {simbolo.generar_palabras(self)}')

# Ejemplo de uso
gramatica = Gramatica(['a', 'b', 'c'], ['A', 'B', 'C'], {'A': ['aA', 'a'], 'B': ['bB', 'b'], 'C': ['cC', 'c']})
gramatica.mostrar_lenguajes()
