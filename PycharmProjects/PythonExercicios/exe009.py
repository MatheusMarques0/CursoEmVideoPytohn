#pulei alguns exercícios por serem muito simples

num = int(input("Digite um número para ver sua tabuada: "))
print('\n')

n = 1
while n < 11:
    soma = n * num
    print('{} x {} = {}'.format(num, n, soma))
    n = n + 1