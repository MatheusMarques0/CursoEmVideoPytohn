'''
def ajuda(txt):
    print('\033[44m-' * 50)
    print(f'\033[44m{f'Acessando o manual do comando "{txt}"':^50}')
    print('\033[44m-' * 50)
    print(f'\033[40m', end='')
    help(txt)
    print(f'\033[m', end='')

while True:
    print('\033[43m-' * 50)
    print(f'\033[43m{'SISTEMA DE AJUDA PyHELP':^50}')
    print('\033[43m-' * 50)
    print('\033[m')
    texto = str(input('Função ou Biblioteca (digite "fim" para parar): '))
    if texto != 'fim':
        ajuda(texto)
    else:
        break

print('\033[41m-' * 50)
print(f'\033[41m{'Até logo!':^50}')
print('\033[41m-' * 50)
print('\033[m')
'''
from time import sleep

c = ('\033[m', # 0 - sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;40m', # 6 - branco
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!', 1)