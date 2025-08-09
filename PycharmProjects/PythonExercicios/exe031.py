distancia = int(input('Digite a distância da viagem (em Km): '))

if distancia > 200:
    price = distancia * 0.45
    print('O preço da viagem de {} Kms será de R$: \033[32m{}\033[m'.format(distancia, price))
else:
    preco = distancia * 0.50
    print('Uma viagem de {} Km custará R$: \033[32m{}\033[m'.format(distancia, preco))