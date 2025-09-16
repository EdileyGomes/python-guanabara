from tarfile import calc_chksums

salario = float(input('Digite o seu salário: '))

calc = (salario / 100) * 15
calcfinal = calc + salario

print(f'Com um aumento de 15% no salário, o funcionário que ganhava R${salario}, começara a ganhar R${calcfinal}')