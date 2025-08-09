sexo = str(input('Digite o sexo da pessoa (M/F): ').upper())
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[31m[ERRO] DIgite um valor correto: \033[m').upper())

print('O sexo da pessoa é {}!'.format(sexo))