pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
Birthday = int(input('Ano de nascimento: '))
age = 2025 - Birthday
pessoa['Idade'] = age
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de Contratação'] = int(input('Digite o ano de Contratação: '))
    pessoa['Salário'] = float(input('Digite o salário: '))
    AposentadoriaExpc = pessoa['Ano de Contratação'] + 35
    pessoa['Aposentadoria'] = AposentadoriaExpc - Birthday
    print('-=' * 20)
    print(f'Nome tem o valor {pessoa['Nome']}')
    print(f'Idade tem o valor {pessoa['Idade']}')
    print(f'CTPS tem o valor {pessoa['CTPS']}')
    print(f'Salário tem o valor {pessoa['Salário']}')
    print(f'Aposentadoria tem o valor {pessoa['Aposentadoria']}')
else:
    print('-=' * 20)
    print(pessoa)
    print(f'Nome tem o valor {pessoa['Nome']}')
    print(f'Idade tem o valor {pessoa['Idade']}')
    print(f'CTPS tem o valor {pessoa['CTPS']}')