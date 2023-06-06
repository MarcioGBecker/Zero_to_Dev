grupo = []
contador = soma = 0
while True:
    pessoas = {}
    contador += 1
    pessoas['nome'] = str(input(f'Insira o nome da {contador}ª pessoa: ')).capitalize()
    pessoas['sexo'] = str(input(f'Insira o sexo de {pessoas["nome"]}:[M/F] ')).strip().upper()[0]
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = str(input(f'OPÇÃO INVÁLIDA! Insira o sexo da {contador}ª pessoa:[M/F] ')).strip().upper()[0]
    pessoas['idade'] = int(input(f'Insira a idade de {pessoas["nome"]}: '))
    grupo.append(pessoas.copy())
    again = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    while again not in 'SN':
        again = str(input('OPÇÃO INVÁLIDA! Deseja continuar?[S/N] ')).strip().upper()[0]
    if again in 'N':
        break
print ('-=' * 30)
print (f'Ao todo tivemos {len(grupo)} pessoas cadastradas.')
for pessoas in grupo:
    valor = pessoas['idade']
    soma += valor
média = soma / len(grupo)
print (f'A média de idade do grupo é de {média:.2f} anos')
print (f'As mulheres cadastradas foram:', end= ' ')
for pessoas in grupo:
    if pessoas['sexo'] in 'F':
        print (pessoas['nome'], end= '.. ')
print ()
print (f'As pessoas acima da média de idade foram:', end= ' ')
for pessoas in grupo:
    if pessoas['idade'] > média:
        print (f'{pessoas["nome"]} com {pessoas["idade"]} anos', end= '.. ')
print()
print ('-=' * 30)
