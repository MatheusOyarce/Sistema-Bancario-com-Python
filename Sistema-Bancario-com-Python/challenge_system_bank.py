# Opções
saldo = 0
deposito = 0
extrato = ''

# Regras
limite_saque = 500
numero_tentativas = 0

# Iteração do loop
opcao = -1

while opcao != 0:
    print(
    """
    ================================= Caixa Eletronico =================================

    Seja Bem vindo (a) ao caixa eletronico, Quais operações você gostaria de realizar ?:
    1) Saque.
    2) Deposito.
    3) Extrato.
    0) Sair.

    ====================================================================================
    """
    )

    opcao = int(input('Escolha uma das opções (1/2/3/0):'))

    # Opção Saque
    if opcao == 1:
        print('Você escolheu a opção Saque')

        valor_saque = float(input('Insira um valor para saque: '))
        
        if valor_saque > saldo:
            print(f'Saldo insuficiente.')
        elif valor_saque > limite_saque:
            print('Você excedeu seu limite para saque')
        elif numero_tentativas > 3:
            print('Você excedeu seu limite de tentativas de saque')
        elif valor_saque > 0:
            print (f'\nSacando {valor_saque:.2f}...')
            saldo -= valor_saque
            extrato += f'\nSaque: R$ {valor_saque:.2f}'
            numero_tentativas += 1
        else:
            print ('Operação falhou, tente novamente ...')

    # Opção Deposito
    if opcao == 2:
        print('Você escolheu a opção de Deposito')

        valor_deposito = float(input('Insira um valor para deposito: '))

        if valor_deposito > 0:
            print(f'Depositando R$: {valor_deposito} ...')
            saldo += valor_deposito
            extrato += f'\nDeposito: R$ {valor_deposito:.2f}'
        else:
            print('O valor informado é inválido.')
    
    # Opção Extrato
    if opcao == 3:
        print('\n================================= Extrato =================================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print (f'\nSaldo R$ {saldo:.2f}' )
        print ('===========================================================================')
    
    # Opção de Exit
    if opcao == 0:
        print('Operação cancelada, saindo ...')
        break