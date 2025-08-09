'''
def fatorial(numero,show = False):
    c = 1
    if show == False:
        for f in range(numero, 0, -1):
            c *= f
        return print(f'{c}')
    elif show == True:
        for f in range(numero, 0, -1):
            c *= f
            if f == numero:
                print(f'{f} ', end='')
            else:
                print(f'x {f} ', end='')
        print(f'= {c}')

fatorial(5, show=True)
'''
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))
