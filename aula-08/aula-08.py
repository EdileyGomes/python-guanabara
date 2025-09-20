import math

num = int(input('Digite um número: '))

semmath = num ** (1/2)
raiz =  math.sqrt(num)

print(f'Esse é a raiz quadrada do valor que você digitou sem usar a biblioteca Math: {semmath}')
print(f'Esse é a raiz quadrada do valor que você digitou usando a biblioteca Math: {raiz}')
