num = int(input('Digite algum número: '))
conf = "S"
total = 1
maior = num
menor = num
soma = num
confi = str(input('Quer continuar? [S/N]: ')).upper()

while confi == 'S':
    num = int(input('Digite algum número: '))
    total += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma = soma + num
    confi = str(input('Quer continuar? [S/N]: ')).upper()
media = soma / total
print('Você digitou {} números, sendo o maior valor \033[32m{}\033[m e o menor \033[31m{}\033[m. Com uma média de \033[33m{}\033[m'.format(total, maior, menor, media))