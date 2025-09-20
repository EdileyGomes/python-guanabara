altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

mquadrado = altura * largura

tinta = mquadrado / 2
print(f'Você tem uma parede de {altura} de altura, e {largura} de largura. Isso em m² da {mquadrado}!\nCom um rendimento de 2m² por litro de tinta, da pra pintar {tinta:.2f}m²!')