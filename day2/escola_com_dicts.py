#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequentam
cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Giovanni Padilha"

# Dados
salas = {
    "Sala-1": [
        "Erik",
        "Maia",
        "Gustavo",
        "Manuel",
        "Sofia",
        "Joana",
    ],
    "Sala-2": [
        "João",
        "Antônio",
        "Carlos",
        "Maria",
        "Isolda",
    ],
}

atividades = {
    "Inglês": [
        "Erik",
        "Maia",
        "Joana",
        "Carlos",
        "Antônio",
    ],
    "Música": [
        "Erik",
        "Carlos",
        "Maria",
    ],
    "Dança": [
        "Gustavo",
        "Sofia",
        "Joana",
        "Antônio",
    ],
}

# Listar de uma sala que tem interseção com uma atividade

for atividade in atividades:
    for sala in salas:
        alunos = set(salas[sala]) & set(atividades[atividade])
        print(f"Alunos de {atividade} da {sala}: ", alunos)
    print("-" * 50)    
