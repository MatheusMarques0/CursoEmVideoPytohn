num = int(input('Digite alguns números (digite 999 para parar): '))
total = 0
soma = 0

while num != 999:
    total += 1
    soma = soma + num
    num = (int(input('Digite alguns números (digite 999 para parar): ')))

print('{} números foram digitados, dando uma soma de {}'.format(total, soma))