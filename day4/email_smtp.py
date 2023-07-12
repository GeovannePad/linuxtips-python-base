#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""
import smtplib

# Criando uma instância local do servidor de e-mail
SERVER = "localhost"
PORT = 8025 # porta padrão TCP 25, 8025 é um servidor de teste do Python

FROM = "geovannepadilha@hotmail.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá mundo </b>
"""

# \ evita a quebra de linha
# SMTP não aceita a primeira linha em branco.
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

# Abrir uma instância de servidor e ao terminar de mandar o e-mail, o servidor é fechado
with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))