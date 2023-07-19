#!/usr/bin/env python

def function_name(a: int, b: int, c: int) -> int:
    """ Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c
    Quando o parâmetro a tiver o valor 10 vai acontecer x.

    >>> nome_da_funcao(1, 2, 3)
    """
    result = a + b + c
    return result

value = function_name(1, 2, 3)
print(value)

def another_function(a, b, c):
    """Explica o que ela faz"""
    return a * 2, b * 2, c * 2

print(another_function(1, 2, 3))

########################################

# Passagem de argumentos com desempacotamento

def sum(n1, n2):
    """Realiza a soma de 2 números"""
    return n1 + n2

# Normal
print(sum(10, 20))

# Argumentos em sequência

# Tuplas
args = (20, 30)
print(sum(*args)) # Modo posicional, o primeiro elemento de args encaixa no primeiro elemento da função

# Dicionários
args = {"n2": 90, "n1": 100}
#print(sum(n1=args["n1"], n2=args["n2"]))
print(sum(**args))

# Lista de dicionários
list = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650},
    (5, 10),
    [8, 13],
]

for item in list:
    if isinstance(item, dict): # Verifica o tipo da variável, retorna True ou False
        print(sum(**item))
    else:
        print(sum(*item))