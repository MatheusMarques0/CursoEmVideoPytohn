numeros = []
while True:
    numero = float(input('Digite um valor: '))
    if numero in numeros:
        numero = float(input('Valor duplicado! Não é possível adicionar..'))
    else:
        numeros.append(numero)
        print('Valor adicionado com sucesso')
    conf = str(input('Quer continuar? [S/N]: ')).upper()
    if conf == 'N':
        break

print(f'Você digitou os valores {numeros}')