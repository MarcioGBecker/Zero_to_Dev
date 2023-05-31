while True:
    número = int(input('Informe um valor para ver sua tabuada: '))
    if número < 0:
        break
    for controle in range(0, 11):
        print (f'{número} x {controle} = {número * controle}')
print ('PROGRAMA DE TABUADA ENCERRANDO!')
print ('Volte sempre!')
