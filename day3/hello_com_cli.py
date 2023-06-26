#!/usr/bin/env python3
"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, exemplo:

    export LANG=pt_BR    

Ou informe através do CLI argument `--lang`

Ou o usuário terá que digitar

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Geovanne"
__license__ = "Unlicense"

import os
import sys 
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger(__name__, log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {"lang": None, "count": 1,} # Dicionário contendo os argumentos esperados e com seus valores padrões

# Iterando em cima de todos os elementos a partir do 2º passado no CLI
for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=") # Divide o argumento em dois pelo caractere "=" e desempacota a 1ª parte na variável "key" e a 2ª parte na variável "value"
    except ValueError as e:
        log.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)
        
    key = key.lstrip("-").strip() # Remove o caractere especial "-" do início da string, juntamente dos espaços em brancos de anbos os lados da variável "key".
    value = value.strip() # Remove os espaços em branco de ambos os lados da variável "value"
    
    # Tratamento para verificar se o argumento passado na CLI é o esperado ou não
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
        
    # Atribuindo os argumentos no dicionário para uso posterior
    arguments[key] = value

# Atribuindo o argumento "lang" para a variável "current_language"
current_language = arguments["lang"]

# Verificação para ver se a variável "current_language" não tem nenhum valor nela
if current_language is None:
    # TODO: Usar repetição
    
    # Verificar se a variável de ambiente "LANG", se existir obter o valor dela e atribuir a "current_language".
    # Caso não existir a variável de ambiente "LANG", perguntar ao usuário a língua desejada
    if "LANG" in os.environ:   
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

# Fatiando a variável para obter apenas a partir do quinto caractere.
current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

"""
# try com valor default
message = msg.get(current_language, msg["en_US"])
"""

try:
    current_language in msg
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")   
    sys.exit(1)

print(message * int(arguments["count"]))