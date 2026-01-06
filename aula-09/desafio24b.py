cidade = str(input('Digite o nome da cidade: ')).strip()
cidade = cidade.upper()

if cidade == 'SANTO':
    print('Sua cidade contem "SANTO", no nome!')
else:
    print('Você não nasceu numa cidade que contem "SANTO"')