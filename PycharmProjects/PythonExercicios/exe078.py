numeros = []
for n in range(5):
    valor = float(input('Digite um número: '))
    numeros.append(valor)
print(f'O maior valor foi \033[32m{max(numeros)}\033[m na posição {numeros.index(max(numeros)) + 1}')
print(f'o menor valor foi \033[32m{min(numeros)}\033[m na posição {numeros.index(min(numeros)) + 1}')