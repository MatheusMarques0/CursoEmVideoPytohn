name = 'LOJA SUPER BARATÃO'
end = 'FIM DO PROGRAMA'
total = 0
over2k = 0
over2kQuant = 0
cheapest = 0
cheapestName = ''

print(f'{'':-^30}')
print(f'{name:^30}')
print(f'{'':-^30}')
while True:
    produto = str(input('Nome do produto: '))
    price = float(input('Preço: R$'))
    if cheapest == 0:
        cheapest = price
        cheapestName = produto
    total += price
    if price > 1000:
        over2k += 1
        over2kQuant += 1
    if price < cheapest:
        cheapest = price
        cheapestName = produto
    conf = str(input('Quer continuar? [S/N]: ')).upper()
    if conf == 'N':
        break

print(f'{end:-^30}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {over2kQuant} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {cheapestName} que custa R${cheapest}')