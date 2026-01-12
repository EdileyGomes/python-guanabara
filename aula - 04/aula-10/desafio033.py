num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite outro valor: '))

if num1 > num2 and num1 > num3:
    print(f'O número {num1}, é o maior!!!')
elif num2 > num3 and num2 > num1:
    print(f'O número {num2}, é o maior!!!')
else:
    print(f'O número {num3}, é o maior!!!')