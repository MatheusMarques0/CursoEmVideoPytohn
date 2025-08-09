def area(largura, comprimento):
    areas = largura * comprimento
    print(f'A área do terreno um {largura}x{comprimento} é {areas}m')

def lin():
    print('-' * 40)

lin()
num1 = float(input('Digite a largura do terreno: '))
num2 = float(input('Digite o comprimento do terreno: '))
lin()
area(num1, num2)