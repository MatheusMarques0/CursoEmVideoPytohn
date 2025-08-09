#Minha versão:
matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapares = 0
somaColuna = 0
segundalinha = []
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if c == 2:
            somaColuna += matriz[l][c]
        if l == 1:
            segundalinha.append(matriz[l][c])
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
       print(f'[{matriz[l][c]:^5}]', end='')
    print()
segundalinha.sort()
print(f'A soma de dos pares é igual a {somapares}')
print(f'A soma das colunas é igual a {somaColuna}')
print(f'O maior valor da segunda linha é igual a {segundalinha[-1]}')