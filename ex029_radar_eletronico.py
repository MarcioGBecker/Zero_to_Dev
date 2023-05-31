vel = float(input('Qaul a velocidade do carro? '))
multa = ((vel-80)*7)
if vel > 80:
    print ('Infelizmente você foi multado por excesso de velocidade')
    print (f'A Multa é de: R${multa:.2f}')
print ('Dirija com cuidado! Tenha um bom dia.')