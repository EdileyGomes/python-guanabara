from itertools import count

frase = 'Sla em Vídeo Python'
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase[9:14])

print(frase[:5])
print(frase[9:])
print(frase.count('o'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print(frase.count('o',))

for curso in frase:
    frase.replace('Android','Mandar')
    print(frase)
    print(frase.replace('Mandar', 'Python'))
    print(frase)
    print(frase.replace('Sla', 'Curso'))



frase2 = '   Aprenda Python  '
print(len(frase2))
frase2.strip()
frase2 = frase2.strip()
print(frase2)
print(len(frase2))

split_exp = frase2.split()
print(split_exp[1])


