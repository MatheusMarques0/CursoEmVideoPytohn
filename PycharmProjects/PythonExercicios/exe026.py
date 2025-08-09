frase = str(input('Digite uma frase: '))
frase = frase.lower().strip()

print('A palavra A aparece \033[33m{}\033[m vezes na frase'.format(frase.count('a')))
print('A palavra A aparece na posição \033[33m{}\033[m pela primeira vez'.format(frase.find('a')+1))
print('A palavra A aparece na posião \033[33m{}\033[m pela última vez'.format(frase.rfind('a')+1))