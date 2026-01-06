sla = str(input('Digite uma frase: ')).strip().upper()
sla = sla.replace(' ', '')
contadordeletras = len(sla)

print('A frase digitada tem {} letras'.format(contadordeletras))
print(f'A Letra "A", aparece {sla.count("A")} vezes')
print(f'A primeira letra "A", apareceu na posição {sla.find("A")}')
print(f'A última letra apareceu na posição número {sla.rfind("A")}')