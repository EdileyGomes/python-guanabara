from datetime import date

ano = int(input('Qual ano quer análisar??? '))

if ano == 0:
    ano = date.today().year
    print(f'O ANO É {ano}')
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é BISSEXTO')
    else:
        print('Não é BISSEXTO')