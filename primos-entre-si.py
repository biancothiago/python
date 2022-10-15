# Números primos entre si possuem apenas o número 1 como divisor em comum
def imprima(string):
    tam = len(string)
    print('-' * tam)
    print(string)
    print('-' * tam)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

divisores1 = list() 
for divisor in range(1, n1+1):
    resto = n1 % divisor
    if resto == 0:
        divisores1.append(divisor)

divisores2 = list()
for divisor in range(1, n2+1):
    resto = n2 % divisor
    if resto == 0:
        divisores2.append(divisor)

cont = 0
for num in divisores1:
    if num in divisores2:
        cont += 1
        if cont >= 2:
            imprima('- NÃO são números primos entre si.')
            break
if cont == 1:
    imprima('SÃO números primos entre si!')
