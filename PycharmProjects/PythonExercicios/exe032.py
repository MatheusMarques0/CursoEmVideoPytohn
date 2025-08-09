ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print('O ano é \033[4;34mbissexto\033[m')
else:
    print('O ano não é \033[4;31mbissexto\033[m')