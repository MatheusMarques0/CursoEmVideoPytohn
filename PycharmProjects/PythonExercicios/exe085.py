#a forma que fiz (deu certo):
#listaUnica = list()
#pares = list()
#impares = list()
#
#for n in range(0, 7):
#    valores = int(input('Digite um valor inteiro: '))
#    if valores % 2 == 0:
#        pares.append(valores)
#    else:
#        impares.append(valores)
#
#pares.sort()
#impares.sort()
#listaUnica.append(pares)
#listaUnica.append(impares)
#
#print(f'Os valores pares são: {listaUnica[0]}')
#print(f'Os valores ímpares são: {listaUnica[1]}')
num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores digitados foram: {num[0]}')
print(f'Os valores digitados foarm: {num[1]}')
