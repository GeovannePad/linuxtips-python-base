#!/usr/bin/env python3
"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""

# [S]OLID - Single Responsibility

# Definir uma função
def f(x): # Assinatura da função
    # Corpo da função
    result = 5 * (x / 2)
    return result # Caso não haja um return específico, toda função retorna None

def double(x):
    return x * 2

print(double(10))
print(f(10))
print(f(10) == 25)


####


# Procedimento / Procedure - Sem retorno explícito
def print_in_upper(text):
    print(text.upper())
    
value = print_in_upper("bruno")
print(value)

def heron(a, b, c):
    """Calcula a área de um triângulo que não seja equilátero."""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5 # math.sqrt(area)

def heron2(params):
    a, b, c = params
    return heron(a, b, c)

area_triangle = heron(3, 4, 5)
print(area_triangle)

triangles = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
]

print(list(map(heron2, triangles)))

for triangle in triangles:
    area = heron(*triangle)
    print(f"A área do triângulo é: {area}")

