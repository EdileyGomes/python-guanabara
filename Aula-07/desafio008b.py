n = float(input('Digite um valor em metros!: '))

km = n * 0.001
hm = n * 0.01
dm = n * 0.1
dc = n * 10
cm = n * 100
mm = n * 1000

print(f'A metragem {n}, é igual a: \n'
      f'KM = {km}\n'
      f'HM = {hm}\n'
      f'DM = {dm:.2f}\n'
      f'DC = {dc}\n'
      f'CM = {cm}\n'
      f'MM = {mm}')

print(f'')