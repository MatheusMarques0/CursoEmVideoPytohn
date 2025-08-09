import random

print('\033[33mJOKENPÔ\033[m')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura \n')

jokenpo = int(input('Escolha qual ação deseja: '))
while jokenpo != 1 and jokenpo != 2 and jokenpo != 3:
    jokenpo = int(input('Escolha um número entre 1 e 3, por favor:'))
num = random.randint(1, 3)

if jokenpo == 1 and num == 1:
    print('\033[1mPEDRA X PEDRA !\033[m')
    print('\033[33mEmpate! Ambos jogaram pedra\033[m')
elif jokenpo == 2 and num == 1:
    print('\033[1mPAPEL X PEDRA !\033[m')
    print('\033[32mO jogador venceu!\033[m')
elif jokenpo == 3 and num == 1:
    print('\033[1mTESOURA X PEDRA !\033[m')
    print('\033[31mO jogador pedeu!\033[m')

elif jokenpo == 1 and num == 2:
    print('\033[1mPEDRA X PAPEL !\033[m')
    print('\033[31mO jogador perdeu!\033[m')
elif jokenpo == 2 and num == 2:
    print('\033[1mPAPEL X PAPEL !\033[m')
    print('\033[33mEmpate! Ambos jogaram papel\033[m')
elif jokenpo == 3 and num == 2:
    print('\033[1mTESOURA X PAPEL !\033[m')
    print('\033[32mO jogador venceu!\033[m')

elif jokenpo == 1 and num == 3:
    print('\033[1mPEDRA X TESOURA !\033[m')
    print('\033[32mO jogador venceu!\033[m')
elif jokenpo == 2 and num == 3:
    print('\033[1mPAPEL X TESOURA !\033[m')
    print('\033[31mO jogador perdeu!\033[m')
elif jokenpo == 3 and num == 3:
    print('\033[1mTESOURA X TESOURA !\033[m')
    print('\033[33mEmpate! Ambos jogaram tesoura!\033[m')