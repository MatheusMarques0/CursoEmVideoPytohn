expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append('(')
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão está válida!')
else:
    print('A sua expressão está errada!')