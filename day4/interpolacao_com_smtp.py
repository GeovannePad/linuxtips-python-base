#!/usr/bin/env python3
"""Imprime um template de e-mail para várias pessoas diferentes"""
__version__ = "0.1.1"
__author__ = "Geovanne"

import os
import sys
import smtplib
from email.mime.text import MIMEText # Template pronto e estruturado

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit(1)
    
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, "day3", "txts", filename)
templatepath = os.path.join(path, "day3", "txts", templatename)

with smtplib.SMTP(host="localhost", port=8025) as server:
    for line in open(filepath):
        name, email = line.split(",")
        text = (
            open(templatepath).read() % {
                "nome": name,
                "produto": "Caneta",
                "texto": "Escrever muito bem",
                "link": "https://canetas.com",
                "quantidade": 1,
                "preco": 50.50,
            }
        )    
        from_ = "geovannepadilha@hotmail.com"
        to = ", ".join([email])
        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to
        
        server.sendmail(from_, to, message.as_string())