#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10

---Tabuada do 1---

    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3

...

##################
---Tabuada do 2---

    2 x 1 = 2
    2 x 2 = 4

...

##################
"""
__version__ = "0.1.1"
__author__ = "Geovanne"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Define uma lista.

# Função range que gera uma sequência de números. Ao terminar tem que ser sempre um número a mais, por ser não inclusivo.
# Função list converte um objeto para uma lista.
numeros = list(range(1, 11)) 

# Iterable (percorríveis)
# Para cada número em números.
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)