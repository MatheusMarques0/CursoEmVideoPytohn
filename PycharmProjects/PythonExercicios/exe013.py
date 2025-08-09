income = int(input("Qual é o salário do funcionário? R$: "))
aumentoNum = int(input("Qual é o aumento que o funcionário irá receber (1%-100%): "))
aumento = income + (income * (aumentoNum/100))

print('O funcionário que ganahva R${}, com {}% de aumento, passa a  receber R${}'.format(income, aumentoNum, aumento))