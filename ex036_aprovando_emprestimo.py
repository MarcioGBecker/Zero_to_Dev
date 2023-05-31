casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
meses = anos * 12
parcelas = casa / meses
porcentagem = salário * 30 / 100


if parcelas > porcentagem:
    print('Infelizmente não podemos liberar o empréstimo.')
    print(f'As parcelas de R${parcelas:.2f} e é mais de 30% do seu salário.')
elif parcelas == porcentagem:
    print ('Foi por muito pouco que seu empréstimo não foi aprovado.')
    print ('As parcelas devem ser menor que 30% de seu salário')
else:
    print ('PARABÉNS!! Seu empréstimo foi aprovado.')
print ('-=' * 20)
print (f'CONDIÇÕES DO EMPRÉSTIMO \nParcelas: R${parcelas:.2f} \nTempo: {meses} meses \nPorcentagem salarial: R${porcentagem:.2f}')
print ('-=' * 20)