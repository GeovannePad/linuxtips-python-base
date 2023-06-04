#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10

Tabuada do 1
1
2
3
...
-------------------
Tabuada do 2
2
4
...
-------------------

"""
__version__ = "0.1.0"
__author__ = "Bruno"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Define uma lista.

# Função range que gera uma sequência de números. Ao terminar tem que ser sempre um número a mais, por ser não inclusivo.
# Função list converte um objeto para uma lista.
numeros = list(range(1, 11)) 

# Iterable (percorríveis)
# Para cada número em números.
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-------------")