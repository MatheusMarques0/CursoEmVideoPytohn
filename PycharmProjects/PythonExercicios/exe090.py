aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Media: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'APROVADO'
else:
    aluno['Situação'] = 'REPROVADO'

print(f'Nome é igual a {aluno['Nome']}')
print(f'Média é igual a {aluno['Media']}')
print(f'Situação é igual a {aluno['Situação']}')