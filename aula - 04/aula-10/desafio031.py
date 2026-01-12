km = float(input('Qual a distância da viagem?: '))

if km <= 200:
    preco = km * 0.50

    print(f'A sua viagem tem {km}KM. A sua passagem vai custar R${preco:.2f}')
elif km > 200:
    preco = km * 0.45

    print(f'A sua viagem tem {km}. A passagem vai custar R${preco:.2f}')