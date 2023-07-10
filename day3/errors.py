#!/usr/bin/env python3

import sys
import os

# EAFP - Easy To Ask Forgiveness Than Permission

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))

try:
    names = open("day3/txts/names.txt").readlines() #FileNotFoundError
except (FileNotFoundError, ZeroDivisionError) as e:
    print(str(e))
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)