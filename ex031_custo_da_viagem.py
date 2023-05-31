km = float(input('Diga quantos Km você irá viajar: '))
if km <= 200:
    print (f'Você está prestes a fazer uma viagem de {km:.1f}km')
    print (f'O valor da sua passagem será: R${km*0.5:.2f}')
else:
    print (f'Você está prestes a fazer uma viagem de {km:.1f}km')
    print (f'O valor da sua passagem será: R${km*0.45:.2f}')