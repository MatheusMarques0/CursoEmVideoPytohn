import moeda

p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.moeda(p)} é \033[31m{moeda.metade(p, True)}\033[m')
print(f'O dobro de {moeda.moeda(p)} é \033[32m{moeda.dobro(p, True)}\033[m')
print(f'Aumentando em 10%, temos \033[31m{moeda.aumentar(p, 10, False)}\033[m')
print(f'Reduzindo em 13%, temos \033[31m{moeda.diminuir(p, 13, False)}\033[m')
