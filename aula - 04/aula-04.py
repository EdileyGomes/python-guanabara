print ('Olá, Mundo!')

print(7 + 4)
print('7'+'4')

print('olá, Mundo!')
nome = 'Ediley'
idade = '19'
peso =  63.4

print(f'Seu nome é, {nome}, você tem {idade}, e tem {peso}Kg')
print('-=*='* 20)

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

print('-=*='* 20)

imc = peso / (altura * altura)
print(f'Olá, {nome}! Você tem {idade} anos, sua altura é {altura}, e você pesa {peso}, logo seu IMC é {imc}')