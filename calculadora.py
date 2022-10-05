def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2


print(' CALCULADORA COM PYTHON '.center(40, '='))
print("""\nEscolha uma opção:
1 - Soma
2 - Divisão
3 - Multiplicação
4 - Divisão""")
while True:
    escolha = int(input('\n>>> Insira a opção: '))
    if 1 <= escolha <= 4:
        break
    else: 
        print('Opção Inválida. Digite novamente.')

n1 = int(input('\n- Digite o primeiro número: '))
n2 = int(input('- Digite o segundo número: '))
print()
print('*' * 17)

if escolha == 1:
    print(f'{n1} + {n2} = {adicao(n1, n2)}'.center(17))
elif escolha == 2:
    print(f'{n1} - {n2} = {subtracao(n1, n2)}'.center(17))
elif escolha == 3:
    print(f'{n1} x {n2} = {multiplicacao(n1, n2)}'.center(17))
elif escolha == 4:
    print(f'{n1} / {n2} = {divisao(n1, n2)}'.center(17))
print('*' * 17)