#!/usr/bin/env python3
"""Imprime um template de e-mail para várias pessoas diferentes"""
__version__ = "0.0.1"
__author__ = "Geovanne"


email_tmpl = """
Olá %(nome)s

Tem interesse em comprar %(produto)s?
 
Este produto é ótimo para resolver
%(texto)s
 
Clique agora em %(link)s
 
Apenas %(quantidade)d disponíveis!
 
Preço promocional %(preco).2f
"""

clientes = ["Maria", "João", "Bruno"]

for cliente in clientes:
    print(email_tmpl % {
            "nome": cliente,
            "produto": "Caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetas.com",
            "quantidade": 1,
            "preco": 50.50,
        }
    )