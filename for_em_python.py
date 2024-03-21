#For laço de repetição
#Função range para imprimir os números inteiros de 1 a 10

#For - para
for numero in range(1, 11):
    
    print(numero)
    
"""
Explicação:

    Loop For com Range: A estrutura for é usada para criar um loop que 
    iterará sobre uma sequência de valores. A função range(1, 11) gera uma sequência 
    de números inteiros começando em 1 e terminando antes de 11.

    Corpo do Loop: Dentro do loop, há uma única instrução:
    
        Imprimir Número Atual: A função print(i) imprime o valor atual da variável de loop i.

    Execução do Loop: O loop será executado para cada valor de i na sequência gerada 
    por range(1, 11), o que significa que ele será executado 10 vezes, com i assumindo os 
    valores de 1 a 10, um de cada vez.


O código ilustra como usar um loop for com a função range para iterar sobre uma sequência 
de números inteiros, executando uma ação (neste caso, imprimir o número) para cada valor na 
sequência. É uma maneira comum de repetir uma ação para um número fixo de vezes em Python.

"""

# for - utilizando números
print()
for i in range(10, 0, -1):
    print(i)


# for - utilizando números
print()
for i in range(0, 11, 2):
    print(i)


print()
# Inicializando a variável para armazenar a soma
soma = 0

# Iterando de 1 a 10, de 2 em 2 (capturando apenas os números ímpares)
for i in range(1, 11, 2):
    print(f'Número impar atual: {i}')

    soma += i # Adicionando o número ímpar atual à soma

print(f'\nA soma dos números impares de 1 a 100 é: {soma}')

"""
Exercício: Multiplicação de Números

Objetivo: Escreva um programa que utilize um loop for 
para multiplicar os números de 1 a 5 e imprima 
o resultado de cada etapa e o resultado final.

Etapas:
    - Utilize um loop for para iterar pelos números de 1 a 5.
    - Multiplique cada número pelo resultado anterior (começando por 1)
    - Imprima o resultado de cada etapa.
    - Imprima o resultado final da multiplicação de todos os números.

Saída:
    Multiplicador por 1, o resultado parcial é 1
    ...

O resultado final da multiplicação de 1 a 5 é: 120

"""
resultado = 1
for i in range(1,6):
    resultado *= i
    print(f'Multiplicando por {i}, o resultado parcial é {resultado}')

print(f'O resultado final da multiplicação de 1 a 5 é: {resultado}')

"""
Exercícios: Soma de Números Pares

Objetivo: Escreva um programa que peça ao usuário um número
inteiro N e some todos os números pares de 1 até N, incluindo o próprio N (se for par)

Utilize um loop for para esta tarefa.

Etapas: 
    - Solicite ao usuário um número inteiro positivo N.
    - Utilize um loop for para iterar de 1 a N e some todos os números pares.
    - Imprima o resultado da soma.

Exemplo de Saída:
    Digite um número inteiro positivo: 10
    A soma dos números pares de 1 até 10 é: 30
"""

n = int(input('Informe um número inteiro: '))

soma_par = 0
for i in range(1, n+1):
    if i % 2 == 0:
        soma_par +=i

print(f'A soma dos números pares de 1 até {n} é: {soma_par}')


"""
Exercício: Tabela de Multiplicação

Objetivo: Escreva um programa que peça ao usuário um número inteiro positivo NN e exiba
a tabela de multiplicação para esse número, de 1 a 10. Utilizando um loop for
para está tarefa.

Etapas:
    - Solicite ao usuário um número inteiro positivo NN
    - Utilize um loop for para iterar de 1 a 10.
    - para cada iteração, multiplique o número N pelo valor da iteração e imprima o resultado.

Exemplo de Saída:
    Digite um número inteiro positivo para exibir a sua tabela de multiplicação: 5

"""

nn = int(input('Digite um número inteiro positivo para exibir a sua tabela de multiplicação: '))

for i in range(1,11):
    print(f'{nn} x {i} = {nn * i}')

print('Fim da tabela de multiplicação.')

"""
Exercício: Soma dos Quadrados

Objetivo: Escreva um programa que peça ao usuário um número inteiro positivo NN 
e calcule a soma dos quadrados de todos os números de 1 até NN. 
Utilize um loop for para esta tarefa.

Etapas:
    - Solicite ao usuário um número inteiro positivo NN.
    - Utilize um loop for para iterar de 1 a NN, calculando o quadrado
    de cada número e somando-o a uma variável.
    - Imprima o resultado da soma.

Exemplo de Saída:
    Digite um número inteiro positivo: 5
    Quadrado de 1: 1
    Quadrado de 2: 2
    Quadrado de 3: 9
    Quadrado de 4: 16
    Quadrado de 5: 25

    A Soma dos quadrados dos números de 1 até 5 é = 55
    

"""

num = int(input(f'Digite um número inteiro positivo:'))

result = 0
for i in range(1, n +1):
    print(f'Quadrado de {i}: {i**2}')
    result = result + (i**2)

print(f'A Soma dos quadrados dos números de 1 até {num} é = {result}')

lista = ["A", "B", "C", "D", "E"]

for item in lista:
    print(item)

    if item == "C":
        break

frutas = ['maça', 'banana', 'laranja']

for fruta in frutas:
    print(fruta)

numero = int(input('Digite um número: '))
for i in range(1, numero + 1):
    print(i)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(f'{numero}, é par')
    else:
        print(f'{numero}, é ímpar')


"""
Exercício: Lista de Compras

Objetivo: Use um loop for para iterar sobre uma lista de itens de compras
e imprimir cada item em um formato específico.

Instruções:
    1. Crie uma lista chamada itens_compra contendo alguns itens que
    você compraria em uma loja, por exemplo: ['maça', 'banana', 'cenoura', 'leite']
    2. Use um loop for para iterar sobre os itens da lista
    3. Para cada item na lista, imprima o item no seguinte formato:
    " Eu preciso comprar [item]"

"""

lista_de_compras = ['maça', 'banana', 'cenoura', 'leite']

for item in lista_de_compras:
    print(f'Eu preciso comprar {item}')


"""
Exercício: Estrelas Descendentes

Objetivo: Use um loop for para criar um padrão descendente de estrelas (*)
Comece com 5 estrelas na primeira linha e reduza uma estrela 
em cada linha subsequente até não restar nenhuma estrela.

Instruções:
    1. Use um loop para iterar de 5 a 0 
    (dica: pense sobre a função range() de maneira descendente)
    2. Em cada iteração do loop, imprima o número atual de estrelas 
    em uma única linha.

Após concluir o exercício, sua saída deve ser parecer com:
*****
****
***
**
*


"""

for i in range(5, 0, -1):
    print(i * '*')

"""
Exercício: Palavra com Mais de 4 Letras

Objetivo: Solicite ao usuário uma lista de palavras e, em seguida
    exiba apenas as palavras que têm mais de 4 letras.

Instruções:
    1. Peça ao usuário que insira palavras separadas por vírgula
    (por exemplo, ['casa', 'carro', 'sol', 'arvore'])
    2. Use um loop for para iterar sobre essa lista de palavras
    3. Dentro do loop, verifique o comprimento de cada palavra
    4. Se a palavra tiver mais de 4 letras, imprima-a.

Após concluir o exercício, se o usuário inser 'casa, carro, sol, árvore', a
saídade deve ser:

carro
árvore

"""

palavras = input('Insira palavras separadas por vírgula: ').split(',')

for palavra in palavras:
    if len(palavra) > 4:
        print(palavra)