from math import hypot

cat_oposto = float(input('Digite o cateto oposto: '))
cat_adjacente = float(input('Digite o cateto adjacente: '))

hipotenusa = hypot(cat_oposto, cat_adjacente)
print(f'Se o cateto oposto é {cat_oposto}, e o cateto adjacente é {cat_adjacente}, logo a hipotenusa é {hipotenusa}')