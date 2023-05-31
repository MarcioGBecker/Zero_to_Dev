número = int(input('Informe um número: '))
print (f'A tabuada do número {número} é:')
for controle in range(0, 11):
    print (f'{número} x {controle:2} = {controle * número}')
