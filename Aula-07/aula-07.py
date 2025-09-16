a = 5 + 2
b = 5 - 2
c = 5 * 2
d = 5 / 2
e = 5 ** 2
f = 5 // 2
g = 5 % 2

print(a, b, c, d, e, f, g)
print(252**126)
print(18%2)
print(122%3)
print(int(81**(1/2)))
print(77**(1/2))

print(127**(1/3))
print('oi' * 5)
print('-=*=' * 30 )

nome = input('Qual é o seu nome?')
print('Prazer em te conhecer {:=^20}!'.format(nome))

num = int(input('Digite um Número!: '))
num2 = int(input('Digite outro número!: '))
s = num + num2
m = num * num2
d = num / num2
s = num - num2
print('A soma entre {} e {} vale {}'.format(num, num2, num2 + num ))
print('Logo a mutiplicação da {:=^10}, a divisão da {:.3f} e a subtração da {:=^10}!'.format(m, d, s))