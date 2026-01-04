import random
print('_-==-' * 15)
a1 = input('Digite o primeiro aluno:')
a2 = input('Digite o número do segundo aluno: ')
a3 = input('Digite o número do terceiro aluno: ')
a4 = input('Digite o número do quarto aluno: ')

escl = random.choices((a4, a3, a2, a1))

print(f'Entre os alunos {a1}, {a2}, {a3}, {a4}, o escolhido foi o...\n'
              f'{escl}')