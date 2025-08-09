tupla = ('PROGRAMAR', 'PYTHON', 'ESTUDAR', 'JAVA', 'CADERNO','CANETA',
         'BORRACHA','ESTOJO')

for c in tupla:
    vogais = ''
    for n in c:
        if n == 'A' or n == "E" or n == "I" or n == "O" or n == "U":
            vogais += " " + n
    print(f'A palavra {c} tem as vogais:{vogais}')