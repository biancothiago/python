from random import choice, randint

aposta = []
total = int(input('Informe o número de apostas desejada: '))
for i in range(0, total):
    for c in range(0, 6):
        while True:
            n = randint(1, 61)
            if n not in aposta:
                aposta.append(n)
                break
            else:
                continue
    print(f'* {i+1:>2}º JOGO: ', end='')
    for n in aposta:
        print(f'{n:<2}', end=' ')
    print()
    aposta.clear()
