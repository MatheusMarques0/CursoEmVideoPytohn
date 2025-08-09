#clássico
num = int(input('Digite um número e descubra se ele é par: '))
if num % 2 == 0:
    print('O número é \033[7m par \033[m')
else:
    print('O número é \033[mímpar\033[m')