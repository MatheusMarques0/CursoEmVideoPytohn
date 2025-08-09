#metodo normal
#co = float(input('Digite o comprimento do cateto oposto: '))
#ca = float(input('o comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

#metodo com import
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai ser {:.2f}'.format(hi))