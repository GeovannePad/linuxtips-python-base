#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

sender = "geovannepadilha@hotmail.com"
receiver = "vinnicampz@gmail.com"
text = """\
Um e-mail qualquer de teste
"""

with smtplib.SMTP(host="sandbox.smtp.mailtrap.io", port=2525) as server:
    server.login(user="394a84b7184a93", password="f9ec7275aa3328")
    message = MIMEText(text)
    message["Subject"] = "Teste"
    message["From"] = sender
    message["To"] = receiver
    
    server.sendmail(sender, receiver, message.as_string())

print("Email enviado com sucesso")
