name = str(input('Digite um nome completo: '))
separado = name.split(' ')
qtd = len(separado) - 1

print('Primeiro nome: \033[31m{}\033[m'.format(separado[0]))
#print('Último nome {}'.format(separado[-1]))) não quero fazer dessa forma
print('último nome \033[36m{}\033[m'.format(separado[qtd]))
