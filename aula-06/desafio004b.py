from cloudinit.sources.DataSourceOpenNebula import switch_user_cmd
n = 0
def inicio():
    print('-=*=' * 30)
    print('Banco PONCIANO')
    print('OPÇÕES: [1] - SALDO | [2] INFORMAÇÕES')
    n = int(input('Digite a opção: '))
inicio()
saldo = 2381

def saldodapessoa():
    print(f'O seu saldo é de {saldo} reais')

def informacoes():
    print('Sua conta é a 5923-X')




if n == 1:
    saldodapessoa()
    inicio()
elif n == 2:
    informacoes()
    inicio()
else:
    print('Inválido.')
    inicio()