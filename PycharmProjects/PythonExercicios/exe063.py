n = int(input('Digite uma posição da sequência fibonacci: '))
#passado = futuro - presente
#presente = futuro - passado
#futuro = presente + passado
x = n
presente = 1
passado = 0
futuro = 1
print(0)
while n > 1:
    futuro = presente + passado
    passado = presente
    presente = futuro
    n -= 1
    print(passado)
