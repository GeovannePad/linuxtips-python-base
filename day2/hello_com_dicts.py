#!/usr/bin/env python3
"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, exemplo:

    export LANG=pt_BR    

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2" # Metadado que determina a versão do programa.
__author__ = "Geovanne" # Metadado que determina o nome do autor do programa.
__license__ = "Unlicense" # Metadado que determina o tipo de licença do programa.

import os # Biblioteca usado para que o Python se comunique com o SO.

current_language = os.getenv("LANG", "en_US")[:5] # Comando para obter o valor de uma variável de ambiente, contendo um valor padrão "en_US" e sendo fatiada a partir do primeiro caractere até o quinto. [:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language]) # Função de imprimir algo na tela (output)
