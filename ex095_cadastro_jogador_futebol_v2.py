jogador = {}
gols = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Insira o nome do jogador: ')).capitalize()
    partidas = int(input(f'Insira quantas partidas {jogador["nome"]} jogou: '))
    gols.clear()
    for controle in range (0, partidas):
        gols.append(int(input(f'Insira quantos gols o {jogador["nome"]} fez na {controle + 1}ª partida: ')))
        jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    again = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    while again not in 'SN':
        again = str(input('OPÇÃO INVÁLIDA!! Deseja continuar?[S/N] ')).strip().upper()[0]
    if again == 'N':
        break
print ('-' * 40)
print ('cod ', end='')
for indice in jogador.keys():
    print (f'{indice:<15}', end='')
print ()
print ('-' * 40)
for chave, valor in enumerate(time):
    print (f'{chave:>4} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print ()
print ('-' * 40)

while True:
    busca = int(input('Mostrar os dados de qual jogador?(999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f'----- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} -----')
        for indice, gol in enumerate(time[busca]["gols"]):
            print (f'       No jogo {indice + 1} fez {gol} gols!')
    print ('-' * 40)
print ('Encerrando...')