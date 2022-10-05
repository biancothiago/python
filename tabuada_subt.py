for tab in range(1, 11):
    print(f'TABUADA DO {tab}:')
    for c in range(1, 21):
        resultado_soma = tab + c
        print(f'{resultado_soma:<2} - {tab:>2} = {resultado_soma - tab}')
    print('-' * 14)  