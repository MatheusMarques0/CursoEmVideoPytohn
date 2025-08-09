numero = ('zero' ,'um', 'dois', 'tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
          'treze','quatorze', 'quinze', 'dezesseis', 'dezesete','dezoito','dezenove','vinte')

pick = int((input('Digite um número entre 0 e 20: ')))
while pick < 0 or pick > 20:
    pick = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numero[pick]}')