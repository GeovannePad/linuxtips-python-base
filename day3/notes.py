#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text: Anotação geral sobre carreira de tecnologia

$ notes.py read tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "day3", "txts", "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)
    
if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    sys.exit(1)
 
if arguments[0] == "new":
    # criação da nota
    title = arguments[1]
    text = [
        f"{title}",
        input("Tag:").strip(),
        input("Text:\n").strip(),
    ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n") # pega cada item na lista "text" e separa cada linha com o "\t"
     
if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")
            print(f"Text: {text}")
            print("-" * 30)
            print()
