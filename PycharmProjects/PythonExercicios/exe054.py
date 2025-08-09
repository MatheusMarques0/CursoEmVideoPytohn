young = 0
old = 0

for n in range(1, 8):
    num = int(input('Em qua ano a {}° pessoa nasceu? '.format(n)))
    if (2025 - num) > 18:
        old += 1
    else:
        young += 1

print('\033[33m{}\033[m pessoas são maiores de idade'.format(old))
print('\033[33m{}\033[m pessoas são menores de idade'.format(young))