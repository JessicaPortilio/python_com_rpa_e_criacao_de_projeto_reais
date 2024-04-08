"""
Exercício: Simulação de Caixa Eletrônico

Objetivo: Desenvolver um programa em python que simula as 
operações básicas de um caixa eletrônico. O usuário deve ser capaz de
verificar o saldo, depositar dinheiro, sacar dinheiro e sair do programa.

Requisitos:
    Verificar Saldo:
        - Ao escolher essa opção, o programa deve exibir o saldo atual da conta.
    
    Depositar Dinheiro:
        - O usuário deve ser capaz de inserir uma quantia para depositar na conta.
        - A quantia deve ser positiva.
        - Após um depósito bem-sucedido, o saldo da conta deve ser atualizado e uma
        mensagem de confirmação deve ser exibida.
    
    Secar Dinheiro:
        - O usuário deve ser capaz de inserir uma quantia para sacar da conta.
        - A quantia deve ser positiva e não deve exceder o saldo atual.
        - Após um saque bem-sucedido, o saldo da conta deve ser atualizado e uma mensagem de confirmação deve ser exibida.

    Sair:
        - O usuário deve ser capaz de sair do programa escolhendo essa opção.
    
    Validação de Entrada:
        - O programa deve lidar com entradas inválidas de forma adequada, exibindo mensagens de erro quando aplicável.
    
    Interface de Usuário:
        - O programa deve exibir um menu de opções para o usuário e permitir
        a seleção de ações a serem realizadas.
        - As opções do menu devem ser apresentadas em um loop, permitindo
        múltiplas operações até que o usuário escolha sair.

        Caixa Eletrônico
        1 - Verificar Saldo
        2 - Depositar Dinheiro
        3 - Sacar Dinheiro
        4 - Sair
        Escolha uma opção (1-4):

    Seldo Inicial:
        - A conta deve começar com um saldo inicial de R$ 1000.00

    Intruções:
        - Comece inicializando o saldo e entrando em um loop que apresente o menu de opções
        - 
"""

saldo = 1000.00 # Define o saldo inicial da conta

# Inicía um loop infinito que continuará até que o usuário escolha a opção de sair
while True:
    # Imprime as opções do menu disponível para o usuário
    print(
        "\nCaixa Eletrônico \n" 
        "1 - Verificar Saldo \n"
        "2 - Depositar Dinheiro \n"
        "3 - Sacar Dinheiro \n"
        "4 - Sair"
    )
    opcao = int(input("Escolha uma opção (1-4): ")) # Solicita que o usuário escolha uma opção

    # Verifica a opção escolhida pelo usuário e executa a ação correspondente
    if opcao == 1:
        print(f'\nO saldo da conta é: R$ {saldo:.2f}') # Imprime o saldo atual da conta
    elif opcao == 2:
        depositar = float(input('\nInforme a quantia a depositar: ')) # Solicita o valor do depósito
        if depositar > 0: # Verifica se o valor do depósito é positivo
            saldo += depositar # Adiciona o valor do depósito ao saldo

            print(f'\nDepósito de: R$ {depositar:.2f} realizado com sucesso!') # Confirma o depósito
        else:
            print(f'\nO valor a ser depositado negado: R$ {depositar:.2f}. Observação: O valor do deposito tem que ser positivo!') # Informa que o valor do depósito é inválido
    elif opcao == 3:
        sacar = float(input('\nInforme a quantia a sacar: ')) # Solicita o valor do saque
        if sacar > 0 and sacar <= saldo: # Verifica se o valor do saque é válido e se há saldo suficiente
            saldo -= sacar # Subtrai o valor do saque do saldo

            print(f'\nSaque de: R$ {sacar:.2f} realizado com sucesso!') # Confirma o saque
        else:
            print(f'\nValor de saque inválido ou saldo insuficiente!') # Informa que o valor do saque é inválido ou insuficiente
    elif opcao == 4:
        print(f'\nCaixa Eletrônico agradece a sua operação!') # Agradece o usuário e prepara-se para sair do loop
        break
    else:
        print(f'\nOpção inválido, digite o número de 1 ao 4!') # Informa ao usuário que ele escolheu um opção inválida e contiua o loop
        
