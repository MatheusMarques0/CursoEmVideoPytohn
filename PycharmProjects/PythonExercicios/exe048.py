soma = 0
count = 0

for n in range(1, 501):
    if n % 2 != 0:
        if n % 3 == 0:
            soma = soma + n
            count = count + 1
print('São {} valores, dando um total de {}'.format(count, soma))