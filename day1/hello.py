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
__version__ = "0.0.1" # Metadado que determina a versão do programa.
__author__ = "Geovanne" # Metadado que determina o nome do autor do programa.
__license__ = "Unlicense" # Metadado que determina o tipo de licença do programa.

import os # Biblioteca usado para que o Python se comunique com o SO.

current_language = os.getenv("LANG", "en_US")[:5] # Comando para obter o valor de uma variável de ambiente, contendo um valor padrão "en_US" e sendo fatiada a partir do primeiro caractere até o quinto. [:5]
msg = "Hello, World!"

if current_language == "pt_BR": # Condicional if "se"
    msg = "Olá, Mundo!"
elif current_language == "it_IT": # Condicional elif "se não então"
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"

if __name__ == "__main__": # Condicional para definir um bloco principal de um Script Python quando o programa rodar dentro de um terminal.
    print(msg) # Função de imprimir algo na tela (output)
