import random
streak = 0
print(f'{'':=^30}')
print('Vamos jogar par ou ímpar!')
print(f'{'':=^30}')

while True:
    numero = int(input('Diga um valor: '))
    p = input('PAR ou ÍMPAR? [P/I]: ').upper()
    print(f'{'':-^30}')
    num = random.randint(1, 10)
    soma = numero + num
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    print(f'Você jogou {numero} e o computador {num}. Total de {soma}, deu {resultado}!')
    print(f'{'':-^30}')
    if p == resultado:
        print('Você \033[32mVENCEU\033[m')
        print('Vamos jogar novamente...')
        print(f'{'':=^30}')
        streak += 1
    else:
        break

print('Você \033[31mPERDEU\033[m')
print(f'{'':=^30}')
print(f'GAME OVER! Você venceu {streak} vezes.')