#Como eu fiz:
#matriz = [[], [], []]
#for a in range(0, 3):
#    valor1 = str(input(f'Digite um valor para [0, {a}]: '))
#    matriz[0].append(f"[ {valor1} ]")
#for b in range(0, 3):
#    valor2 = str(input(f'Digite um valor para [{b}, 0]: '))
#    matriz[1].append(f'[ {valor2} ]')
#for c in range(0, 3):
#    valor3 = str(input(f'Digite um valor para [{c}, {c}]: '))
#    matriz[2].append(f'[ {valor3} ]')
#print('-=' * 30)
#print(f'', end='')
#for n in range(0,3):
#    print(f'{matriz[0][n]}', end='')
#print('')
#
#print('', end='')
#for n in range(0,3):
#    print(f'{matriz[1][n]}', end='')
#print('')
#
#print('', end='')
#for n in range(0,3):
#    print(f'{matriz[2][n]}', end='')
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()