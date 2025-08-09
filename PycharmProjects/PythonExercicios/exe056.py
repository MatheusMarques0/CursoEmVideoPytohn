ageMax = 0
maior = 0
maiorIdade = ''
menor = 0
chica = 0

for n in range (1, 5):
    name = str(input('diga o nome da {}° pessoa: '.format(n)))
    age = int(input('diga a idade da {}° pessoa: '.format(n)))
    sex = str(input('diga o sexo da {}° pessoa (F/M): '.format(n)))
    if sex == "m" or sex == 'M':
        if n == 1:
            maior = age
            maiorIdade = name
            menor = age
        elif age > maior:
            maior = age
            maiorIdade = name
    if sex == "F" or sex == "f":
        if age < 20:
            chica += 1

    ageMax += age

media = ageMax / 4

print('A média de idade do grupo é igual a {}'.format(media))
print('O homem mais velho tem {} anos, e se chama {}'.format(maior, maiorIdade))
print('{} é a quantidade de mulheres que têm menos de 20 anos'.format(chica))
