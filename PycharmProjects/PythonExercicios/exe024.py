cidade = str(input('Digite o nome de uma cidade: '))

if cidade[0:5].lower() == 'santo':
    print('\033[1:33mA sua cidade começa com santo\033[m')
else:
    print('\033[4:37mA sua cidade não começa com santo\033[m')