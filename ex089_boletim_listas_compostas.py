ficha = []
opção = 0
while True:    
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    again = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    while again not in 'SN':
        again = str(input('OPÇÃO INVÁLIDA! Deseja continuar?[S/N] '))
    if again in 'N':
        break
print ('-=' * 30)
print (f'{"N°":<5}{"NOME":<10}{"MÉDIA":>8}')
print ('-' * 30)
for índice, alunos in enumerate(ficha):
    print (f'{índice:<5}{alunos[0]:<10}{alunos[2]:>8}')
print ('-' * 30)
while True:
    opção = int(input('Mostrar notas de qual aluno?(999 interrompe)'))
    if opção == 999:
        print ('-' * 30)
        print ('FINALIZANDO')
        print ('-' * 30)
        break
    if opção <= len(ficha) - 1:
        print (f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')
print ('Volte sempre!')