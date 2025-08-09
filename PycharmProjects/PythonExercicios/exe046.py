from time import sleep

print('contagem regressiva:')
for n in range(10, -1, -1):
    sleep(1)
    print(n)
print('\033[33mBUM!\033[m')