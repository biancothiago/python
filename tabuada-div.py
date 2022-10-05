for tab in range (1, 11):
    print(f'TABUADA DO {tab}:')
    for c in range (1, 11):
        resultado_mult = tab * c
        print(f'{resultado_mult:<2} ÷ {tab:>2} = {resultado_mult / tab:>2.0f}')
    print('-' * 14)  