vel = int(input('Digite a velocidade que o carro passou (km/h): '))
multa = (vel - 80) * 7
if vel > 80:
    print('\033[1:31mVocê ultrapassou o limite de velocidade!\033[m')
    print('A multa a ser paga é de R$: {}'.format(multa))
else:
    print('\033[1:32mTudo certo!\033[m')
