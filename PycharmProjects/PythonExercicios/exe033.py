num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite um outro número: '))

if num1 > num2 and num1 > num3:
    print('\033[1:32mO número {} é o maior\033[m'.format(num1))
elif num2 > num1 and num2 > num3:
    print('\033[1:32mO número {} é o maior\033[m'.format(num2))
elif num3 > num2 and num3 > num1:
    print('\033[1:32mO número {} é o maior\033[m'.format(num3))
else:
    print('\033[1:31mNão existe um número maior, pois os maiores números foram repetidos\033')

if num1 < num2 and num1 < num3:
    print('\033[1:31mo número {} é o menor\033[m'.format(num1))
elif num2 < num1 and num2 < num3:
    print('\033[1:31mO número {} é o menor\033[m'.format(num2))
elif num3 < num2 and num3 < num1:
    print('\033[1:31mO número {} é o menor\033[m'.format(num3))
else:
    print('\033[1:31mNão existe um número menor, pois os maiores números foram repetidos\033[m')