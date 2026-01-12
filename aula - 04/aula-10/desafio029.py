velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('Seu carro foi multado')
    print('Cada Km/H acima de 80 km/h, você vai ter que pagar 7.12 euros a mais!')

    velocidade2 = velocidade - 80
    multa = velocidade2 * 7.12

    print(f'A sua multa foi de R$ {multa:.2f}')
elif velocidade <= 80:
    print('Seu carro esta dentro da velocidade. Conduza com cuidade!!!')