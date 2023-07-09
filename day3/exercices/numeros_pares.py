#!/usr/bin/env python
"""
Faça um programa que imprime os números pares de 1 a 200

ex
`python3 numeros_pares.py`
2
4
6
8
...
"""

numero = 1
while numero <= 200:
    if numero % 2 == 0:
        print(numero)
    numero += 1

"""
for num in range(1, 201):
    if num % 2 == 0:
        print(num)
"""
    