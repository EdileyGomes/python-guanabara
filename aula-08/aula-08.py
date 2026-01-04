import math
import random
import datetime
import emoji

print(emoji.emojize("Olá mundo :smile:", language='alias'))
print(emoji.emojize("Eu amo Python :heart:", language='alias'))

print(math.factorial(3))


num = int(input('Digite um número: '))

semmath = num ** (1/2)
raiz =  math.floor(math.sqrt(num))

print(f'Esse é a raiz quadrada do valor que você digitou sem usar a biblioteca Math: {semmath}')
print(f'Esse é a raiz quadrada do valor que você digitou usando a biblioteca Math: {raiz}')

num = random.randint(1, 10)
print(num)





