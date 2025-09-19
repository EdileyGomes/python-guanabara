num = int(input('Digite um número inteiro para tabuada: '))

cont = 0

while cont < 10:
    cont = cont + 1
    print(f'{num} X {cont:2} = {num * cont}')