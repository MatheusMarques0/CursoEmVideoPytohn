import random
maiores = 0
menores = 0
numeros = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

for n in range(5):
    if maiores == 0:
        maiores = numeros[n]
        menores = numeros[n]
    else:
        if numeros[n] > maiores:
            maiores = numeros[n]
        if numeros[n] < menores:
            menores = numeros[n]

print(f'Os números sorteados são: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {maiores}')
print(f'O menor valor sorteado foi: {menores}')