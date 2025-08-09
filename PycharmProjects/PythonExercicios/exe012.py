num = float(input('Qual é o preço do produto? R$: '))
descontoNum = int(input('Qual é o desconto que você precisa? (1-100): '))
desconto = 100 - descontoNum

price = num * (desconto/100)

print('O produto que custava {}, na promoção com desconto de {}% vai custar R${}'.format(num, descontoNum, price))