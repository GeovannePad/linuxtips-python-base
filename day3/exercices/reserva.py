#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponíveis para alugar e o preço de cada quarto, esta informação está 
disponível em um arquivo de texto separado por vírgulas.

`quartos.txt` 
# codigo, nome, preço
1, Suite Master, 500
2, Quarto Familia, 200
3, Quarto Single, 100
4, Quarto Simples, 50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
# cliente, quarto, dias
Bruno, 3, 12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
import sys
import os
import logging

log = logging.Logger("reserva")

# Caminhos dos arquivos de quartos e reservas
path = os.curdir
rooms_filepath = os.path.join(path, "day3", "exercices", "reserva", "quartos.txt")
reservations_filepath = os.path.join(path, "day3", "exercices", "reserva", "reservas.txt")

# Criando o arquivo de reserva, caso não exista
if not os.path.exists(reservations_filepath):
    os.mknod(os.path.join(path, "day3", "exercices", "reserva", "reservas.txt"))
# Lendo o arquivo de reservas e armazenando os quartos que já estão reservados em uma lista.
reserved_rooms = []
# Verificando se o arquivo está vazio
if not os.stat(reservations_filepath).st_size == 0:
    for line in open(reservations_filepath):
        _, reserved_room, _ = line.split(",")
        reserved_rooms.append(int(reserved_room.strip()))


# Lendo o arquivo de quartos e armazenando os dados dos quartos em um dicionário.
try:
    rooms = {}
    for line in open(rooms_filepath):
        room_number, room_name, room_price = line.split(",")
        rooms[int(room_number)] = {
            "name": room_name.strip(),
            "price": float(room_price.replace("\n", "").strip()),
            "available": False if int(room_number) in reserved_rooms else True,
        }
except FileNotFoundError:
    print("Arquivo de quartos não existe.")
    sys.exit(1) 

client_name = input("Qual é o seu nome?: ")
# Tabela mostrando os quartos
print("{:-^59}".format("Quartos"))
print("{:^12} | {:^14} | {:^14} | {:^8}".format("Nº do quarto", "Tipo de quarto", "Valor em reais", "Disponível"))
for room in rooms:    
    print("{:^12} | {:^14} | {:^14.2f} | {:^8}".format(room, rooms[room]["name"], rooms[room]["price"], "✅" if rooms[room]["available"] else "❌"))
print("-" * 59)

# Verificando se foram inseridos valores não numéricos na variável "room" e se o nº do quarto existe
try:
    room = int(input("Qual o número do quarto que deseja reservar?: "))
    if room in reserved_rooms:
        print(f"O Quarto {room} já está reservado!")
        sys.exit(1)
    elif not room in rooms.keys():
        print(f"O Quarto {room} é inválido")
        sys.exit(1)
except ValueError as e:
    log.error("Valor não numérico inserido, favor inserir novamente!")
    print(e)
    sys.exit(1)

# Verificando se foi inserido valores não numéricos na variável "days"
try:
    days = int(input("Quantos dias deseja ficar?: "))
except ValueError as e:
    log.error("Valor não numérico inserido, favor inserir novamente!")
    print(e)
    sys.exit(1)

confirmation = input("Gostaria de confirmar a reserva? (S(s) ou Sim/N(n) ou Não): ")

if confirmation in "SsSim":
    print(f"O valor total da sua reserva é de {rooms[room]['price'] * days}")
    with open(reservations_filepath, "a") as file_:
        file_.write(f"{client_name}, {room}, {days} \n")
else:
    print("Reserva cancelada.")