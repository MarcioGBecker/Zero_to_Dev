from datetime import date
ano = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = ano - nascimento
faltam = 18 - idade
passaram = idade - 18

if idade < 18:
    print ('Você ainda não precisa se alistar.')
    print (f'Ainda faltam {faltam} anos para seu alistamento')
elif idade == 18:
    print ('Você deve se alistar \033[31mIMEDIATAMENTE\033[m!. \nJá fez sua inscrição?')
else:
    print('Seu período de alistamento já passou!')
    print(f'Já se passaram {passaram} anos do seu alistamento.')