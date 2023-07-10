#!/usr/bin/env python
"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo
das condições:

temp maior 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp < 0: ALERTA: Frio extremo
"""
import logging
import sys
log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None,
} # Dict / Mutável

for key in info.copy().keys(): # Iterando um dict mutável
    try:
        info[key] = float(input(f"Qual a {key}?: ").strip())
        # Alterando durante a iteração
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temperatura = info["temperatura"]
umidade = info["umidade"]

if temperatura > 45:
    print("ALERTA!!! Perigo calor extremo")
elif temperatura > 30 and (temperatura * 3) >= umidade:
    print("ALERTA!!! Perigo de calor úmido")
elif temperatura >= 10 and temperatura <= 30:
    print("Normal")
elif temperatura >= 0 and temperatura < 10:
    print("Frio")
elif temperatura < 0:
    print("ALERTA!!! Frio extremo")