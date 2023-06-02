from random import randint
from time import sleep
lista = []
jogos = []
quantidade = int(input('Quantos jogos você deseja fazer? '))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        número = randint(1, 60)
        if número not in lista:
            lista.append(número)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total +=1
print ('-=' *5, f'SORTEANDO {quantidade} JOGOS', '-=' *5)
for indice, valor in enumerate(jogos):
    print (f'Jogo {indice + 1}: {valor}')
    sleep(1)
    