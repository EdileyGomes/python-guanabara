import random

num = random.randint(0, 5)

adv = int(input('Digite um Número de 0 a 5: '))

if num == adv:
    print('Parabéns, vca acertou!')
    exit()
else:
    print('Que pena, tente denovo')
