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
print()

"""
A diferença entre os loops while e for em Python (e na maioria das linguagens de programação) reside 
principalmente em como eles determinam a continuação do loop e como manipulam a iteração. 

Veja as principais diferenças:

Loop while

    Controle de Condição: O loop while continuará executando enquanto uma condição 
    especificada for avaliada como verdadeira (True).
    
    Incremento/Decremento Manual: Você geralmente precisa manipular manualmente a 
    variável de controle (por exemplo, incrementar ou decrementar) dentro do loop.
    
    Geralmente Usado Quando: A quantidade de iterações não é conhecida de antemão, e o loop 
    deve continuar com base em uma condição.

Exemplo:

count = 0
while count < 5:
    print(count)
    count += 1


Loop for

    Iteração sobre uma Sequência: O loop for é usado para iterar sobre uma 
    sequência (lista, tupla, dicionário, conjunto ou string), percorrendo cada 
    elemento da sequência.
    
    Incremento/Decremento Automático: O controle do loop é gerenciado automaticamente 
    pelo próprio loop for.
    
    Geralmente Usado Quando: Você sabe o número de iterações de antemão, ou você 
    está iterando sobre uma sequência.

Exemplo:

for i in range(5):
    print(i)

Em resumo, o loop while é geralmente usado quando você quer continuar o 
loop com base em uma condição, e você pode não saber quantas vezes o loop precisa ser 
executado. O loop for, por outro lado, é mais comum quando você sabe quantas vezes quer 
iterar ou quando está trabalhando diretamente com uma sequência de elementos.

"""
print()

#for - utilizando números

for i in range(10, 0, -1):
    
    print(i)
    
"""
Explicação:

    Loop For com Range: A estrutura for é usada para criar um loop que iterará 
    sobre uma sequência de valores. A função range(10, 0, -1) gera uma sequência de 
    números inteiros começando em 10 e terminando antes de 0, decrementando 1 a cada passo.
    
        O primeiro argumento 10 é o valor inicial.
        
        O segundo argumento 0 é o valor final (exclusivo).
        
        O terceiro argumento -1 é o passo, ou seja, a quantidade pela qual o 
        valor é alterado a cada iteração (neste caso, decrementado em 1).

    Corpo do Loop: Dentro do loop, há uma única instrução:
    
        Imprimir Número Atual: A função print(i) imprime o valor atual da variável de loop i.

    Execução do Loop: O loop será executado para cada valor de i na sequência gerada por 
    range(10, 0, -1), o que significa que ele será executado 10 vezes, com i assumindo os 
    valores de 10 a 1, um de cada vez, em ordem decrescente.


O código ilustra como usar um loop for com a função range para iterar sobre uma 
sequência de números inteiros em ordem decrescente, executando uma ação (neste caso, 
imprimir o número) para cada valor na sequência.
"""

#for - utilizando números

#De 1 a 10 com um passo de 2.

#Começa em 2, termina antes de 12, com um passo de 2
for i in range(2, 12, 2):
    
    print(i)
# Inicializando a variável para armazenar a soma
soma = 0

# Iterando de 1 a 10, de 2 em 2 (capturando apenas os números ímpares)
for i in range(1, 11, 2):
    
    print(f"Número ímpar atual: {i}")
    
    #soma = soma + i
    soma += i  # Adicionando o número ímpar atual à soma

print(f"\nA soma dos números ímpares de 1 a 10 é: {soma}")
    

"""
Exercício: Multiplicação de Números

Objetivo: Escreva um programa que utilize um loop for para multiplicar os 
números de 1 a 5 e imprima o resultado de cada etapa e o resultado final.

Etapas:

    - Utilize um loop for para iterar pelos números de 1 a 5.
    - Multiplique cada número pelo resultado anterior (começando por 1).
    - Imprima o resultado de cada etapa.
    - Imprima o resultado final da multiplicação de todos os números.

Saída:

Multiplicando por 1, o resultado parcial é 1
Multiplicando por 2, o resultado parcial é 2
Multiplicando por 3, o resultado parcial é 6
Multiplicando por 4, o resultado parcial é 24
Multiplicando por 5, o resultado parcial é 120
"""

# Inicializando a variável resultado com 1
resultado = 1

# Utilizando um loop for para iterar pelos números de 1 a 5
for numero in range(1, 6):
    
    # Multiplicando o resultado pelo número atual
    #resultado = resultado * numero
    resultado *= numero 
    
    print(f"Multiplicando por {numero}, o resultado parcial é {resultado}")

print(f"O resultado final da multiplicação de 1 a 5 é: {resultado}")

"""
Exercício: Soma de Números Pares

Objetivo: Escreva um programa que peça ao usuário um número 
inteiro N e some todos os números pares de 1 até N, incluindo o próprio N (se for par). 

Utilize um loop for para esta tarefa.

Etapas:

    - Solicite ao usuário um número inteiro positivo N.
    - Utilize um loop for para iterar de 1 a N e some todos os números pares.
    - Imprima o resultado da soma.


Exemplo de Saída:

Digite um número inteiro positivo: 10
A soma dos números pares de 1 até 10 é: 30
"""

# Solicitando ao usuário o número
N = int(input("Digite um número inteiro positivo: "))

# Inicializando a variável para armazenar a soma
soma_pares = 0

# Utilizando um loop for para somar os números pares de 1 até N
for i in range(1, N + 1):
    
    # Verificando se o número é par
    if i % 2 == 0: 
        
        #Imprime cada etapa
        print(f"Número: {i} + {soma_pares} = {i+soma_pares}")
        
        soma_pares += i
        
        

# Imprimindo o resultado
print(f"A soma dos números pares de 1 até {N} é: {soma_pares}")

"""
Exercício: Tabela de Multiplicação

Objetivo: Escreva um programa que peça ao usuário um número inteiro positivo NN e 
exiba a tabela de multiplicação para esse número, de 1 a 10. Utilize um loop for para esta tarefa.

Etapas:

    - Solicite ao usuário um número inteiro positivo NN.
    - Utilize um loop for para iterar de 1 a 10.
    - Para cada iteração, multiplique o número NN pelo valor da iteração e imprima o resultado.
    
Exemplo de Saída:

Digite um número inteiro positivo para exibir a sua tabela de multiplicação: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Fim da tabela de multiplicação.

"""

# Solicitando ao usuário o número para criar a tabela de multiplicação
N = int(input("Digite um número inteiro positivo para exibir a sua tabela de multiplicação: "))

# Utilizando um loop for para criar a tabela de multiplicação de 1 a 10
for i in range(1, 11):
    
    resultado = N * i # Calculando o resultado da multiplicação
    
    print(f"{N} x {i} = {resultado}") # Imprimindo o resultado

# Imprimindo uma linha final
print("Fim da tabela de multiplicação.")


"""
Exercício: Soma dos Quadrados

Objetivo: Escreva um programa que peça ao usuário um número inteiro positivo NN e 
calcule a soma dos quadrados de todos os números inteiros de 1 até NN. Utilize um loop 
for para esta tarefa.

Etapas:

    - Solicite ao usuário um número inteiro positivo NN.
    
    - Utilize um loop for para iterar de 1 a NN, calculando o quadrado 
    de cada número e somando-o a uma variável.
    
    - Imprima o resultado da soma.

Exemplo de Saída:

Digite um número inteiro positivo: 5
Quadrado de 1: 1
Quadrado de 2: 4
Quadrado de 3: 9
Quadrado de 4: 16
Quadrado de 5: 25
A soma dos quadrados dos números de 1 até 5 é: 55


"""

# Solicitando ao usuário o número
N = int(input("Digite um número inteiro positivo: "))

# Inicializando a variável para armazenar a soma dos quadrados
soma_quadrados = 0

# Utilizando um loop for para somar os quadrados de 1 até N
for i in range(1, N + 1):
    quadrado = i**2 # Calculando o quadrado do número
    print(f"Quadrado de {i}: {quadrado}") # Imprimindo o quadrado do número
    soma_quadrados += quadrado # Adicionando o quadrado à soma

# Imprimindo o resultado
print(f"A soma dos quadrados dos números de 1 até {N} é: {soma_quadrados}")

#For - Utilizando Strings
#loop for para iterar sobre uma lista de caracteres alfabéticos, 
#imprimindo cada item da lista até encontrar o caractere "C"

#For = Para

lista = ["A", "B", "C", "D", "E"]

for item in lista:
    
    print(item)
    
    if item == "C":
        
        break
        
"""
Explicação:

    Definindo a Lista: A variável lista é inicializada com uma lista de 
    caracteres alfabéticos ["A", "B", "C", "D", "E"].

    Loop For: A estrutura for é usada para criar um loop que iterará sobre 
    cada elemento da lista lista.

    Corpo do Loop: Dentro do loop, há duas instruções:
    
        Imprimir Item Atual: A função print(item) imprime o valor atual da 
        variável de loop item.
        
        Condição de Parada (if): A instrução if verifica se o valor atual 
        de item é igual a "C". Se essa condição for verdadeira, a instrução break 
        é executada, interrompendo o loop imediatamente.

    Execução do Loop: Veja como ele se comporta em cada iteração:
    
        Iteração 1: item é "A", é impresso, e o loop continua.
        
        Iteração 2: item é "B", é impresso, e o loop continua.
        
        Iteração 3: item é "C", é impresso, e então a condição item == "C" é 
        verdadeira, o que aciona a instrução break.
        
        O loop é interrompido, e o programa termina sua execução.

O código demonstra como usar um loop for juntamente com uma instrução condicional 
if e a palavra-chave break para controlar a execução do loop. Neste exemplo, o loop é interrompido 
quando o item "C" é encontrado na lista.
"""
print()

#For - Utilizando Strings

#For = Para

# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    
    print(fruta)

numero = int(input("Digite um número: "))

for i in range(1, numero + 1):
    
    print(i)


#For Utilizando If e Else
#Verifica se é par ou ímpar e imprime uma mensagem correspondente. 
    
# Iterando sobre uma lista de números e aplicando uma condição
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicia um loop 'for' para iterar através de cada número na lista 'numeros'
for numero in numeros:
    
    # Verifica se o número atual é par usando o operador de módulo (%), que retorna o resto da divisão por 2
    if numero % 2 == 0:
        
        # Se o número for par, imprime a mensagem indicando que o número é par
        print(numero, "é par")
        
    else:
        
        # Se o número não for par (ou seja, ímpar), imprime a mensagem indicando que o número é ímpar
        print(numero, "é ímpar")

        
        
"""
Explicação:

    Definindo a Lista: A variável numeros é inicializada com uma 
    lista de números inteiros de 1 a 10.

    Loop For: A estrutura for é usada para criar um loop que iterará 
    sobre cada elemento da lista numeros.

    Corpo do Loop: Dentro do loop, há uma estrutura condicional if-else:
    
        Verificar se é Par: A instrução if numero % 2 == 0 verifica 
        se o valor atual de numero é par (ou seja, divisível por 2 sem resto). 
        
        Se for verdade, o programa imprime "<numero> é par".
        
        Caso Contrário, é Ímpar: Se a condição acima não for verdadeira, 
        o programa entra na cláusula else e imprime "<numero> é ímpar".

    Execução do Loop: O loop será executado para cada valor de numero na 
    lista numeros, verificando se cada número é par ou ímpar e imprimindo 
    a mensagem correspondente.


O código ilustra como usar um loop for juntamente com uma instrução 
condicional if-else para iterar sobre uma lista de números, executando uma 
verificação e imprimindo uma mensagem correspondente para cada número na lista.
"""
print()

"""
Exercício: Lista de Compras

Objetivo: Use um loop for para iterar sobre uma lista de itens de 
compras e imprimir cada item em um formato específico.

Instruções:

    1. Crie uma lista chamada itens_compra contendo alguns itens que 
    você compraria em uma loja, por exemplo: ["maçã", "banana", "cenoura", "leite"].
    
    2. Use um loop for para iterar sobre os itens da lista.
    3. Para cada item na lista, imprima o item no seguinte formato: "Eu preciso comprar [item]".

Após concluir o exercício, sua saída deve se parecer com:

Eu preciso comprar maçã
Eu preciso comprar banana
Eu preciso comprar cenoura
Eu preciso comprar leite

"""

# Criando uma lista chamada 'itens_compra' contendo quatro itens (strings).
itens_compra = ["maçã", "banana", "cenoura", "leite"]

# Iniciando um loop 'for' que irá iterar sobre cada 'item' na lista 'itens_compra'.
for item in itens_compra:
    
    # Imprimindo uma frase com o item atual da iteração.
    # A função 'print' automaticamente insere um espaço entre os argumentos.
    print("Eu preciso comprar", item)



"""
Exercício: Estrelas Descendentes

Objetivo: Use um loop for para criar um padrão descendente 
de estrelas (*). Comece com 5 estrelas na primeira linha e reduza 
uma estrela em cada linha subsequente até não restar nenhuma estrela.

Instruções:

    1. Use um loop for para iterar de 5 a 0 (dica: pense sobre 
    a função range() de maneira descendente).
    
    2. Em cada iteração do loop, imprima o número atual 
    de estrelas em uma única linha.

Após concluir o exercício, sua saída deve se parecer com:

*****
****
***
**
*


"""

# Itera sobre os números de 5 a 1 (inclusive) em ordem descendente
for i in range(5, 0, -1):
    
    # Imprime 'i' estrelas
    print('*' * i)
    
"""
Em Python, quando multiplicamos uma string por um número inteiro, obtemos 
a repetição dessa string pelo número especificado de vezes.

Por exemplo:

    'a' * 3 resultará em 'aaa'
    'hello ' * 2 resultará em 'hello hello '

No contexto do exercício, estamos usando essa característica 
para repetir o caractere de estrela (*) um determinado número de vezes (i).

Vamos observar passo a passo como a expressão é avaliada durante cada iteração do loop:

    Quando i é 5: print('*' * 5) → Imprime *****
    Quando i é 4: print('*' * 4) → Imprime ****
    Quando i é 3: print('*' * 3) → Imprime ***
    Quando i é 2: print('*' * 2) → Imprime **
    Quando i é 1: print('*' * 1) → Imprime *

Desta forma, obtemos o padrão descendente de estrelas desejado. O 
loop for controla o número de vezes que o caractere de estrela é repetido, e a 
multiplicação da string cuida da repetição do caractere em si.

"""

"""
Exercício: Palavras com Mais de 4 Letras

Objetivo: Solicite ao usuário uma lista de palavras e, em 
seguida, exiba apenas as palavras que têm mais de 4 letras.

Instruções:

    1. Peça ao usuário que insira palavras separadas 
    por vírgula (por exemplo, ["casa","carro","sol","árvore"]).
    
    2. Use um loop for para iterar sobre essa lista de palavras.
    
    3. Dentro do loop, verifique o comprimento de cada palavra.
    
    4. Se a palavra tiver mais de 4 letras, imprima-a.

Após concluir o exercício, se o usuário inserir "casa,carro,sol,árvore", a saída deve ser:

carro
árvore

"""

# lista de palavras
palavras = ["casa","carro","sol","árvore", "ovo", "professor", "aluno"]

# Itera sobre a lista de palavras
for palavra in palavras:
    
    # Verifica se a palavra tem mais de 4 letras
    if len(palavra) > 4:
        
        # Imprime a palavra
        print(palavra)



#For Nested loops

"""
For Nested Loops" refere-se à prática de aninhar um ou mais 
loops for dentro de outro loop for. Em outras palavras, é quando 
você tem um loop for dentro do corpo de outro loop for. Esse conceito é 
aplicável em várias linguagens de programação, incluindo Python.
"""

# Exemplo de loops aninhados
# Inicia o loop externo, iterando a variável 'i' de 1 a 3 (o valor final 4 é exclusivo)
for linha in range(1, 4):
    
    # Inicia o loop interno, iterando a variável 'j' de 1 a 3 (o valor final 4 
    #é exclusivo) para cada valor de 'i'
    for coluna in range(1, 4):
        
        # Imprime o produto de 'i' e 'j', junto com os valores de 'i' e 'j' e os 
        #símbolos de multiplicação e igual
        print(i, "*", j, "=", i * j)


"""
Explicação:

    Loop Externo For: O loop externo for i in range(1, 4) iterará sobre a 
    sequência de números inteiros de 1 a 3 (inclusive). A variável de loop i 
    assumirá esses valores, um de cada vez.

    Loop Interno For: Dentro do loop externo, há outro loop for, denotado por 
    for j in range(1, 4). Este loop interno iterará sobre a mesma sequência de 
    números inteiros de 1 a 3 (inclusive). A variável de loop j assumirá esses 
    valores, um de cada vez.

    Corpo do Loop Interno: Dentro do loop interno, há uma única instrução:
    
        Imprimir Multiplicação: A função print(i, "*", j, "=", i * j) imprime a expressão 
        de multiplicação atual e seu resultado. Por exemplo, se i é 2 e j é 3, ele 
        imprimirá 2 * 3 = 6.

    Execução dos Loops Aninhados: O loop interno será executado completamente para 
    cada valor de i do loop externo. Como ambos os loops variam de 1 a 3, haverá um 
    total de 3×3=93×3=9 iterações para o loop interno.


O código ilustra o conceito de loops aninhados em Python, onde um loop 
é colocado dentro de outro loop. Neste exemplo, os loops aninhados são usados 
para gerar uma pequena tabela de multiplicação, demonstrando a relação de 
multiplicação entre os números de 1 a 3.
"""

"""
compreensão de lista (list comprehension) em Python, que é uma maneira 
concisa de criar listas. Aqui está um exemplo que combina um for e um if em 
uma única linha para criar uma lista de quadrados dos números ímpares de 0 a 9:
"""

quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)

"""
Ao executar este código, a lista quadrados_impares conterá os 
valores [1, 9, 25, 49, 81], que são os quadrados dos números 
ímpares entre 0 e 9.

Explicando o código:

    Vamos destrinchar a compreensão de lista [x**2 for x in range(10) if x % 2 != 0]:

    for x in range(10): Esta é a parte principal do loop. Ela vai 
    iterar sobre os números de 0 a 9 (isso é o que range(10) faz).

    if x % 2 != 0: Esta é a condição de filtragem. A expressão x % 2 retorna 
    o resto da divisão de x por 2. Se x for ímpar, esse resto será diferente 
    de 0. Portanto, esta condição verifica se x é ímpar.

    x**2: Esta é a expressão que será avaliada para cada x que satisfaça a 
    condição acima. Ou seja, para cada número ímpar x no intervalo de 0 a 9, esta 
    expressão calculará seu quadrado.
    

Agora, vamos converter essa compreensão de lista em um loop for tradicional:


quadrados_impares = []  # Lista vazia para armazenar os quadrados dos números ímpares

for x in range(10):  # Itera sobre os números de 0 a 9
    if x % 2 != 0:  # Verifica se x é ímpar
        quadrados_impares.append(x**2)  # Calcula o quadrado de x e adiciona à lista

print(quadrados_impares)


No final deste loop, a lista quadrados_impares terá os mesmos valores que a 
compreensão de lista original produziria: [1, 9, 25, 49, 81].
"""

print()

quadrados_impares = []

for x in range(10):  # Itera sobre os números de 0 a 9
    if x % 2 != 0:  # Verifica se x é ímpar
        quadrados_impares.append(x**2)  # Calcula o quadrado de x e adiciona à lista

print(quadrados_impares)


#List Comprehensions (Compreensão de Listas)
#Criando uma lista de todos os caracteres em uma string que não são vogais:
texto = "Hello World"
consoantes = [char for char in texto if char.lower() not in 'aeiou']
print(consoantes)

"""
Vamos destrinchar a compreensão de lista: [char for char in texto if char.lower() not in 'aeiou'].

    for char in texto: Este é o loop principal que itera sobre cada 
    caractere da string texto.

    char.lower(): Esta é uma conversão do caractere atual para minúsculas. Isso 
    garante que a comparação funcione tanto para letras maiúsculas quanto minúsculas.

    if char.lower() not in 'aeiou': Esta é a condição de filtragem. Ela verifica 
    se o caractere (convertido para minúsculo) não está na string 'aeiou', que contém 
    todas as vogais minúsculas. Assim, a condição se torna verdadeira apenas para 
    consoantes (e outros caracteres que não são vogais, como espaços, pontuação, etc.)

    char: Esta é a expressão a ser avaliada e adicionada à lista resultante para 
    cada char que satisfaça a condição acima. No contexto desta compreensão de lista, apenas 
    retorna o próprio caractere.

Vamos converter essa compreensão de lista para um loop for tradicional:
"""

#consoantes = [char for char in texto if char.lower() not in 'aeiou']

consoantes = []


# Lista vazia para armazenar os caracteres que não são vogais
consoantes_exemplo2 = []  

# Itera sobre cada caractere na string 'texto'
for letra in texto:  
    
    # Verifica se o caractere não é uma vogal
    if letra.lower() not in 'aeiou':  
        
        # Adiciona o caractere à lista 'consoantes'
        consoantes_exemplo2.append(letra)
        
print(consoantes_exemplo2)


"""
Exercício

Crie um programa em Python que solicite ao usuário que digite um número inteiro
não negativo. Em seguida, calcule e exiba o fatorial desse número.

Digite um número inteiro não negativo: 5
O fatorial de 5 é: 120
"""

# Solicita ao usuário a entrada de um número inteiro não negativo
numero = int(input("Digite um número inteiro não negativo: "))

# Verifica se o número informado é negativo
if numero < 0:
    
    # Se for negativo, exibe uma mensagem de erro
    print("O número deve ser não negativo.")
    
else:
    
    # Inicializa uma variável para armazenar o fatorial do número
    fatorial = 1

    # Loop que percorre todos os números inteiros de 1 até o número informado pelo usuário (inclusive)
    for i in range(1, numero + 1):
        
        # Multiplica o valor atual de 'fatorial' pelo número atual (i) na iteração
        # fatorial = fatorial * i
        fatorial *= i

    # Imprime o resultado final, que é o fatorial do número informado pelo usuário
    print("O fatorial de", numero, "é:", fatorial)
    

"""
Exercício

Crie um programa em Python que solicite ao usuário que digite um número inteiro
não negativo. Em seguida, calcule e exiba o fatorial desse número.

Digite um número inteiro não negativo: 5
O fatorial de 5 é: 120
"""

# Solicita ao usuário a entrada de um número inteiro não negativo
numero = int(input("Digite um número inteiro não negativo: "))

# Verifica se o número informado é negativo
if numero < 0:
    
    # Se for negativo, exibe uma mensagem de erro
    print("O número deve ser não negativo.")
    
else:
    
    # Inicializa uma variável para armazenar o fatorial do número
    fatorial = 1
    
    # Imprime a mensagem inicial indicando o cálculo do fatorial
    print("Cálculo do fatorial de", numero, ":")

    # Loop para multiplicar os números de 1 até o número informado
    for multiplicador in range(1, numero + 1):
        
        # Multiplica o valor atual de 'fatorial' pelo número atual na iteração
        fatorial *= multiplicador
        
        # Imprime o número da iteração atual seguido de "!" e o símbolo de igual
        print(f"{multiplicador}! =", end=" ")

        # Loop para imprimir a expressão do fatorial (e.g., "1 * 2 * 3")
        for i in range(1, multiplicador + 1):
            
            print(i, end="")
            
            if i != multiplicador:
                
                # Imprime o símbolo de multiplicação se não for o último número
                print(" * ", end="")
                
        # Imprime o resultado parcial do fatorial para a iteração atual
        print(" = ", fatorial)

    # Imprime o resultado final, que é o fatorial do número informado pelo usuário
    print("O fatorial de", numero, "é:", fatorial)


"""
numero = int(input("Digite um número inteiro não negativo: ")): O código inicia 
solicitando ao usuário que insira um número inteiro não negativo. A função input é 
usada para receber a entrada do usuário como uma string, e int() é usada para converter 
essa string em um número inteiro.

if numero < 0:: Aqui é realizada uma verificação para garantir que o número inserido pelo 
usuário não seja negativo. Se o número for negativo, o código entra no bloco do if.

print("O número deve ser não negativo."): Caso o número seja negativo, uma mensagem de erro é 
exibida, informando ao usuário que o número deve ser não negativo.

else:: Se o número inserido pelo usuário for não negativo, o código entra no bloco do else.

fatorial = 1: É inicializada uma variável chamada fatorial com o valor 1. Essa variável será 
usada para armazenar o resultado do fatorial do número informado pelo usuário.

print("Cálculo do fatorial de", numero, ":"): Uma mensagem é impressa indicando o início do 
cálculo do fatorial do número informado.

for multiplicador in range(1, numero + 1):: Aqui, é utilizado um loop for para iterar de 1 até o 
valor do número informado pelo usuário (incluindo o próprio número).

fatorial *= multiplicador: Em cada iteração do loop, o valor atual da variável fatorial é 
multiplicado pelo número atual na iteração. Isso é feito para calcular o fatorial.

print(f"{multiplicador}! =", end=" "): A cada iteração do loop, uma mensagem é impressa mostrando 
o número da iteração seguido do símbolo "!" e o símbolo de igual.

for i in range(1, multiplicador + 1):: É utilizado outro loop for dentro do loop principal para 
criar a expressão do fatorial (por exemplo, "1 * 2 * 3") que será impressa na saída.

print(i, end=""): O valor atual de i é impresso sem quebra de linha (end=""), para que os 
números sejam impressos sequencialmente.

if i != multiplicador:: É feita uma verificação para saber se o valor de i é diferente do 
valor atual do multiplicador na iteração. Se for diferente, significa que não estamos na 
última iteração do loop, então o símbolo de multiplicação "*" é impresso.

print(" * ", end=""): O símbolo de multiplicação "*" é impresso na mesma linha, sem quebra de linha.

print(" = ", fatorial): Após o loop interno ser concluído, é impresso o símbolo de igual "=" seguido 
do valor atual do fatorial até a iteração atual.

print("O fatorial de", numero, "é:", fatorial): Após o loop principal ser concluído, é impresso o 
resultado final, que é o fatorial do número informado pelo usuário.

O código utiliza loops para calcular o fatorial e imprimir a expressão do cálculo passo a passo. 

Ao final, o resultado é apresentado ao usuário. O fatorial de um número é o produto de todos os 
inteiros positivos menores ou iguais a ele. Por exemplo, o fatorial de 5 é 5! = 5 * 4 * 3 * 2 * 1 = 120.
"""

#For Criando um Retangulo

# Criando um retângulo com loops for
largura = 5  # Define a largura do retângulo
altura = 3   # Define a altura do retângulo

for i in range(altura):  # Loop para iterar pelas linhas do retângulo
    
    for j in range(largura):  # Loop para iterar pelas colunas do retângulo
    
        print("*", end=" ")  # Imprime o caractere "*" e um espaço na mesma linha
    
    print()  # Avança para a próxima linha após imprimir uma linha completa

"""
O código usa dois loops for aninhados para criar e imprimir
um retângulo feito de caracteres asteriscos (*). A largura e a altura do
retângulo são definidas pelas variáveis largura e altura.

Explicação:

    Definindo Largura e Altura: As variáveis largura e altura são
    definidas como 5 e 3, respectivamente. Elas determinam as
    dimensões do retângulo.

    Loop Externo For: O loop externo for i in range(altura) itera altura
    vezes, controlando o número de linhas do retângulo.

    Loop Interno For: Dentro do loop externo, há um loop interno for j
    in range(largura), que itera largura vezes, controlando o
    número de colunas do retângulo.

    Imprimir Caractere e Espaço: Dentro do loop interno, a função 
    print("*", end=" ") imprime o caractere asterisco (*) seguido de um
    espaço. O argumento end=" " garante que o próximo caractere seja impresso na
    mesma linha, em vez de avançar para a próxima linha.

    Avançar para a Próxima Linha: Após imprimir uma linha completa (loop interno),
    a função print() sem argumentos é chamada. Isso serve para avançar para a próxima
    linha, permitindo que o próximo conjunto de asteriscos seja impresso em uma nova linha.

    Execução dos Loops Aninhados: O loop interno será executado completamente para
    cada iteração do loop externo, criando o padrão retangular desejado.

Saída:

A saída do programa será um retângulo de asteriscos com 5 colunas e 3 linhas:

* * * * * 
* * * * * 
* * * * * 

O código ilustra o conceito de loops aninhados em Python e como eles podem
ser usados para criar padrões e formas geométricas. É um exemplo comum de manipulação
de loops para produzir saídas visuais.
"""
print()



# Criando um triângulo com a ponta no meios usando loops for

altura  = 5

for i in range(altura):
    
    """
    altura: É o valor definido anteriormente, representando a altura do triângulo.

    i: É o contador do loop for, que varia de 0 até o valor de 
    altura - 1. Ou seja, i representa o número da linha atual 
    sendo construída do triângulo.

    espacos: É a variável que irá armazenar a quantidade de espaços que serão 
    inseridos no início de cada linha do triângulo.

    Agora, vamos entender a fórmula altura - i - 1:

    O valor de i começa em 0 e aumenta em cada iteração até altura - 1. Isso 
    significa que na primeira iteração (i = 0), estamos construindo a linha de 
    número 1 do triângulo, na segunda iteração (i = 1), a linha de número 2, e 
    assim por diante.

    Para cada linha sendo construída, queremos adicionar espaços no início 
    para criar o efeito de triangulação. A quantidade de espaços em cada linha 
    depende da posição da linha em relação ao topo do triângulo. Ou seja, quanto mais 
    perto do topo, mais espaços precisamos adicionar.

    Para entender como a fórmula altura - i - 1 funciona, vamos considerar 
    o exemplo com altura = 5:

    Para a primeira linha (i = 0), temos: espacos = 5 - 0 - 1 = 4. Isso significa 
    que devemos adicionar 4 espaços antes do primeiro asterisco na primeira linha.

    Para a segunda linha (i = 1), temos: espacos = 5 - 1 - 1 = 3. Nesse caso, adicionamos 
    3 espaços antes do primeiro asterisco na segunda linha.

    Para a terceira linha (i = 2), temos: espacos = 5 - 2 - 1 = 2. Adicionamos 
    2 espaços antes do primeiro asterisco na terceira linha.

    E assim por diante...

    À medida que o valor de i aumenta, a quantidade de espaços diminui, pois 
    estamos construindo linhas mais próximas da base do triângulo.
    
    """
    espacos = altura - i - 1
    
    """
    altura = 5: Aqui, uma variável chamada altura é definida com o 
    valor 5. Essa variável representa a altura do triângulo que 
    será impresso na saída.

    for i in range(altura):: Este é um loop for que irá iterar 
    de 0 até o valor de altura - 1. Ou seja, no caso da altura ser 5, o 
    loop irá executar para i = 0, i = 1, i = 2, i = 3 e i = 4.

    espacos = altura - i - 1: Aqui, é calculada a quantidade de espaços 
    que devem ser inseridos no início de cada linha do triângulo. A quantidade 
    de espaços diminui à medida que aumenta o valor de i, ou seja, à medida 
    que o loop avança.

    asteriscos = 2 * i + 1: Essa linha é responsável por calcular a 
    quantidade de asteriscos que devem ser inseridos em cada linha do 
    triângulo. O valor de i é usado para calcular o número de asteriscos, 
    seguindo uma sequência de números ímpares. Quando i é 0, asteriscos 
    é igual a 1, quando i é 1, asteriscos é igual a 3, quando i é 2, 
    asteriscos é igual a 5 e assim por diante.

    print(" " * espacos + "*" * asteriscos): Aqui, a linha do triângulo 
    é construída combinando os espaços calculados na variável espacos e os 
    asteriscos calculados na variável asteriscos. Essa linha é impressa na 
    saída do console.
    """
    asteriscos = 2 * i + 1
    print(" " * espacos + "*" * asteriscos)








