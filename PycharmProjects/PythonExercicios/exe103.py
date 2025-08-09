'''
def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    return print(f'O joador {nome} fez {gols} gol(s) no campeonato')

nomeJogador = str(input('Nome do jogador: '))
numGols = str(input('Número de Gols: '))
ficha(nomeJogador, numGols)
'''

def ficha(jog = '<desconhecido>', gol = 0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
    if n.strip() == '':
        ficha(gol=g)
    else:
        ficha(n, g)
