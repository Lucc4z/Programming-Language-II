import nltk

# Definimos los símbolos no terminales
v0 = nltk.Nonterminal('v0')
v1 = nltk.Nonterminal('v1')
a = nltk.Nonterminal('a')
b = nltk.Nonterminal('b')

# Definimos las reglas de producción
production_rules = [
    nltk.Production(v0, ['a', v1]),
    nltk.Production(v1, ['b', v0]),
    nltk.Production(v1, ['a'])
]

# Creamos la gramática
grammar = nltk.CFG(v0, production_rules)

# Imprimimos la gramática
print(grammar)
