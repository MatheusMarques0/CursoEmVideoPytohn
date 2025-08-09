print('\033[33m100°\033[m')
import random

from time import sleep
numeros = []
pares = []

def sorteados():
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(5):
        num = random.randint(0, 100)
        numeros.append(num)
        print(f'{num} ', end='')
        sleep(0.5)
    print('PRONTO!')

def somapar():
    somapares = 0
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
            somapares += i
    print(f'A soma dos números pares {pares} da {somapares}')

sorteados()
somapar()