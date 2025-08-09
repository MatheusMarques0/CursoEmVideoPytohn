def moeda(num = 0,moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')

def aumentar(num, per=0, forma = True):
    if forma == False:
        aumento = num + num * (per /100)
        return aumento
    else:
        aumento = num +  num * (per / 100)
        return moeda(aumento)

def metade(num, forma = True):
    if forma == False:
        half = num / 2
        return half
    else:
        half = num / 2
        return moeda(half)

def dobro(num, forma = True):
    if forma == False:
        double = num * 2
        return double
    else:
        double = num * 2
        return moeda(double)

def diminuir(num, per=0, forma = True):
    if forma == False:
        less = num * (1 - per/100)
        return less
    else:
        less = num * (1 - per/100)
        return moeda(less)

def resumo(price = 0, mais = 0, menos = 0):
    print('-' * 40)
    print(f'{'RESUMO DO VALOR':^40}')
    print('-' * 40)
    print(f'{'Preço analisado':<8}: \t{moeda(price)}')
    print(f'{'Dobro do preço':<8}: \t{dobro(price)}')
    print(f'{'Metade do preço':<8}: \t{metade(price)}')
    print(f'{f'{mais}% de aumento':<8}: \t{aumentar(price, mais)}')
    print(f'{f'{menos}% de redução':<8}: \t{diminuir(price, menos)}')
    print('-' * 40)