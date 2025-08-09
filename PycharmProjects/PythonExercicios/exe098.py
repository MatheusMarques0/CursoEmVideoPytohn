from time import  sleep

def lin():
    print('-=' * 20)

def contador(inicio, fim, passo):
    lin()
    print('Contagem de 1 até 10 de 1 em 1:')
    for n in range(1, 11):
        print(f'{n} ', end='')
        sleep(0.3)
    print('FIM!')
    sleep(0.5)
    lin()
    print('Contagem de 10 até 0 de 2 em 2:')
    for p in range(10, -1, -2):
        print(f'{p} ', end='')
        sleep(0.3)
    print('FIM!')
    sleep(0.5)
    lin()
    print('Agora é asua vez de personalizar a contagem!')
    inicio = int(input('ínicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    while passo == 0:
        passo = int(input('\033[31m[ERRO] digite um valor diferente de zero: \033[m'))
    lin()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}!')
    if passo < 0:
        passo = passo * -1
    if fim > inicio:
        for num in range(inicio, fim + 1, passo):
            print(f'{num} ', end='')
            sleep(0.3)
        print('FIM!')
    else:
        for num in range(inicio, fim - 1, passo*-1):
            print(f'{num} ', end='')
            sleep(0.3)
        print('FIM!')

contador(1, 10, 1)