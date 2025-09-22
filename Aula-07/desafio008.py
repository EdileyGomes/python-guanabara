import emoji

n =int(input(emoji.emojize('Olá, mundo 🌎: ', language='alias')))

print(n)


num = float(input('Digite o valor em metros: '))

cm = num * 100
mm = num * 1000

print(f'CM: {cm:.1f} \nMM: {mm}')