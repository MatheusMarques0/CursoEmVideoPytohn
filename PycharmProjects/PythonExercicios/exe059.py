opt = '0'
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um segundo número: '))

while opt != '5':
    print('\033[33m[1]\033[m Somar')
    print('\033[33m[2]\033[m Multiplicar')
    print('\033[33m[3]\033[m Maior')
    print('\033[33m[4]\033[m Novos números')
    print('\033[33m[5]\033[m sair do programa')

    opt = str(input('Digite a opção que deseja: '))
    while opt == '' or (opt != '1' and opt != '2' and opt != '3' and opt != '4' and opt != '5'):
        opt = str(input('\033[31m[ERRO] Digite um valor válido (1-5): '))

    if opt == "1":
        s = num1 + num2
        print('A soma dos dois número é igual a {}'.format(s))
    elif opt == '2':
        m = num1 * num2
        print('A multiplicação dos dois números é igual a {}'.format(m))
    elif opt == '3':
        if num1 > num2:
            print('O primeiro número ({}) é o maior'.format(num1))
        elif num2 > num1:
            print('O segundo número ({}) é o maior'.format(num2))
        else:
            print('os números são iguais')
    elif opt == '4':
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um segundo número: '))

print('\nPrograma cancelado! ')