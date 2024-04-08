"""
Exercício: Calculadora Simples

Desenvolva uma calculadora simples que permite ao usuário realizar
operações básicas de adição, subtração, multiplicação e divisão

Objetivos:
    Mostrar um Menu ao Usuário:
        - A calculadora deve exibir um menu com cinco opções:
            - adição
            - subtração
            - multiplicação
            - divisão
            - sair
        
        O usuário deve ser capaz de selecionar a operação
        desejada através da entrada de um número
    Receber Dois Números:
        - Após selecionar a operação, o usuário deve inserir
        dois números que serão utilizados na operação.
    
    Realizar a Operação Selecionada:
        - A calculadora deve realizar a operação selecionada
        com os números inseridos e exibir o resultado

    Repetir ou Encerrar:
        - Após cada operação, o menu deve ser exibindo novamente,
        permitindo que o usuário realize outra operação ou saia do
        programa.
        - O programa deve continuar funcionando até que o 
        usuário escolha sair
    
"""

while True:
    print(
        "\nCalculadora Simples:"
        "\n1 - Adição"
        "\n2 - Subtração"
        "\n3 - Multiplicação"
        "\n4 - Divisão"
        "\n5 - Sair"
    )
    try:
        opcao = int(input('Escolha uma operação: '))
        if opcao == 5:
            print('Até mais!')
            break
        
        num1 = float(input('Informe o primeiro número: '))
        num2 = float(input('Informe o primeiro número: '))
        if opcao == 1:
            soma = num1 + num2
            print(f'Resultado: {soma:.2f}')
        elif opcao == 2:
            menos = num1 - num2
            print(f'Resultado: {menos:.2f}')
        elif opcao == 3:
            vezes = num1 * num2
            print(f'Resultado: {vezes:.2f}')
        elif opcao == 4:
            if num2 != 0:
                divisao = num1 / num2
                print(f'Resultado: {divisao:.2f}')
            else:
                print("Error: Divisão por zero.")    
        else:
            print('Operação inválida!')
    except ValueError :
        print("Entrada inválida. Por favor, insira um número válido.")
        