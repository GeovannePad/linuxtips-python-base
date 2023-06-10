#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

# Biblioteca Pretty Print, um print mais bonito
from pprint import pprint

produto = {
    "nome": "Caneta",
    "cores": ["Azul", "Branco"],
    "preco": 3.23,
    "dimensoes": {
        "altura": 12.1, 
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}


cliente = {
    "nome": "Bruno"
}
compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

# pprint(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)