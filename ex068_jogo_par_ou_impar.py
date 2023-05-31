from random import randint
vitória = 0
while True:
    print ('~' * 20)
    print ('JOGO DO PAR OU ÍMPAR')
    print ('~' * 20)
    valor = int(input('Escolha um valor: '))
    computador = randint(0, 10)
    total = computador + valor
    opção = ' '
    while opção not in 'PI':
            opção = str(input('Escolha PAR ou ÍMPAR:[P/I] ')).strip().upper()[0]
    print (f'Você jogou {valor} e o computador jogou {computador} a soma é {total}!')
    print ('DEU PAR!' if valor % 2 == 0 else 'DEU ÍMPAR!')
    if opção == 'P':
        if total % 2 == 0:
            print ('Você venceu!')
            vitória += 1
        else:
            print ('Você perdeu!')
            break
    elif opção == 'I':
        if total % 2 != 0:
            print ('Você venceu!')
            vitória += 1
        else:
            print ('Você perdeu!')
            break
    print ('Vamos jogar novamente...')
print (f'GAME OVER! Total de vitórias: {vitória}')
