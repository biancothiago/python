from time import sleep

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def outputFormatado(string):
    tam = len(string)
    print('*' * tam)
    print(string)
    print('*' * tam)

while True:
    print('\033[34m', end='')
    print(' CALCULADORA COM PYTHON '.center(40, '='))
    print('\033[m', end='')
    print("""\nEscolha uma opção:
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Sair""")
    while True:
        escolha = int(input('\n>>> Insira a opção: '))
        if 1 <= escolha <= 5:
            break
        else: 
            print('Opção Inválida. Digite novamente.')
    if escolha == 5:
        print('\n \033[32m--- FIM DO PROGRAMA, VOLTE SEMPRE! ---\033[m')
        break

    n1 = int(input('\n- Digite o primeiro número: '))
    n2 = int(input('- Digite o segundo número: '))
    print()

    if escolha == 1:
        output = f'{n1} + {n2} = {adicao(n1, n2)}'
        outputFormatado(output)
    elif escolha == 2:
        output = f'{n1} - {n2} = {subtracao(n1, n2)}'
        outputFormatado(output)
    elif escolha == 3:
        output = f'{n1} x {n2} = {multiplicacao(n1, n2)}'
        outputFormatado(output)
    elif escolha == 4:
        output = f'{n1} / {n2} = {divisao(n1, n2)}'
        outputFormatado(output)
    print()
    sleep(2)