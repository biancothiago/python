from time import sleep

def mostrarCadastro():
    print('-' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-' * 40)
    arq = open('cadastro.txt', 'r', encoding='utf8')
    for linha in arq:
        dados = linha.split(';')
        dados[1] = dados[1].replace('\n', '')
        print(f'{dados[0]:<25}{dados[1]} anos')
    sleep(1.5)

def fazerCadastro():
    arq = open('cadastro.txt', 'a', encoding='utf8')
    nome = input('Nome: ')
    while True:
        idade = input('Idade: ')
        if idade.isnumeric():
            break
        else:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
    arq.write(f'{nome};{idade}\n')
    arq.close()
    print(f'Novo registro de {nome} adicionado.')
    sleep(1.5)

while True:
    print('-' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('-' * 40)
    print("""1 - Ver pessoas cadastradas
2 - Cadastrar nova Pessoa
3 - Sair do Sistema""")
    print('-' * 40)
    while True:
        op = int(input(">>> Sua Opção: "))
        if 1 <= op <= 3:
            break
        else:
            print('\033[31m* Opção inválida! Digite novamente.\033[m')

    if op == 1:
        mostrarCadastro()
    elif op == 2:
        fazerCadastro()
    else:
        print('-' * 40)
        print('*** FIM DO PROGRAMA. ***'.center(40))
        print('Volte Sempre!'.center(40))
        print('-' * 40)
        break
    
