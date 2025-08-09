Galera = list()
pessoa = dict()
mulheres = []
AcimaDaMedia = []
qtd = int(input('Quantas pessoas participarão? '))
mediatotal = 0
for n in range(qtd):
    pessoa[f'Pessoa{n}'] = dict()
    pessoa[f'Pessoa{n}']['Name'] = str(input('Nome:'))
    pessoa[f'Pessoa{n}']['Sexo'] = str(input('Sexo (F = feminino / M = masculino): ')).upper()
    if pessoa[f'Pessoa{n}']['Sexo'] == 'F':
        mulheres.append(pessoa[f'Pessoa{n}']['Name'])
    pessoa[f'Pessoa{n}']['Idade'] = int(input('Idade: '))
    mediatotal += pessoa[f'Pessoa{n}']['Idade']
    print('-' * 20)
media = mediatotal / qtd
Galera.append(pessoa)
print(Galera)
print(f'{qtd} pessoas participarão.')
print(f'A média do grupo foi {media}')
print(f'As mulheres que participam foram: {mulheres}')
for p in range(qtd):
    if pessoa[f'Pessoa{p}']['Idade'] > media:
        AcimaDaMedia.append(pessoa[f'Pessoa{p}']['Name'])
print(f'As pessoas acima da média são: {AcimaDaMedia}')

