Jogador = dict()
Partidas = list()
total = 0
Jogador['Nome'] = str(input('Nome do Jogador: '))
qtd = int(input(f'Quantas partidas {Jogador['Nome']} jogou? '))
for n in range(qtd):
    Partidas.append(int(input(f'Quantos gols na partida {n + 1}? ')))
    total += Partidas[n]
Jogador['Goals'] = Partidas
Jogador['Total'] = total
print('-=' * 30)
print(Jogador)
print('-=' * 30)
for k, v in Jogador.items():
    print(f'{k} do jogador: {v}')
print('-=' * 30)
print(f'O jogador {Jogador['Nome']} jogou {qtd} partidas.')
for p in range(qtd):
    print(f'==> Na partida {p + 1}, fez {Jogador['Goals'][p]} goals.')
print(f'Foi um total de {total} partidas.')