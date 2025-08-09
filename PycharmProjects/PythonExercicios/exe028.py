print('Adivinhe o número que estou pensando! \n')
guess = int(input('\033[4mDica: é um número inteiro entre 0 e 5: \033[m'))


if guess == 3:
    print('\033[1:32mVocê acertou!\033[m')
else:
    print('\033[1:31mVocê errou!\033[m')