num = (int(input('Digite um valor: ')), int(input('Digite um outro valor: ')), int(input('Digite um outro valor: ')), int(input('Digite um outro valor: ')) )
nove = 0
tres = 0
pares = ''
for c in num:
    if c == 9:
        nove += 1
    if c == 3:
        tres = num.index(c) + 1
    if c % 2 == 0:
        pares += ' ' + str(c)

print(f'O 9 apareceu {nove} vezes')
print(f'O três apareceu primeiramente na posição {tres}')
print(f'Os números pares são:{pares}')