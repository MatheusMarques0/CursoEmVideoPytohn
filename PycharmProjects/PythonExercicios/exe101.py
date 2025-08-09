def voto(ano):
    from datetime import date

    atual = date.today().year
    idade = atual - ano
    if idade >= 18 and idade < 70:
        return print(f'com {idade} anos: OBRIGATÓRIO')
    elif idade >= 70:
        return print(f'com {idade} anos: OPCIONAL')
    else:
        return print(f'com {idade} anos: NEGADO')
print('-' * 20)
anoNascimento = int(input('Em que ano você nasceu? '))
voto(anoNascimento)