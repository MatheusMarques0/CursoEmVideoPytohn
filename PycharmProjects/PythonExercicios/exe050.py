soma = 0

for n in range (6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num

print('A soma dos números pares são: {}'.format(soma))