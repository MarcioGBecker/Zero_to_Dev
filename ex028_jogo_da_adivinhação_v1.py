from random import randint
from time import sleep
cnum = randint(0 , 5)

print('-=-' * 20)
print ('Vou pensar em um númer de 0 a 5.')
print('-=-' * 20)
unum = int(input('Tente adivinhar: '))
print ('PROCESSANDO...')
sleep(2)

if unum == cnum:
    print ('UAU VOCÊ ACERTOU!')
else:
    print (f'Sabia que você iria errar! O número que eu pensei foi {cnum} e não {unum}')