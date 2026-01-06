import random

num = random.randint(0, 9999)

print(num)

numstr = str(num).zfill(4)
print(numstr)

print(f'Milhar {numstr[0]}')
print(f'Centena {numstr[1]}')
print(f'Dezena {numstr[2]}')
print(f'Unidade {numstr[3]}')