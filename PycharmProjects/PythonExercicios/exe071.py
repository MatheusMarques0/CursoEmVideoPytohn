valor = int(input('Digite o valor a ser sacado: '))
pagar = valor
cinquenta = 0
vinte = 0
dez = 0
um = 0

while True:
    if valor >= 50:
        valor -= 50
        cinquenta += 1
    elif valor >= 20:
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor > 0:
        valor -= 1
        um +=1
    elif valor == 0 or valor < 0:
        break

if cinquenta > 0:
    print(f'Total de {cinquenta} cédulas de R5:50')
if vinte > 0:
    print(f'Total de {vinte} cédulas de R5:20')
if dez > 0:
    print(f'Total de {dez} cédulas de R5:10')
if um > 0:
    print(f'Total de {um} cédulas de R5:1')