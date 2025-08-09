import random
tentativas = 1
numero = random.randint(1, 10)
chute = int(input('Descubra o número que estou pensando! (1-10): '))
while chute != numero:
    chute = int(input('\033[31mO número que você escolheu estava errado! Tente novamente(1-10): \033[m'))
    tentativas += 1

print('Você acertou! o número de tentatiavs necessárias foram: {}'.format(tentativas))