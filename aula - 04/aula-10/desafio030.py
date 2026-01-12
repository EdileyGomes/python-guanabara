num = int(input('Digite um número, e eu vou falar se ele é ímpar ou par!: '))

impar = num % 2
if impar == 1:
    print('é impar')
    exit()
else:
    print('É, par')