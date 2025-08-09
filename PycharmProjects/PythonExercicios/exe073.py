times = ('Cruzeiro', 'Flamengo', 'Palmeiras','Red Bull Bragantino', 'Botafogo', 'Bahia', 'Mirassol', 'Fluminense','Atlético-MG','Internacional',
         'Corinthians','São Paulo', 'Ceará','Vitória','Vasco', 'Santos','Juventude','Fortaleza','Sport')

print(f'Os primeiros colocados do Campeonato Brasileiro de Futebol são: {times[0:5]}')
print(f'Os últimos 4 colocados da tabela são: {times[-5:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'\033[32mO Palmeiras está em {times.index('Palmeiras')}° Lugar\033[m')