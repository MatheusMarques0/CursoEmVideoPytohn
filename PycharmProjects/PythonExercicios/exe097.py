def escreva(txt):
    tamanho = len(txt) + 10
    print('-' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('-' * tamanho)

texto = str(input('Escreva o título: '))
escreva(texto)