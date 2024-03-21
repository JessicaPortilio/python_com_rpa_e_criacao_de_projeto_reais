nome = input("Digite seu nome: \n")

print("\nO seu nome é: " + nome)

"""
Solicita ao usuário que insira seu nome e duas notas, calcula a média dessas notas e, 
em seguida, imprime uma mensagem contendo o nome do aluno e a média calculada. 

Vamos analisar cada parte do código:

    nome = input("Digite seu nome"): Solicita ao usuário que digite seu nome e 
    armazena o valor inserido na variável nome.

    nota1 = float(input("Digite a nota 1")): Solicita ao usuário que digite a 
    primeira nota, converte o valor inserido para um número de ponto flutuante usando 
    float(), e armazena o resultado na variável nota1.

    nota2 = float(input("Digite a nota 2")): Semelhante à linha anterior, solicita ao 
    usuário que digite a segunda nota, converte o valor inserido para um número de ponto 
    flutuante e armazena o resultado na variável nota2.

    media = (nota1 + nota2) / 2: Calcula a média das duas notas somando nota1 e nota2, e dividindo 
    o resultado por 2. A média é armazenada na variável media.

    print("Aluno ", nome, " Média: ", media): Imprime uma mensagem formatada contendo o nome do 
    aluno e a média calculada. A função print() pode receber vários argumentos separados 
    por vírgulas, e imprimirá cada um deles sequencialmente, separados por um espaço. 
    
    O resultado final combina os valores das variáveis nome e media com as strings 
    literais para criar a saída completa.

"""

nome = input("Digite seu nome: \n")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print("\nAluno:", nome, " Média:", media)

"""

Exercício: Tabuada Personalizada

Escreva um programa que solicite ao usuário um número inteiro e exiba a tabuada desse número, do 1 ao 10.

Entrada:

    Um número inteiro n, representando o número do qual você deseja ver a tabuada.

Saída:

    O programa deve imprimir dez linhas, mostrando o resultado da multiplicação do 
    número digitado com os números de 1 a 10, no formato n * i = resultado, onde n é o número 
    digitado pelo usuário e i varia de 1 a 10.

Exemplo de Entrada:

A tabuada de qual número deseja ver 5


Exemplo de Saída:

5  * 1 =  5
5  * 2 =  10
5  * 3 =  15
5  * 4 =  20
5  * 5 =  25
5  * 6 =  30
5  * 7 =  35
5  * 8 =  40
5  * 9 =  45
5  * 10 =  50


"""

#Tabuada

nDigitado = int(input("A tabuada de qual número você deseja ver? "))

print(nDigitado, "* 1 =", nDigitado * 1)
print(nDigitado, "* 2 =", nDigitado * 2)
print(nDigitado, "* 3 =", nDigitado * 3)
print(nDigitado, "* 4 =", nDigitado * 4)
print(nDigitado, "* 5 =", nDigitado * 5)
print(nDigitado, "* 6 =", nDigitado * 6)
print(nDigitado, "* 7 =", nDigitado * 7)
print(nDigitado, "* 8 =", nDigitado * 8)
print(nDigitado, "* 9 =", nDigitado * 9)
print(nDigitado, "* 10 =", nDigitado * 10)


"""

Exercício

Crie um algoritmo que solicite o ano de nascimento do usuário e 
com base no ano corrente imprima a idade

"""

ano_atual = 2024
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

print("Sua idade é:", idade)