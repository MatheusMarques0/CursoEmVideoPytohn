income = float(input('Qual o salário do Fulano? \n'))

if income > 1250.00:
    increase = income * 1.10
    print('O salário de {} foi aumentado para \033[31m{:.2f}\033[m'.format(income, increase))
else:
    increase2 = income * 1.15
    print('O salário de {} foi aumentado para \033[33m{:.2f}\033[m'.format(income, increase2))