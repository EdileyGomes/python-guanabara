dias = int(input('Quantos dias ele foi alugado?: '))
kms = float(input("Quantos Km's foram rodados?: "))

ppd = dias * 60
ppkm = kms * 0.15

print(f'Você rodou com o carro {kms:.0F}km, por {dias} dias.\n'
      f'O total a pagar fica em R${ppkm + ppd:.2f}')
