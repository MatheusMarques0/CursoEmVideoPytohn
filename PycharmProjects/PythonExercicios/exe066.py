n =0
s =0
total = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    total += 1

print(f'O total de número é {total} e a soma vale {s}')