#!/usr/bin/env python3
"""Imprime um template de e-mail para várias pessoas diferentes"""
__version__ = "0.1.1"
__author__ = "Geovanne"

import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit(1)
    
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, "day3", filename)
templatepath = os.path.join(path, "day3", templatename)

clientes = []
for line in open(filepath):
    name, email = line.split(",")

    # TODO: Substituir por envio de email
    print(f"Email enviado para: {email}")
    print(open(templatepath).read() % {
            "nome": name,
            "produto": "Caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetas.com",
            "quantidade": 1,
            "preco": 50.50,
        }
    )
    print("-" * 50)