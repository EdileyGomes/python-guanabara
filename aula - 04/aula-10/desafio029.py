velocidade = int(input('Qual a velocidade do carro: '))

if velocidade > 80:
    velocidade = (velocidade - 80) * 7
    print(f'Sua Multa é de R${velocidade:.2f}! Diriga com mais cuidado')
elif velocidade <= 80:
    print('Você esta dentro do limite de velocidade. Parabéns!')