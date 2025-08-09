maiores = 0
homens = 0
mulheres20 = 0

print(f'{'':-^30}')
print('CADASTRE UMA PESSOA')
print(f'{'':-^30}')
while True:
    conf = str(input('Quer cadastrar uma pessoa? [S/N]: ')).upper()
    if conf == 'N':
        break
    else:
        idade = int(input('Digite a sua idade: '))
        genero = str(input('Digite o seu sexo [F/M]: ')).upper()
        if idade > 18:
            maiores += 1
        if genero == 'M':
            homens += 1
        if idade < 20 and genero == 'F':
            mulheres20 += 1

print(f'* O programa contou com \033[33m{maiores}\033[m pessoas acimca de 18 anos;')
print(f'* O programa contou com \033[33m{homens}\033[m homens;')
print(f'* O programa contou com \033[33m{mulheres20}\033[m mulheres abaixo de 20 anos;')