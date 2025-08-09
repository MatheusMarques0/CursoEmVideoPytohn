num1 = (int(input('DIgite um número para descobrir seu fatorial: ')))
total = num1

while num1 > 1:
    total = total * (num1 - 1)
    num1 -= 1
print(total)