#pesos = []

#for n in range(1, 6):
    #peso = int(input('Digite o peso da {}° pessoa: '.format(n)))
    #pesos.append(peso)

#menor = min(pesos)
#maior = max(pesos)

#print('O menor peso é {}'.format(menor))
#print('O maior peso é {}'.format(maior))
# não quero fazer com listas

maior = 0
menor = 0
for n in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))