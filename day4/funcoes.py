#!/usr/bin/env python

# Por que usar funções ?

# Código mais organizado

def welcome():
    print("Welcome to the test.")
    input("When you are ready press enter.")

def ask_questions(ask_color = False):
    name = input("name: ")
    print(f"It is nice to meet you {name}")
    
    if ask_color:
        color = input("Quat is your favorite color?: ")
        print(f"{color} is a great color!")
    
    input("Describe Yourself: ")
    print("Admirable!")

def goodbye():
    print("Goodbye.")
    
#welcome()
#ask_questions(ask_color=True)
#goodbye()

# Composições com funções

names = [
    "Bruno", 
    "João", 
    "Bernardo", 
    "Barbara", 
    "Brian",
]

# TODO: Usar lambdas

def starts_with_b(text):
    #return text[0].lower() == "b"
    return text.startswith(("B", "b"))

print(*list(filter(starts_with_b, names)))

