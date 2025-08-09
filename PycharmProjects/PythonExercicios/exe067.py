while True:
    c = 1
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break

    print(f'{'':-^30}')
    while c < 11:
        total = c * num
        print(f'{num} x {c} = {total}')
        c += 1
    print(f'{'':-^30}')


print('Programa interrompido por número negativo')