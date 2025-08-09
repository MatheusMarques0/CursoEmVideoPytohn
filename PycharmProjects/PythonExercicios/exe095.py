'''
jogadores = list()
jogador = dict()
total = 0
t = 1
print('-' * 50)
while True:
    jogador[f'Player{t}'] = dict()
    jogador[f'Player{t}']['Name'] = str(input('Nome do Jogador: '))
    jogador[f'Player{t}']['Partidas'] = int(input(f'Quantas partidas {jogador[f'Player{t}']['Name']} jogou? '))
    jogador[f'Player{t}']['Total'] = 0
    jogador[f'Player{t}'][f'Goals'] = list()
    for n in range(jogador[f'Player{t}']['Partidas']):
        jogador[f'Player{t}'][f'Goals'].append(int(input(f'Quantos gols {jogador[f'Player{t}']['Name']} fez no {n+1} jogo? ')))
    jogador[f'Player{t}']['Total'] = sum(jogador[f'Player{t}'][f'Goals'])
    jogadores.append(jogador.copy())
    jogador.clear()
    ask = str(input('Quer continuar? [S/N]: ')).upper()
    if ask == "N":
        break
    t += 1
print('-=' * 27)
print(f'{'cod':<10}{'nome':<8}{'gols':>8}{'total':>15}')
print('-' * 50)
for n in range(len(jogadores)):
    print(f'{n + 1:<10}{jogadores[n][f'Player{n+1}']['Name']:<8}{f'':>3}{jogadores[n][f'Player{n+1}']['Goals']}{jogadores[n][f'Player{n+1}']['Total']:>7}')
while True:
    info = int(input('Mostrar dados de qual jogador? (999 para cancelar): '))
    if info == 999:
        break
    if info < 1 or info > len(jogadores):
        info = int(input('[ERRO] Digite um comando válido (999 para cancelar): '))
    print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[info -1][f'Player{info}']['Name']} ---')
    for j in range(jogadores[info - 1][f'Player{info}']['Partidas']):
        print(f'No jogo {j + 1} fez {jogadores[info - 1][f'Player{info}']['Goals'][j]} gols')
'''

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('[ERRO]! Rresponda apenas S ou N.')
    if resp == "N":
        break
print('-=' * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'[ERRO] não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')