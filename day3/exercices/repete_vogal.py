#!/usr/bin/env python3
"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex:
python3 repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""

"""
words = []
vowels = "aeiou"
while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    words.append(word)
    if not word:
        for word in words:
            for letter in word:
                if letter.lower() in vowels:
                    print(letter * 2, end="")
                else:
                    print(letter, end="")
            print()
        break
"""


words = []
while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if not word:
        break
    
    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        final_word += letter * 2 if letter.lower() in "aeiou" else letter
        
        # IF convencional
        """
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
        """
    
    words.append(final_word)

print(*words, sep="\n")
