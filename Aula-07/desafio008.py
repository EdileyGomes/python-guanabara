from emoji import emojize

n2 = int(input(emojize('Olá, mundo 🌎: ', language='alias')))

n = int(input(emojize('Olá, mundo 🌎: ', language='alias')))

n3 = int(input(emojize('Olá, mundo 🌎', language='alias')))

n4 = int(input(emojize('Mais um EMOJI para a conta: 😎', language='alias')))

print(n, n2, n3)


num = float(input('Digite o valor em metros: '))

cm = num * 100
mm = num * 1000

print(f'CM: {cm:.1f} \nMM: {mm}')