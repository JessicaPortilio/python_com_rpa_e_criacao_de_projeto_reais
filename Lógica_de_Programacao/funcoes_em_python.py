#Funções

"""
Em programação, uma função é um bloco de código que realiza uma tarefa 
específica e pode ser executado várias vezes em diferentes partes do 
programa. As funções ajudam a organizar e modularizar o código, 
tornando-o mais legível, reutilizável e fácil de manter.
"""

#Criando uma função de soma
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)  # Saída: 5

resultado = soma(8, 9)
print(resultado)  # Saída: 5

resultado = soma(3, 7)
print(resultado)  # Saída: 5

#Criando uma função de soma
def soma(a, b):
    return a + b

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = soma(numero1, numero2)
print("A soma é:", resultado)

#Parâmetros e Argumentos em uma função
def saudacao(nome):
    """Função que exibe uma saudação personalizada."""
    print("Olá, " + nome + "! Bem-vindo(a)!")

# Argumento passado para a função
nome_usuario = "Maria"

# Chamada da função com o argumento
saudacao(nome_usuario)


#Argumentos Default e Non-default

"""
Em Python, ao definir uma função, você pode atribuir valores 
padrão aos parâmetros da função. Esses valores padrão são chamados de 
"argumentos default" (padrão) e permitem que você chame a função sem precisar 
fornecer valores para esses parâmetros, pois eles já têm um valor pré-definido.

Por outro lado, os "argumentos non-default" (não padrão) são aqueles que não 
possuem um valor padrão atribuído na definição da função e, portanto, precisam ser 
fornecidos como argumentos quando a função é chamada.
"""

def exibir_informacoes(nome="Allan", idade=39, cidade="Desconhecida"):
    
    """Função que exibe informações pessoais."""
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)
    print()

# Argumentos sem valores default
exibir_informacoes("João", 25, "São Paulo")

# Argumento com valor default
exibir_informacoes("Maria", 30)

#Exemplo com print():
def saudacao(nome):
    
    """Função que imprime uma saudação personalizada."""
    print("Olá, " + nome + "! Bem-vindo(a) ao nosso programa.")

saudacao("João")

#Exemplo com return:
def soma(a, b):
    
    """Função que retorna a soma de dois números."""
    return a + b

resultado = soma(3, 4)
print("O resultado da soma é:", resultado)

#Vários argumentos *args com números

"""
 parâmetro especial *args, que permite receber um número variável de argumentos numéricos. 
 Dentro da função, os argumentos são tratados como uma tupla.
"""

def soma(*args):
    
    """Função que retorna a soma de vários números."""
    resultado = sum(args)
    return resultado

total = soma(2, 4, 6, 8, 10)
print("A soma dos números é:", total)

"""
Dessa forma, a função soma() é capaz de lidar com qualquer quantidade de argumentos 
numéricos e retorna a soma total desses números.
"""
print()

"""
Exercício: Função para Calcular Estatísticas de Números

Objetivo: Familiarizar com a definição de funções que 
aceitem um número variável de argumentos usando *args, bem como calcular 
algumas estatísticas básicas de um conjunto de números.

Instruções:

    1. Defina uma função chamada estatisticas que aceite 
    um número variável de argumentos numéricos.
    
    2. A função deve retornar a média, o maior e o menor número do conjunto.
    3. Peça ao usuário para inserir uma sequência de números, separados por espaços.
    4. Converta essa entrada do usuário em uma lista de números.
    5. Use a função estatisticas para calcular a média, o maior e o menor número da lista.
    6. Mostre ao usuário a média, o maior e o menor número.
"""

def estatisticas(*args):
    
    return sum(args) / len(args), max(args), min(args)

"""
input("Digite uma sequência de números separados por espaços: "): A função 
input() é usada para obter uma entrada do usuário no console. Nesse caso, a 
mensagem "Digite uma sequência de números separados por espaços: " é exibida para 
o usuário, pedindo que ele insira uma sequência de números separados por espaços.

.split(): O método split() é chamado na string de entrada fornecida pelo 
usuário. Ele divide a string em partes separadas por espaços em branco, criando 
uma lista de strings.

map(float, ...): A função map() é usada para aplicar a função 
float() a cada elemento da lista de strings. A função float() é responsável 
por converter uma string que representa um número em um número de ponto 
flutuante (float). Isso é feito para garantir que todos os números da sequência 
digitada sejam tratados como valores numéricos de ponto flutuante.

list(...) : O resultado da função map(float, ...) é convertido em uma lista de 
números de ponto flutuante. Agora, a variável numeros é uma lista contendo os 
números digitados pelo usuário, convertidos em valores de ponto flutuante.

Depois disso, a função estatisticas(*numeros) é chamada com a lista de números 
numeros desempacotada usando o operador *. A função estatisticas calcula a média, o 
maior e o menor número da sequência e retorna esses valores.

Finalmente, os resultados são impressos na tela usando a função print() para 
mostrar a média, o maior e o menor número da sequência digitada pelo usuário.
"""
try:
    numeros = list(map(float, input("Digite uma sequência de números separados por espaços: ").split()))
    media, maior, menor = estatisticas(*numeros)
    if media is not None:
        print(f"Média: {media}")
        print(f"Maior Número: {maior}")
        print(f"Menor Número: {menor}")
    else:
        print("Nenhum número foi fornecido.")
except ValueError:
    print("Entrada inválida. Certifique-se de inserir números separados por espaços.")


#Vários argumentos xargs nomeando parametros

#função que recebe vários argumentos nomeados usando **kwargs:

"""
Em Python, **kwargs é um parâmetro especial usado em definições de função 
para capturar argumentos nomeados extras passados para a função. 
O termo "kwargs" é uma convenção comumente usada, mas o nome em si pode ser 
qualquer outro desde que seja precedido por dois asteriscos (**).

O parâmetro **kwargs permite que uma função aceite um número variável 
de argumentos nomeados adicionais. Os argumentos nomeados extras são 
passados para a função como um dicionário, onde as chaves são os nomes 
dos argumentos e os valores são os valores atribuídos a esses argumentos.
"""

def exibir_informacoes(**teste):
    
    """Função que exibe informações pessoais"""
    for chave, valor in teste.items():
        print(chave + ": " + str(valor))
        
exibir_informacoes(nome="João", idade=25, cidade="São Paulo", sexo="Masculino")

"""
Escopo de Variáveis
o	Variáveis locais vs. globais
o	Uso do global
o	Uso do nonlocal (em funções aninhadas)


Variáveis Locais vs. Globais

Uma variável definida dentro de uma função é chamada de 
variável local, enquanto uma definida fora de todas as funções é 
chamada de variável global.
"""

# Definindo uma variável global fora de qualquer função
variavel_global = "Eu sou uma variável global"

# Definindo a função funcao_exemplo
def funcao_exemplo():
    
    # Criando uma variável local dentro da função
    variavel_local = "Eu sou uma variável local"
    
    # Imprimindo a variável local
    print(variavel_local)
    
    # Imprimindo a variável global dentro da função (é possível acessá-la, mas 
    # para modificá-la, precisaríamos usar a palavra-chave 'global')
    print(variavel_global)
    

# Chamando a função funcao_exemplo, que imprimirá ambas as variáveis
funcao_exemplo()

# Imprimindo a variável global fora da função
print(variavel_global)

# print(variavel_local)  # Isso resultaria em um erro, pois variavel_local não existe fora da função.

"""
Uso do global

Para modificar uma variável global dentro de uma função, você 
precisa usar a palavra-chave global:
"""

# Definindo uma variável global chamada 'contador' e inicializando com 0
contador = 0


# Definindo a função 'incrementar_contador'
def incrementar_contador():
    
    # Informando à função que vamos usar a variável global 'contador' e não uma variável local
    global contador
    
    # Incrementando o valor da variável global 'contador'
    # contador = contador + 1
    contador += 1
    
    # Imprimindo o valor atualizado de 'contador'
    print(contador)

# Chamando a função 'incrementar_contador' pela primeira vez
# Isso incrementa 'contador' para 1 e imprime o valor
incrementar_contador()  # Imprime 1

# Chamando a função 'incrementar_contador' novamente
# Agora, 'contador' é incrementado para 2 e o novo valor é impresso
incrementar_contador()  # Imprime 2

incrementar_contador()  # Imprime 3


"""
Uso do nonlocal (em funções aninhadas)

A palavra-chave nonlocal é usada para trabalhar com variáveis em um 
escopo mais próximo, mas não global, como em funções aninhadas:
"""

print("\n---------------------------\n")

# Definindo a função 'funcao_externa'
def funcao_externa():
    
    # Criando uma variável 'variavel_externa' dentro do escopo da 'funcao_externa'
    variavel_externa = "Eu sou externa"
    
    # Definindo uma função aninhada chamada 'funcao_interna' dentro de 'funcao_externa'
    def funcao_interna():
        
        # Usando a palavra-chave 'nonlocal' para indicar que queremos
        # modificar a 'variavel_externa' do escopo imediatamente 
        # superior, ou seja, da 'funcao_externa'
        nonlocal variavel_externa
        
        print(variavel_externa)
        
        # Modificando a 'variavel_externa'
        variavel_externa = "Eu fui modificada pela função interna"
        
        # Imprimindo a 'variavel_externa' após modificá-la
        print(variavel_externa)
        
    # Chamando a 'funcao_interna' dentro da 'funcao_externa', que 
    # por sua vez modifica e imprime a 'variavel_externa'
    funcao_interna()
    
    # Imprimindo a 'variavel_externa' após a 'funcao_interna' 
    # ter sido chamada e ter modificado seu valor
    print(variavel_externa)

# Chamando a função 'funcao_externa' para executar o fluxo acima
funcao_externa()

"""
No exemplo acima, a função funcao_interna modifica a 
variavel_externa da função funcao_externa usando a palavra-chave nonlocal. 

Se você não usasse nonlocal, ocorreria um erro, pois estaria tentando 
modificar uma variável local que não foi definida na função interna.
"""

"""
Funções como Objetos de Primeira Classe

o	Atribuindo funções a variáveis
o	Passando funções como argumentos
o	Retornando funções de outras funções

Funções são objetos de primeira classe. Isso significa que 
elas podem ser tratadas como qualquer outro objeto, como strings, listas 
ou até mesmo classes. 

Aqui estão exemplos dos três casos mencionados:

"""

#Atribuindo funções a variáveis:
# Definindo uma função simples
def saudacao():
    
    return "Olá, mundo!"

# Atribuindo a função à variável 'cumprimentar'
cumprimentar = saudacao

# Chamando a função através da variável
print(cumprimentar())  # Saída: Olá, mundo!

#---------------------------

#Passando funções como argumentos

# Definindo duas funções simples
def saudacao_nome(nome):
    
    return f"Olá, {nome}!"

def cumprimentar(funcao, nome):
    
    return funcao(nome)

# Usando a função 'cumprimentar' e passando 'saudacao_nome' como um argumento
print(cumprimentar(saudacao_nome, "Alice"))  # Saída: Olá, Alice!

#------------------------------


#Retornando funções de outras funções

# Definindo uma função que retorna outra função
def nivel_saudacao(nivel):
    
    def saudacao_basica():
        return "Oi!"
    
    def saudacao_avancada():
        return "Olá, como você está?"

    if nivel == "basico":
        
        return saudacao_basica
    
    else:
        return saudacao_avancada

# Chamando a função 'nivel_saudacao' que retorna uma função, e depois chamando a função retornada
cumprimento = nivel_saudacao("basico")
print(cumprimento())  # Saída: Oi!

cumprimento = nivel_saudacao("avancado")
print(cumprimento())  # Saída: Olá, como você está?


"""
Exercício: Calculadora Simples com Funções

Objetivo: Criar uma calculadora simples que pode realizar 
quatro operações básicas: adição, subtração, multiplicação e divisão.

O usuário deverá fornecer dois números e a operação desejada. A solução 
deve ser implementada usando funções.

Instruções:

    Defina quatro funções: adicionar(), subtrair(), multiplicar() e dividir(). 
    
    - Cada função deve aceitar dois parâmetros (números) e retornar o resultado 
    da operação correspondente.
    - Peça ao usuário para inserir dois números.
    - Peça ao usuário para escolher uma das quatro operações (por exemplo, 
    ele pode digitar "adicionar" para adição).
    - Com base na escolha do usuário, chame a função correspondente e imprima o resultado.

"""

# Definindo as funções para as operações básicas

# Definindo a função para adicionar dois números
def adicionar(a, b):
    
    # Retorna a soma de a e b
    return a + b  

# Definindo a função para subtrair um número do outro
def subtrair(a, b):
    
    # Retorna a diferença entre a e b
    return a - b  

# Definindo a função para multiplicar dois números
def multiplicar(a, b):
    
    # Retorna o produto de a e b
    return a * b  

# Definindo a função para dividir um número pelo outro
def dividir(a, b):
    
    # Retorna a divisão de a por b
    return a / b  

# Solicitando ao usuário o primeiro número e convertendo-o para float
num1 = float(input("Digite o primeiro número: "))

# Solicitando ao usuário o segundo número e convertendo-o para float
num2 = float(input("Digite o segundo número: "))

# Solicitando ao usuário que escolha uma das operações definidas
op = input("Escolha uma operação (adicionar, subtrair, multiplicar, dividir): ")

# Usando condicionais para determinar qual função chamar com base na escolha do usuário
if op == "adicionar":
    
    # Chama a função de adição se o usuário escolheu 'adicionar'
    resultado = adicionar(num1, num2)  
    
elif op == "subtrair":
    
    # Chama a função de subtração se o usuário escolheu 'subtrair'
    resultado = subtrair(num1, num2)   
    
elif op == "multiplicar":
    
    # Chama a função de multiplicação se o usuário escolheu 'multiplicar'
    resultado = multiplicar(num1, num2) 
    
elif op == "dividir":
    
    # Chama a função de divisão se o usuário escolheu 'dividir'
    resultado = dividir(num1, num2)     
    
else:
    
    # Imprime uma mensagem de erro se o usuário não escolheu uma operação válida
    print("Operação inválida.")         

# Imprime o resultado da operação escolhida
print("Resultado:", resultado)


"""
Exercício: Fábrica de Funções de Operações Matemáticas

Imagine que você está construindo uma calculadora. Porém, ao invés de 
implementar cada operação matemática (soma, subtração, multiplicação e divisão) 
diretamente, você decide criar uma "fábrica de funções". Esta fábrica, quando fornecida 
com o nome de uma operação, deve retornar uma função que realiza a operação desejada.

Instruções:

    - Escreva uma função chamada fábrica_de_operacoes que aceite uma 
    string: 'soma', 'subtracao', 'multiplicacao' ou 'divisao'.
    
    - Dependendo do argumento fornecido, sua função deve retornar uma das 
    operações matemáticas. Por exemplo, se o argumento for 'soma', a função 
    retornada deve ser capaz de somar dois números.
    
    - Se a operação não for reconhecida, retorne uma função que 
    imprima "Operação não suportada.".
    
    
Desafio Extra:
Adapte a fábrica para aceitar operações com 
mais de dois números. Por exemplo, a operação de soma deve 
ser capaz de somar três, quatro ou mais números de uma só vez.

Dica: Utilize argumentos variáveis (*args) para essa adaptação.
"""

def fabrica_de_funcoes(operacao):
    
    # Esta função recebe um número indefinido de argumentos e os soma.
    def soma(*args):
        
        return sum(args)
    
    # Esta função subtrai todos os números subsequentes do primeiro número.
    def subtracao(*args):
        
        resultado = args[0]
        
        # Itera sobre todos os números após o primeiro
        for num in args[1:]:
            
            #resultado = resultado - num
            resultado -= num
            
        return resultado
    
    # Esta função multiplica todos os números fornecidos.
    def multiplicacao(*args):
        
        resultado = 1
        
        # Itera sobre todos os números e os multiplica
        for num in args:
            
            #resultado = resultado * num
            resultado *= num
            
        return resultado
    
    # Esta função divide o primeiro número pelos números subsequentes.
    def divisao(*args):
        
        resultado = args[0]
        
        # Itera sobre todos os números após o primeiro
        for num in args[1:]:
            
            # Verifica se algum número é zero (para evitar divisão por zero)
            if num == 0:
                
                """
                é usada para lançar (ou "raise", em inglês) uma exceção do tipo ValueError.

                Em programação, uma exceção é uma forma de sinalizar que algo inesperado 
                aconteceu durante a execução de um programa. Quando uma exceção é 
                lançada e não tratada, ela interrompe a execução do programa e produz 
                uma mensagem de erro.

                A razão pela qual lançamos essa exceção específica é porque a divisão por zero 
                é matematicamente indefinida e resultaria em um erro se tentássemos fazer 
                isso em Python (ou na maioria das linguagens de programação). Em vez de permitir 
                que esse erro ocorra, detectamos o caso em que um número é dividido por zero e 
                lançamos uma exceção com uma mensagem explicativa.

                Em outras palavras, essa linha foi adicionada para:

                    Prevenir a ocorrência de um erro de divisão por zero.
                    
                    Fornecer uma mensagem de erro amigável e explicativa para o usuário, 
                    informando-o do problema.

                Se você remover essa linha e tentar dividir por zero, o Python lançará sua 
                própria exceção de ZeroDivisionError, que pode não ser tão amigável ou específica 
                quanto à mensagem que fornecemos.
                """
                raise ValueError("Divisão por zero não é permitida.")
                
            resultado /= num
            
        return resultado
    
    # Retorna a função correspondente baseada no valor da 'operacao'
    if operacao == "soma":
        
        return soma
    
    elif operacao == "subtracao":
        
        return subtracao
    
    elif operacao == "multiplicacao":
        
        return multiplicacao
    
    elif operacao == "divisao":
        
        return divisao
    
    else:
        
        def operacao_nao_suportada(*args):

            return "Operação não suportada."
        
        return operacao_nao_suportada
    
    
# Testando o código
adicionar = fabrica_de_funcoes("soma")
print(adicionar(5, 3, 2, 9, 4, 7)) # Esperado: 30

subtrair = fabrica_de_funcoes("subtracao")
print(subtrair(50, 30, 5)) # Esperado: 15

multiplicar = fabrica_de_funcoes("multiplicacao")
print(multiplicar(5, 3, 2)) # Esperado: 30

dividir = fabrica_de_funcoes("divisao")
print(dividir(10, 2, 2)) # Esperado: 2.5

operacao_invalida = fabrica_de_funcoes("modulo")
print(operacao_invalida(5, 3)) # Esperado: "Operação não suportada."
            


"""
Funções Anônimas (Lambda)
o	Definição e uso
o	Limitações em relação às funções regulares


Função lambda


Funções lambda são funções anônimas de pequena extensão. Ao contrário 
de uma função definida com def, a função lambda pode ter apenas uma 
expressão e retorna implicitamente o resultado dessa expressão. Ela é 
frequentemente usada para pequenas operações que são convenientes de 
se definir sem nomear uma função completa.


"""

#Exemplo Prático 1: Definição e uso

#Função Regular para Dobrar um Número

def dobrar(n):
    
    return n * 2

print("Função Regular:", dobrar(5)) # Saída: 10 

#Função Lambda para Dobrar um Número
dobrar_com_lambda = lambda n: n * 2

print("Função Lambda:", dobrar_com_lambda(5)) # Saída: 10 

"""
Exemplo Prático 2: Limitações

    Expressividade

Função Regular para Classificar Números:
"""

def classificar_numero(n):
    
    if n < 0:
        
        return "Negativo"
    
    elif n == 0:
        
        return "Zero"
    
    else:
        
        return "Positivo"

print(classificar_numero(5)) #Saída: Positivo

#Tentativa de Função lambda para Classificar Números (Menos Clara):

classificar_numero_lambda = lambda n: "Negativo" if n < 0 else ( "Zero" if n == 0 else "Positivo")

print(classificar_numero_lambda(5)) #Saída: Positivo
"""
    Nomeação

Sem atribuir a função lambda a uma variável, ela permanece anônima. 
Você pode usá-la, por exemplo, em funções como sorted:

Ordenar uma lista de strings pelo comprimento usando função lambda:
"""

#Função lambda com sorted

"""
Exemplo com sorted:

Suponha que você tenha uma lista de tuplas representando 
pessoas e suas idades, e você queira classificá-las pela idade:
"""

pessoas = [("João", 35), ("Maria", 25), ("Pedro", 40)]
pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])

print(pessoas_ordenadas)  # Saída: [('Maria', 25), ('João', 35), ('Pedro', 40)]

#No exemplo acima, estamos usando a função lambda 
#para especificar que queremos ordenar as tuplas pela idade (índice 1).

"""
    sorted(): É uma função built-in do Python que retorna uma nova 
    lista contendo todos os itens da lista original em ordem crescente.
    
    Uma função built-in é uma função que já vem incluída no 
    núcleo do Python, de modo que você não precisa importar nenhum módulo ou 
    pacote adicional para usá-la. Essas funções estão sempre disponíveis no namespace 
    principal e ajudam a realizar tarefas comuns sem a necessidade de escrever código extra.

    pessoas: É a lista que você deseja ordenar. No exemplo fornecido, 
    pessoas é uma lista de tuplas onde cada tupla contém um nome e uma idade.

    key: É um argumento opcional que você pode passar para a função 
    sorted(). Ele espera uma função que pode aceitar um item da 
    lista (neste caso, uma tupla) e retornar um valor que será usado 
    para ordenar a lista.

    lambda x: x[1]: Esta é uma função lambda que aceita uma 
    tupla x e retorna o segundo item da tupla (ou seja, x[1]). Neste 
    contexto, isso significa que estamos pegando a idade de cada 
    tupla. A função sorted() usará essas idades para ordenar a lista de tuplas.

Então, quando você escreve pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1]), você está dizendo:

    "Eu quero ordenar a lista pessoas."
    
    "Para determinar a ordem, para cada tupla em pessoas, pegue o segundo 
    item da tupla (a idade) e use-o como a chave de ordenação."
    
    "Coloque o resultado ordenado na variável pessoas_ordenadas."

O resultado é uma lista de tuplas ordenadas por idade.
"""
print()


"""
    Restrição de escopo

Vamos considerar um exemplo em que tentamos modificar uma variável 
global usando global em uma função lambda, mas não podemos.

Função Regular Modificando uma Variável Global:
"""

contador = 0

def aumentar_contador():
    
    global contador
    
    contador += 1 

aumentar_contador()
print(contador)

aumentar_contador()
print(contador)

aumentar_contador()
print(contador)

#Tentativa de Função Lambda Modificando uma Variável Global (Isso causará um erro):
# A seguinte linha causará um erro se descomentada
# aumentar_contador = lambda: global contador; contador += 1


#Esses exemplos práticos ajudam a entender a versatilidade e as 
#limitações das funções lambda em comparação com as funções regulares.

#função lambda com filter

"""
Filtramos uma lista para obter apenas números pares 
usando a função filter() junto com uma função lambda.

Problema:
Dada uma lista de números, filtre-a para obter apenas os números pares.
"""

# Lista original de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando filter() e lambda para obter apenas números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

"""
    list(): A função list() é usada para converter um iterável em uma lista. No 
    contexto desta linha, ela está sendo usada para converter o iterador resultante 
    da função filter() de volta em uma lista.

    filter(): A função filter() é uma função built-in do Python que filtra os itens 
    de um iterável (como uma lista) com base em uma função fornecida. Ela retorna um 
    iterador, razão pela qual usamos list() para converter de volta em uma lista.

    lambda x: x % 2 == 0: Esta é uma função lambda. É uma pequena função anônima que pode \
    ter qualquer número de argumentos, mas só pode ter uma expressão. Esta expressão 
    específica retorna True se x for par e False caso contrário.
    
        x % 2 retorna o resto da divisão de x por 2.
        x % 2 == 0 verifica se esse resto é zero (o que indica que x é um número par).

    numeros: É a lista original de números que você deseja filtrar.

Então, quando você combina tudo, esta linha de código está dizendo:

    "Quero filtrar a lista numeros."
    "Para cada número na lista, quero verificar se ele é par."
    "Se for par, inclua-o no resultado."
    "Finalmente, converta o resultado filtrado de volta em uma lista e armazene-o na variável numeros_pares."

Assim, numeros_pares acabará sendo uma lista contendo apenas os números pares da lista original numeros.
"""

print(numeros_pares)  # Saída: [2, 4, 6, 8, 10]

"""
Explicação:
A função lambda lambda x: x % 2 == 0 verifica se um número 
é par (ou seja, se ele é divisível por 2 sem deixar um resto). A função filter() então 
aplica essa função lambda a cada item da lista numeros. Os itens que retornam True são mantidos 
no resultado, que no final são os números pares.
"""
print()

"""
Vamos criar um exemplo onde filtramos uma lista de strings 
para obter apenas aquelas que começam com a letra "A".

Problema:

Dada uma lista de nomes, filtre-a para obter apenas os nomes 
que começam com a letra "A".
"""

# Lista original de nomes
nomes = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Tom"]

# Usando filter() e lambda para obter apenas nomes que começam com "A"
nomes_com_A = list(filter(lambda nome: nome[0] == "A", nomes))

"""
    list(): Esta função é usada para converter um iterável em uma lista. 
    No contexto desta linha, ela está sendo usada para converter o resultado 
    do filter() de um iterador de volta para uma lista.

    filter(): A função filter() é uma função built-in do Python que é usada 
    para filtrar os itens de um iterável (como uma lista) com base em uma função 
    fornecida. Ela irá retornar um iterador contendo todos os itens do iterável para 
    os quais a função aplicada retorna True.

    lambda nome: nome[0] == "A": Esta é uma função lambda, que é uma pequena função anônima em Python.
    
        nome: é o argumento da função. Para cada string na lista nomes, a string 
        será passada para esta função lambda.
        
        nome[0]: obtém o primeiro caractere da string nome.
        
        nome[0] == "A": verifica se o primeiro caractere da string nome 
        é igual a "A". Se for, a função retorna True; caso contrário, retorna False.

    nomes: É a lista original de nomes que você deseja filtrar.

Quando juntamos tudo, a linha está fazendo o seguinte:

    "Quero filtrar a lista nomes."
    "Para cada nome na lista, quero verificar se ele começa com a letra 'A'."
    "Se começar, inclua-o no resultado."
    "Finalmente, converta o resultado filtrado de volta em uma lista."

Como resultado, nomes_com_A será uma lista contendo apenas os nomes da 
lista original nomes que começam com a letra "A".
"""

print(nomes_com_A)  # Saída: ['Alice', 'Anna', 'Alex']

"""
Explicação:

A função lambda lambda nome: nome[0] == "A" verifica se a 
primeira letra do nome é "A". A função filter() aplica essa função 
lambda a cada item da lista nomes. Os itens que retornam True (aqueles que 
começam com "A") são mantidos no resultado.
"""
print()


"""
Suponhamos que queremos filtrar uma lista de nomes e obter 
apenas aqueles que são exatamente "Alice".

Problema:
Dada uma lista de nomes, filtre-a para obter apenas as entradas que são "Alice".
"""

# Lista original de nomes
nomes = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Tom", "Alice"]

# Usando filter() e lambda para obter apenas as entradas que são "Alice"
nomes_Alice = list(filter(lambda nome: nome == "Alice", nomes))

print(nomes_Alice)  # Saída: ['Alice', 'Alice']

"""
Explicação:
A função lambda lambda nome: nome == "Alice" compara cada entrada 
da lista nomes com a string "Alice". Se a entrada for exatamente igual 
a "Alice", a função retorna True; caso contrário, retorna False. A função 
filter() pega esses valores True e False e inclui apenas as entradas que 
retornam True no resultado final.
"""
print()

#Função lambda com map
"""
Vamos a um exemplo em que utilizaremos a função map() com uma 
função lambda para transformar uma lista de números, elevando cada número ao quadrado.

Problema:
Dada uma lista de números, retorne uma nova lista onde cada número é elevado ao quadrado.
"""

# Lista original de números
numeros = [1, 2, 3, 4, 5]

# Usando map() e lambda para elevar cada número ao quadrado
numeros_ao_quadrado = list(map(lambda x: x**2, numeros))

"""
    lambda x: x2:
        Uma função lambda é uma pequena função anônima.
        A função lambda pode ter qualquer número de argumentos, mas só pode ter uma expressão.
        Aqui, a expressão lambda x: x**2 define uma função que aceita um argumento x e retorna x ao quadrado.

    map():
        A função map() aplica uma função a todos os itens de um objeto de entrada (como uma lista ou tupla).
        No caso acima, map() aplica a função lambda definida anteriormente a cada item da lista numeros.

    list():
        A função list() converte o resultado de map() em uma lista. Isso é necessário porque 
        a função map() retorna um objeto iterável de tipo map, e se você deseja uma lista como 
        saída, você deve convertê-lo em uma lista.

    Então, se você tiver a lista numeros = [1, 2, 3, 4, 5]:

    A função map() aplica a função lambda a cada elemento da lista, resultando nos quadrados 
    de cada número: 1, 4, 9, 16 e 25.

    Finalmente, a função list() converte esses resultados em uma lista, dando o resultado final 
    para numeros_ao_quadrado como [1, 4, 9, 16, 25].
"""

print(numeros_ao_quadrado)  # Saída: [1, 4, 9, 16, 25]


"""
Explicação:

A função lambda lambda x: x**2 pega cada número x e retorna seu 
quadrado. A função map() aplica essa função lambda a cada item da lista 
numeros. 

O resultado é um iterador com os números elevados ao quadrado, então 
usamos list() para convertê-lo de volta em uma lista.
"""
print()

"""
Vamos criar um exemplo onde usaremos a função map() juntamente 
com uma função lambda para transformar uma lista de palavras em uma lista 
que contém o comprimento de cada palavra.

Problema:

Dada uma lista de palavras, retorne uma nova lista contendo o 
comprimento de cada palavra.
"""

# Lista original de palavras
palavras = ["maça", "banana", "arroz", "abacate"]

# Usando map() e lambda para obter o comprimento de cada palavra
comprimentos = list(map(lambda palavra: len(palavra), palavras))

"""
    list(): Esta função é utilizada para converter um iterável (como o resultado 
    do map()) em uma lista. A função map(), por padrão, retorna um iterador, e ao envolvê-lo 
    com list(), estamos convertendo esse iterador em uma lista real.

    map(): A função map() é uma função built-in do Python que aplica uma função a 
    todos os itens em um iterável (neste caso, a lista palavras). A ideia principal 
    aqui é transformar cada item da lista original (cada palavra) em um novo 
    valor (neste caso, o comprimento de cada palavra).

    lambda palavra: len(palavra): Isso é uma função lambda (uma função anônima de uma única linha).

        palavra: É a variável que recebe cada item da lista palavras um de cada vez.

        len(palavra): Esta parte da função lambda retorna o comprimento da palavra 
        atual. len() é uma função built-in do Python que retorna o número de itens em um 
        objeto, neste contexto, o número de caracteres em uma string.

    palavras: Este é o iterável original (a lista de palavras) que você deseja transformar.

Quando você combina tudo, o que esta linha faz é:

    Para cada palavra na lista palavras, obtenha o comprimento dessa palavra.
    Crie uma nova lista, comprimentos, contendo os comprimentos de todas as palavras da lista original.

Então, se a lista palavras contém ["maça", "banana"], a lista resultante 
comprimentos será [4, 6], porque "arroz" tem 5 letras e "abacate" tem 7 letras.
"""

print(comprimentos)  # Saída: [4, 6, 5, 7]

"""
Exercício: Filtrando e Transformando Dados com Lambda

Objetivo: Familiarizar-se com o uso de funções lambda 
juntamente com funções built-in como filter e map.

Instruções:

    1. Dada uma lista de números: numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28].
    
    2. Use a função filter() e uma função lambda para criar uma nova 
    lista que contém apenas os números ímpares da lista original.
    
    3. Em seguida, use a função map() e uma função lambda para 
    criar uma nova lista que contém o quadrado de cada número da lista de números ímpares.
    
    4. Imprima ambas as listas.
    
    Dicas:

    Use filter() para filtrar itens de uma lista.
    Use map() para aplicar uma função a cada item de uma lista.
"""

# Lista inicial de números
numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]

# Filtrando números ímpares
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))

"""
    filter(): É uma função built-in do Python que filtra os itens de 
    um iterável (como uma lista) com base em uma função fornecida. Retorna 
    um iterador, razão pela qual usamos list() para convertê-lo de volta em uma lista.

    lambda x: x % 2 != 0: Esta é uma função lambda que verifica se um 
    número x é ímpar. Se o número x quando dividido por 2 tiver um 
    resto diferente de zero, então ele é ímpar.

    numeros: É a lista original de números que você quer filtrar.

O resultado dessa linha de código é uma nova lista, numeros_impares, que 
contém apenas os números ímpares da lista original numeros.
"""

# Obtendo o quadrado de cada número ímpar
quadrados_impares = list(map(lambda x: x ** 2, numeros_impares))

"""
    map(): É outra função built-in do Python que aplica uma função 
    especificada a todos os itens de um iterável (novamente, como uma 
    lista). Assim como filter(), map() também retorna um iterador, e é por 
    isso que usamos list() para convertê-lo novamente em uma lista.

    lambda x: x ** 2: Esta é uma função lambda que retorna o quadrado 
    de um número x.

    numeros_impares: É a lista de números ímpares que obtivemos na 
    primeira linha de código que explicamos.

O resultado dessa linha é uma nova lista, quadrados_impares, que contém 
o quadrado de cada número da lista numeros_impares.

Ambas as linhas são exemplos de como as funções lambda podem ser 
usadas em conjunto com funções como filter() e map() para processar e 
transformar listas de maneira concisa.
"""

# Imprimindo os resultados
print(f"Números ímpares: {numeros_impares}")
print(f"Quadrados dos números ímpares: {quadrados_impares}")

"""
Funções Internas (built-in)

As funções internas (ou built-in functions, em inglês) são funções 
que já vêm embutidas na linguagem Python, ou seja, elas estão disponíveis sem a 
necessidade de importar nenhum módulo ou biblioteca adicional.

o	print(), len(), input(), etc.
o	Conversão de tipos: int(), float(), str(), etc.

"""

#Funções Internas (built-in)

#print(): Utilizada para imprimir valores no console.

nome = "Maria"
print("Olá,", nome)  # Saída: Olá, Maria


#len(): Retorna o número de itens em um objeto.
lista = [1, 2, 3, 4]
print(len(lista))  # Saída: 4

#input(): Lê uma linha do input (entrada padrão).
#nome = input("Digite seu nome: ")  

# O usuário insere "Carlos" e pressiona enter
print("Seu nome é", nome)  # Saída: Seu nome é Carlos

#Conversão de tipos

#int(): Converte um valor para um inteiro.
numero_decimal = "7.9"
numero_inteiro = int(float(numero_decimal))  

#Nota: Aqui, primeiramente converti a string para float, e depois 
#para int, porque diretamente não podemos converter a string "7.9" para int.

print(numero_inteiro)  # Saída: 7

#float(): Converte um valor para ponto flutuante (decimal).
numero_str = "5.6"
numero_float = float(numero_str)
print(numero_float)  # Saída: 5.6

#str() - Converte um valor para string
numero = 123
numero_str = str(numero)
print(numero_str)

"""
Estes são exemplos simples e práticos de algumas funções built-in e 
funções de conversão de tipos em Python. Existem muitas outras funções built-in 
disponíveis no Python que oferecem uma variedade de funcionalidades úteis.
"""
print()

"""
Recursão
•	Funções que chamam a si mesmas
•	Problemas clássicos, como o cálculo do fatorial
•	Riscos e limitações da recursão em Python

"""

#1. Funções que chamam a si mesmas:

#Uma função recursiva é uma função que se chama a si mesma em sua definição.
# Define uma função chamada contar_regressivamente
def contar_regressivamente(n):
                           
    # Verifica se n é maior que 0
    if n > 0:
                           
        # Imprime o valor atual de n
        print(n)
                           
        # Chama a função contar_regressivamente passando n-1 como argumento (recursividade)
        contar_regressivamente(n-1)

# Chama a função contar_regressivamente com o valor inicial 5
contar_regressivamente(5)

"""
No exemplo acima, a função contar_regressivamente imprime números de n até 1.

2. Problemas clássicos:

"""

#Fatorial:
#O fatorial de um número é o produto desse número por todos os seus 
#antecessores até 1. Por exemplo, 5! (lê-se "5 fatorial") é 5 × 4 × 3 × 2 × 1 = 120.
# Define uma função chamada fatorial
def fatorial(n):
                           
    # Se n for 0, o fatorial de 0 é definido como 1
    if n == 0:
        
        return 1
                           
    else:
        
        # Caso contrário, o fatorial de n é n multiplicado pelo fatorial de n-1 (chamada recursiva)
        return n * fatorial(n-1)

# Imprime o fatorial de 5
print(fatorial(5))  # Saída: 120


"""
3. Riscos e limitações da recursão em Python:

A recursão tem seus riscos e limitações. Uma delas é a "RecursionError", 
que ocorre quando a profundidade máxima da recursão é atingida. Por padrão, Python 
tem uma profundidade máxima de recursão de 1000 chamadas.

Exemplo:
"""

def recursao_infinita(n):
    
    print(n)
    
    return recursao_infinita(n+1)

# Descomente a linha abaixo para ver o erro, mas cuidado, vai gerar muitos prints!
#recursao_infinita(1)

"""
Se você descomentar e executar o código acima, receberá uma 
"RecursionError" após 1000 chamadas recursivas.

Nota: É importante utilizar recursão com cuidado e garantir que haja 
um caso base para interromper a recursão e evitar loops infinitos ou estouro da pilha.
"""
print()



"""
Documentação e Anotações de Funções
•	Docstrings
•	Anotações de tipo (Type Hints)


1. Docstrings:

Docstrings são usadas para documentar especificamente o que uma função 
faz, seus parâmetros e o que ela retorna. Eles são colocados logo após 
a definição da função, antes do código da função começar, e são escritos entre três aspas duplas """

#Exemplo
def somar(a, b):
    
    """
    Função que retorna a soma de dois números.

    Parâmetros:
    a (int ou float): Primeiro número.
    b (int ou float): Segundo número.

    Retorna:
    int ou float: A soma de a e b.
    """
    return a + b


print(somar(2, 3))  # Saída: 5
print(somar.__doc__)  # Isso imprimirá a docstring da função


#2. Anotações de tipo (Type Hints)
"""
Anotações de tipo são usadas para indicar os tipos esperados dos 
argumentos e o tipo de retorno de uma função. Elas não causam nenhuma 
verificação de tipo em tempo de execução, mas são úteis para documentação e 
ferramentas de verificação estática de tipo como o mypy.

Exemplo:
"""
def multiplicar(a: int, b: int) -> int:
    
    """Função que retorna a multiplicação de dois números inteiros."""
    return a * b

print(multiplicar(4, 5))  # Saída: 20

"""
No exemplo acima, as anotações a: int e b: int indicam que os parâmetros 
a e b devem ser inteiros. A anotação -> int indica que a função retorna um inteiro.

A combinação de docstrings e anotações de tipo pode tornar o código 
Python mais legível e manutenível, pois fornece informações claras sobre a função, seus 
argumentos e retornos.
"""
print()








