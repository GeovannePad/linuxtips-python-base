#!/usr/bin/env python3
"""Calculadora infix

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"
__license__ = "Unlicense"

import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("operação: ")
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)
    
validated_nums = []
for num in nums:
    # TODO: Usar repetição com while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
    
try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))  
    sys.exit(1)
    
# TODO: Usar dict de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2
    
print(f"O resultado é {result}")