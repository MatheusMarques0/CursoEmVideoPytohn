import moeda

p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.moeda(p)} é \033[31m{moeda.moeda(moeda.metade(p))}\033[m')
print(f'O dobro de {moeda.moeda(p)} é \033[32m{moeda.moeda(moeda.dobro(p))}\033[m')
print(f'Aumentando em 10%, temos \033[31m{moeda.moeda(moeda.aumentar(p, 10))}\033[m')
print(f'Reduzindo em 13%, temos \033[31m{moeda.moeda(moeda.diminuir(p, 13))}\033[m')
