import random
from time import sleep
jogo = list()
partidas = list()
print('\033[33m-=\033[m' * 25)
print(f'{'\033[33mMEGA SENA GENERATOR\033[m':^60}')
print('\033[33m-=\033[m' * 25)
qtd = int(input('Quantos jogos serão gerados? '))
print('\n')
print(f'*Sorteando {qtd} jogos...')
print('')
for j in range(qtd):
    for p in range(6):
        number = random.randint(1, 60)
        partidas.append(number)
    jogo.append(partidas[:])
    partidas.clear()

for n in range(qtd):
    print(f'Jogo {n + 1}: {jogo[n]}')
    sleep(1)
print(f'{'Boa Sorte!':^30}')