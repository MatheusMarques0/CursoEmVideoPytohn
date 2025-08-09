classe = list()
aluno = list()
notas = list()

while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2
    notas.append(media)
    aluno.append(notas[:])
    classe.append(aluno[:])
    notas.clear()
    aluno.clear()
    qtd = str(input('Quer continuar? [S/N]: '))
    if qtd in 'Nn':
        break

print('-=' * 20)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 30)
for n in range(len(classe)):
    print(f'{n:<4}{classe[n][0]:<10}{classe[n][1][2]:>8.1f}')
print('-' * 30)
print('')
while True:
    conf = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if conf != 999:
        print(f'As notas de {classe[conf][0]} são {classe[conf][1][0:2]}')
    else:
        break