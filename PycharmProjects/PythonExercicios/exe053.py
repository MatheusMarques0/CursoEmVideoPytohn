frase = str(input('Escreva uma frase e veja se é um palindromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for n in range(len(junto) -1, -1, -1):
    inverso += junto[n]

print('A frase ao contrário é: {}'.format(inverso))
if inverso == junto:
    print('a frase é um palindromo')
else:
    print('a frase não é um palindromo')