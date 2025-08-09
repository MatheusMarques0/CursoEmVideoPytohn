lista = []
total = 0
cinco = 0

for n in range(5):
    num = float(input('Digite um número: '))
    lista.append(num)
    total += 1
    if num == 5:
        cinco += 1

lista.sort(reverse = True)
print('\n')
print(f'Foram digitados {total} números')
print(f'A lista de valores em forma decrescente é: {lista}')
if cinco > 0:
    print('O número cinco foi digitado e está na lista')
else:
    print('O número 5 não foi digitado')