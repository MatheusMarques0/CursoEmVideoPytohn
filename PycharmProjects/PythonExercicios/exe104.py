def leiaint(txt):
    valor = 0
    while txt.isnumeric() == False:
        txt = str(input('\033[31m[ERRO] Digite um valor inteiro: \033[m'))
    valor = int(txt)
    return valor
numero = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {numero} ')