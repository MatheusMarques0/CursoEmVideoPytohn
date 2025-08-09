name = str(input('Digite um nome: '))

name = name.lower()

if 'silva' in name:
    print('\033[1mVocê tem Silva no nome\033[m')
else:
    print("Você não tem Silva no nome")