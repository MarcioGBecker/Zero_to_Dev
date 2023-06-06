from datetime import date
ano = date.today().year
trabalhador = {}
trabalhador['nome'] = str(input('Insira o nome: ')).capitalize()
nascimento = int(input('Insira o ano de nascimento: '))
trabalhador['idade'] = ano - nascimento
trabalhador['ctps'] = int(input('Insira a CTPS:[Caso não possua aperte 0] '))
if trabalhador['ctps'] != 0:
    contratação = int(input('Insira o ano de contratação: '))
    trabalhador['contribuição'] = ano - contratação
    trabalhador['salário'] = float(input('Insira o salário: R$'))
    if trabalhador['contribuição'] < 35:
        trabalhador['aposentadoria'] = (35 - trabalhador['contribuição']) + trabalhador['idade']
        print ('-=' * 30)
        print (f'O trabalhador {trabalhador["nome"]} tem {trabalhador["idade"]} anos e pode se aposentar com {trabalhador["aposentadoria"]} anos!')
    elif trabalhador['contribuição'] >= 35:
        trabalhador['aposentadoria'] = 'Aposentado'
        print ('-=' * 30)
        print (f'O trabalhador {trabalhador["nome"]} tem {trabalhador["idade"]} anos e já pode se aposentar!')
else:
    print ('-=' * 30)
    print (f'O {trabalhador["nome"]} ainda não possui vínculo empregatício!')
print ('-=' * 30)
for key, value in trabalhador.items():
    if key == 'nome':
        print (f'O nome do trabalhador é: {value}')
    if key == 'idade':
        print (f'A idade de {trabalhador["nome"]} é {value} anos.')
    if key == 'ctps':
        if trabalhador['ctps'] == 0:
            print (f'{trabalhador["nome"]} não possui CTPS.')
        else:
            print (f'{trabalhador["nome"]} possui a CTPS número {value}.')
    if key == 'contribuição':
        print (f'{trabalhador["nome"]} tem {value} anos de contribuição.')
    if key == 'salário':
        print (f'Seu salário é de R${value:.2f}.')
