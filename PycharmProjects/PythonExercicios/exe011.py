print("cada 2 metros quadrados de parede precisam de 1 litro de tinta para ser pintado \n")

parede1 = float(input('Largura da parede: '))
parede2 = float(input('Altura da parede: '))
area = parede1 * parede2
tinta = area / 2

print("A sua parede tem a dimensão de {} x {} e sua área é de {} metros quadrados".format(parede1, parede2, area))
print('Para pintar essa parede, você precisará de {} litros de tinta'.format(tinta))