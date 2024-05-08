from itertools import product

def generar_lenguaje(n, p):
    alfabeto = list(range(n))
    for i in range(p + 1):
        print(f"L^{i} = [", end='')
        print(*[''.join(map(str, x)) for x in product(alfabeto, repeat=i)], sep=', ', end='')
        print("]")

n = int(input("Tamaño del alfabeto: "))
p = int(input("Potencia del lenguaje: "))

generar_lenguaje(n, p)
