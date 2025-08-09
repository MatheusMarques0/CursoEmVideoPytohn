listagem = (str(input('Digite um produto: ')), float(input('Digite o preço de um produto ')), str(input('Digite um produto: ')), float(input('Digite o preço de um produto ')),
            str(input('Digite um produto: ')), float(input('Digite o preço de um produto ')), str(input('Digite um produto: ')), float(input('Digite o preço de um produto ')),
            str(input('Digite um produto: ')), float(input('Digite o preço de um produto ')), str(input('Digite um produto: ')), float(input('Digite o preço de um produto ')))

print(f"{'-' * 40}")
print(f"{'Lista de Compras':^40}")
print(f"{'-' * 40}")

for n in range (0, 12, 2):
    print(f'{listagem[n]:.<30}R$ {listagem[n + 1]}')

print(f"{'-' * 40}")