nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.upper()
nome = nome.split()


if 'SILVA' in nome:
    print('Seu nome completo tem Silva')
else:
    print('Seu nome não tem Silva')