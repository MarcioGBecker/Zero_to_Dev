matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []
maior = soma_coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par.append(matriz[linha][coluna])
        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
soma_par = sum(par)
print ('-=' * 22)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print (f'[{matriz[linha][coluna]:^5}]', end='')
    print ()
print ('-=' * 22)
print (f'A soma de todos os pares digitados é de: {soma_par}')
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print (f'A soma dos valores na 3ª coluna é de: {soma_coluna}')
print (f'O maior valor digitado na 2ª linha foi: {maior}')
print ('-=' * 22)
