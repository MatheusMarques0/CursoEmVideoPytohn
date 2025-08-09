#não é possível fazer só com o video da aula 19
import random
from time import sleep
from operator import itemgetter #***
jogo = {'Jogador1': random.randint(1, 6),
        'Jogador2': random.randint(1, 6),
        'Jogador3': random.randint(1, 6),
        'Jogador4': random.randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #***
print('-=' * 18)
print('  === RANKING DOS JOGADORES ===')
for i, v in enumerate(ranking):
    print(f'    {i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)