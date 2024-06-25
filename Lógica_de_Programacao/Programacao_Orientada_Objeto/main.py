from Manipulador_de_frase import ManipuladorDeFrase

def menu():
    """
    Exibe o menu de opções para o usuário, permitindo que ele escolha diferentes operações de formatação.
    O programa continua rodando até que o usuário escolha sair.
    """
    
    print("\nBem-vindo ao Manipulador de Frase!")

    frase = input("Por favor, digite uma frase: ")
    manipulador = ManipuladorDeFrase(frase)
    
    while True:
        print("\nEscolha uma opção para formatar a sua frase:")
        print("1. Converter para maiúsculas")
        print("2. Converter para minúsculas")
        print("3. Deixar a primeira letra da frase Maiúscula")
        print("4. Converter para o formato título")
        print("5. Contar vogais")
        print("6. Contar consoantes")
        print("7. Contar letra 'l' de deixe seu like")
        print("8. Pesquisar palavra")
        print("9. Substituir palavra")
        print("10. Reverter frase")
        print("11. Contar palavras")
        print("12. Mostrar frase atual")
        print("13. Sair")

        escolha = input("\nDigite o número da sua escolha: ")
        
        if escolha == "1":
            manipulador.em_maiusculas()
        elif escolha == "2":
            manipulador.em_minusculas()
        elif escolha == "3":
            manipulador.primeiraLetraMaiuscula()
        elif escolha == "4":
            manipulador.em_formato_titulo()
        elif escolha == "5":
            print(f"Total de vogais: {manipulador.contar_vogais()}")
        elif escolha == "6":
            print(f"Total de consoantes: {manipulador.contar_consoantes()}")
        elif escolha == "7":
            print(f"Total de ocorrências da letra 'l': {manipulador.contar_letra_l_de_like()}")
        elif escolha == "8":
            palavra = input("Digite a palavra que você quer pesquisar: ")
            contagem = manipulador.procurar_palavra(palavra)
            if contagem > 0:
                print(f"A palavra '{palavra}' aparece {contagem} vez(es) na frase.")
            else:
                print(f"A palavra '{palavra}' não foi encontrada na frase.")
        elif escolha == "9":
            palavra_antiga = input("Digite a palavra que você quer substituir: ")
            palavra_nova = input("Digite a nova palavra: ")
            manipulador.substituir_palavra(palavra_antiga, palavra_nova)
            print(f"Palavra '{palavra_antiga}' foi substituída por '{palavra_nova}'")
        elif escolha == "10":
            manipulador.reverter_frase()
        elif escolha == "11":
            print(f"Total de palavras na frase: {manipulador.contar_palavras()}")
        elif escolha == "12":
            print("\nFrase atual:", manipulador.obter_frase())
            continue
        elif escolha == "13":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Escolha inválida. Tente novamente.")

        print("Frase atual:", manipulador.obter_frase())

if __name__ == "__main__":
    menu()