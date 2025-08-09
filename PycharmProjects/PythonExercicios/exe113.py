#para aprender o que continue faz
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[EERO]: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[ERRO] por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsúario preferiu não digitar esse número')
            return 0
        else:
            return n

num = leiaint(('Digite um valor: '))
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {n2}')
