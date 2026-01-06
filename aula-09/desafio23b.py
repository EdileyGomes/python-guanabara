from random import randint

num = int(input('Informe um numero inteiro de 0 a 9999: '))

num = str(num)


print(f'Milhar: {num[0]}')
print(f'Centena: {num[1]}')
print(f'Dezena: {num[2]}')
print(f'Unidade: {num[3]}')


print('=*' * 50)
print('Agora Vamos mostrar esse mesmo teste usando o módulo *RANDOM*')
print('=*' * 50)

num2 = randint(0, 9999)
num2 = str(num2)

print(f'O número escolhido foi o {num2[0]} {num2[1]} {num2[2]} {num2[3]}')

print(f'Milhar: {num2[0]}')
print(f'Centena: {num2[1]}')
print(f'Dezena: {num2[2]}')
print(f'Unidade: {num2[3]}')


