from random import randint
import time

print('-=-'* 50 )
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('-=-'* 50 )

num = randint(0, 5)

numadv = int(input('Em que numero eu pensei? '))


if num == numadv:
    print('PROCESSANDO...')
    time.sleep(2)
    print(f'Eu pensei no numero {num}. Você acertou!')
else:
    print('PROCESSANDO...')
    time.sleep(2)
    print(f'Tente Novamente... Você errou, pensei no número {num}')


