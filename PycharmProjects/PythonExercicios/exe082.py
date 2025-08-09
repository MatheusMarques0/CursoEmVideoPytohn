lista = []
pares = []
impares = []
for n in range(8):
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append((num))

print(f'Lista dos valores totais: {lista}')
print(f'Lista dos valores pares: {pares}')
print(f'Lista dos valores ímpares: {impares}')