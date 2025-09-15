n = float(input('Digite um valor: '))
print(n)

def chamada():
    num = int(input('Digite um valor novamente!: '))

if type(n) == float or type(n) == bool:
    print('Booleano ou float')
    if n == 23:
        chamada()


else:
    print('Vai corinthians')