import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Digite o terceiro aluno: '))
aluno4 = str(input('Digite o quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)
print('O aluno sorteado foi {}'.format(escolhido))
