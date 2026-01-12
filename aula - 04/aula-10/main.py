nome = str(input("Digite seu nome: "))
if nome == "Gustavo":
    print(f'Olá, {nome}')

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media <= 5:
    print(f'A sua média foi {media}, então vou não passou de ano')
elif media >= 5 and media <= 6.9:
    print('Por pouco ein!!!')
elif media >= 7:
    print('Passou de ano')


print('Parabens' if media >= 8 else 'Estude mais')