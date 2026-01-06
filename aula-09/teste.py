nome = str(input("Qual é o seu nome completo?: ")).strip()
testsplit = nome.split()
print(f'Seu nome é {testsplit[0]}, e o seu último sobrenome é {testsplit[-1]}')
print(f'Olá {testsplit[0]}')