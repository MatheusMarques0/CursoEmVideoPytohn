#numeros = []
#def lin():
#    print('-=' * 25)
#
#def maior(lista):
#    maior = 0
#    for n in lista:
#        if n > maior:
#            maior = n
#    print(f'O maior número é o {maior}')
#
#qtd = int(input('Quantos números serão usados? '))
#for b in range(qtd):
#    num = int(input(f'{b + 1}° Número: '))
#    numeros.append(num)
#
#maior(numeros)

#não percebi que era para usar o empacotador, my bad
from time import  sleep

def maior(*num):
    contador = maior = 0
    print('-=' * 25)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.3)
        if contador == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        contador += 1
    print(f'Fora, informados {contador} valores ao todo')
    print(f'O maior valor informado foi {maior}')

maior(2,9,5,7,1)
maior(4,7,0)
maior(1,2)