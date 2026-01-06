nome = input('Digite seu nome completo: ').strip()

print(f'O nome digitado foi {nome}, e esse nome completo maiusculo fica {nome.upper()}')
print(f'O nome digitado foi {nome}, e em minusculo fica {nome.lower()}')

splitnome  = nome.split()
splitnome = len(splitnome[0])

print(f'O primeiro nome de {nome}, tem {splitnome} letras')
nome = nome.split()
print(f'E esse primeiro nome tem ({nome[0]}), {len(nome[0])} letras')

