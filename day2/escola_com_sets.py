#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequentam
cada uma das atividades.
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antônio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antônio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antônio"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]

# Listar de uma sala que tem interseção com uma atividade
for nome_atividade, atividade in atividades:

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print(f"Alunos de {nome_atividade} da Sala 1:", atividade_sala1)
    print(f"Alunos de {nome_atividade} da Sala 2:", atividade_sala2)
    print("-" * 10)
