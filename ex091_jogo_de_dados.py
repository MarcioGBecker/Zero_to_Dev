from random import randint
from time import sleep
from operator import itemgetter
rancking = []
dados = {'Jogador1':randint(1, 6),
'Jogador2':randint(1, 6),
'Jogador3':randint(1, 6),
'Jogador4': randint(1, 6)}
for chave, valor in dados.items():
    print (f'{chave} tirou {valor}')
    rancking = sorted(dados.items(), key=itemgetter(1), reverse=True)
    sleep(1)
print ('===== RANCKING ======')
for chave, valor in enumerate(rancking):
    print (f'{chave + 1}° lugar: {valor[0]} com {valor[1]}')
    sleep(1)
    