percorrido = int(input('A quantidade de KMs percorridos: '))
days = int(input('Total de dias alugados: '))

payday = days * 60
payrun = percorrido * 0.15
total = payday + payrun

print('O total a pagar é de R${}'.format(total))