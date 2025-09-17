from curses.ascii import isalpha


def inicio ():
    n = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))

    def alternativa():
        alt = input('DESEJA CONTINUAR?\nDIGITE [S], PARA CONTINUAR;\nE DIGITE [N], PARA NÃO CONTINUAR!').upper()
        if alt == 'N':
            print('Paramos por aqui, Muito Obrigado, e volte sempre!')
        elif alt == 'S':
            print('OK, VAMOS CONTINUAR!!!')
            inicio()
        else:
            print('Não consegui entender... Pode digitar dnv?')
            alternativa()

    def somar():
        print(n + n2)

    def dividir():
        print(n / n2)

    def subi():
        print(n - n2)

    def multiplicar():
        print(n * n2)

    opcao = input('Abaixo deixo as opções do que deve fazer, para trabalhar com os números acima!:\n'
                  'SOMAR = +;\n'
                  'SUBTRAIR = -;\n'
                  'DIVIDIR = /;\n'
                  'MULTIPLICAR = X.\n'
                  'Digite sua escolha:').upper()

    if opcao == '+':
        somar()
        alternativa()

    elif opcao == '-':
        subi()
        alternativa()

    elif opcao == 'X':
        multiplicar()
        alternativa()

    else:
        dividir()
        alternativa()

inicio()