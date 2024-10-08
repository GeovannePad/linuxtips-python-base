#!/usr/bin/env python3
"""Exemplos de escopos e o uso da palavra nonlocal em Python."""
__version__ = "0.1.0"
__license__ = "Unlicense"

contador = 0

def funcao():
    # Forçando o acesso a variável do escopo global dentro de uma função.
    global contador
    contador += 1

    subcontador = 0

    def funcao_interna():
        # Forçando o acesso a variável do escopo global mesmo dentro de
        # uma função interna.
        global contador
        contador += 1

        # Forçando o acesso a variável do escopo da função que 
        # envolve (escopo envolvente) a função interna.
        nonlocal subcontador
        subcontador += 1
    
    funcao_interna()

funcao()
funcao()

print(contador)