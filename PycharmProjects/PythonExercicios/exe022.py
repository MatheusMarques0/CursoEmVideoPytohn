name = str(input('Digite o seu nome: '))

print('O seu nome com todas as letras maiúsculas é: {}'.format(name.upper()))
print('O seu nome com todas as letras minúsculas é: {}'.format(name.lower()))
print('O seu nome tem {} letras'.format(len(name.replace(' ',''))))
print('O seu primeiro nome tem {} letras'.format(len(name.split(' ')[0][0:])))