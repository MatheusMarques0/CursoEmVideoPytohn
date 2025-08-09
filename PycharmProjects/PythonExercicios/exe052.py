num = int(input('Digite um número inteiro: '))
cont = 0

for n in range (2, num-1):
    if num % n == 0:
        cont = 1

if cont > 0:
    print('par')
else:
    print('ímpar')