salario = float(input('Digite o salario do funcionario: '))

if salario <= 1250:
    salario = salario + (salario * 15 / 100)
    print(f'Seu salario foi aumentado para R${salario:.2f} reais')
else:
    salario = salario + (salario * 10 / 100)
    print(f'Seu salario foi aumentado para R${salario:.2f} reais')