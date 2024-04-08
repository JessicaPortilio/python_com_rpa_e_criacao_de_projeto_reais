"""
Listas

    Introdução às Listas
        Definição e utilidade das listas em Python.
        Diferença entre listas e outros tipos de dados.

    Criando e Acessando Listas
        Como criar uma lista: minha_lista = [1, 2, 3]
        Acessando elementos pelo índice.
        Índices negativos para acessar elementos do final da lista.

    Operações Básicas com Listas
        Adicionar elementos: append(), insert()
        Remover elementos: remove(), pop()
        Concatenar listas: +, extend()
        Repetir listas: *
        Verificar se um item está na lista: in

    Métodos de Listas
        sort(): ordena a lista in-place.
        reverse(): inverte a ordem dos elementos in-place.
        count(): conta o número de ocorrências de um elemento.
        index(): retorna o índice da primeira ocorrência de um elemento.

    Slicing de Listas
        Como acessar subconjuntos de listas: minha_lista[1:3]
        Omissão de índices iniciais ou finais: minha_lista[:2], minha_lista[2:]
        Slicing com passos: minha_lista[::2]

    List Comprehensions
        Uma maneira concisa de criar listas: [x**2 for x in range(10) if x % 2 == 0]

    Listas Aninhadas (listas de listas)
        Criando e acessando listas dentro de listas.
        Utilizando loops aninhados para iterar sobre elas.

    Copiando Listas
        Cópia rasa (shallow copy): copy(), slicing.
        Cópia profunda (deep copy): usando o módulo copy.

    Utilidades e Funções com Listas
        len(): retorna o número de elementos na lista.
        max(): retorna o maior valor.
        min(): retorna o menor valor.
        sum(): retorna a soma dos elementos.

    Iteração em Listas
        Usando o loop for.
        Usando enumerate() para obter índice e valor ao iterar.

    Listas e Strings
        Conversão de strings para listas: list(), split().
        Conversão de listas para strings: join().

"""
print()

"""
Introdução às Listas: Definição e utilidade

Listas são uma das estruturas de dados mais fundamentais em Python. Elas são 
coleções ordenadas de itens (que podem ser de qualquer tipo) e são muito versáteis.

Vamos supor que você quer armazenar as notas de um aluno em diferentes 
matérias. Uma lista é perfeita para isso!
"""

# Definindo uma lista de notas de um aluno
notas_aluno = [85, 90, 78, 92, 88]
print(notas_aluno)

"""
A utilidade das listas em Python é vasta, elas podem ser usadas para armazenar 
conjuntos de dados relacionados, manipular esses dados e percorrê-los.

Diferença entre listas e outros tipos de dados

Para entender as diferenças, vamos comparar listas com alguns outros tipos de 
dados em Python:
"""

#1. Listas vs. Inteiros/Floats: Inteiros e floats representam números, enquanto 
#listas podem armazenar múltiplos itens, que podem ser números ou outros tipos de dados.


numero = 5
print(type(numero))  # <class 'int'>

lista_de_numeros = [5, 10, 15]
print(type(lista_de_numeros))  # <class 'list'>

#Listas vs. Strings: Strings são sequências de caracteres. Listas, por outro 
#lado, podem armazenar caracteres, números, e até outras listas!

mensagem = "Olá"
print(type(mensagem))  # <class 'str'>

lista_de_strings = ["Olá", "Mundo"]
print(lista_de_strings)  # <class 'list'>
print(type(lista_de_strings))  # <class 'list'>


#Listas vs. Tuplas: Ambas podem armazenar múltiplos itens, mas as listas 
#são mutáveis (você pode alterar seu conteúdo), enquanto as tuplas são imutáveis.
lista = [1, 2, 3]
lista[0] = 100  # Isso é válido
lista[1] = 50  # Isso é válido

print()
print(lista)

tupla = (1, 2, 3)
#tupla[0] = 100  # Isso geraria um erro, porque tuplas são imutáveis!


"""
Este é apenas um breve exemplo que destaca a definição, utilidade e 
diferenças das listas em relação a outros tipos de dados em Python. A profundidade e 
amplitude do tópico podem variar de acordo com o contexto e o público-alvo.
"""
print()


"""
Criando e Acessando Listas
        Como criar uma lista: minha_lista = [1, 2, 3]
        Acessando elementos pelo índice.
        Índices negativos para acessar elementos do final da lista.
"""

#Criar uma lista é tão simples quanto colocar diferentes 
#valores separados por vírgulas entre colchetes [].


# Criando uma lista de números
numeros = [10, 20, 30, 40, 50]
print(numeros)  # Saída: [10, 20, 30, 40, 50]

# Criando uma lista de strings
frutas = ["maçã", "banana", "cereja"]
print(frutas)  # Saída: ['maçã', 'banana', 'cereja']

# Criando uma lista mista
mista = [10, "Olá", 2.5, ["a", "b"], True]
print(mista)  # Saída: [10, 'Olá', 2.5, ['a', 'b'], True]


#Acessando elementos pelo índice

#O índice de uma lista em Python começa em 0. Portanto, para acessar o 
#primeiro item de uma lista, você usaria índice 0, para o segundo item você 
#usaria índice 1, e assim por diante.

frutas = ["maçã", "banana", "cereja", "damasco"]

# Acessando o primeiro elemento (índice 0)
print(frutas[0])  # Saída: maçã

# Acessando o terceiro elemento (índice 2)
print(frutas[2])  # Saída: cereja


#Índices negativos para acessar elementos do final da lista

#Índices negativos em Python são uma forma elegante de acessar elementos 
#a partir do final da lista. Por exemplo, um índice de -1 refere-se ao último 
#item, -2 ao penúltimo e assim por diante.

frutas = ["maçã", "banana", "cereja", "damasco"]

# Acessando o último elemento
print(frutas[-1])  # Saída: damasco

# Acessando o penúltimo elemento
print(frutas[-2])  # Saída: cereja

"""
Esses são os conceitos básicos sobre como criar e acessar listas 
em Python. Com essa base, você pode explorar ainda mais as operações e 
métodos disponíveis para listas.
"""
print()


"""
Exercício: Criando e Acessando Listas

Objetivo: Familiarizar-se com a criação de listas e o acesso a seus 
elementos usando índices positivos e negativos.

Passo 1: Crie uma lista chamada frutas contendo os seguintes 
itens: "maçã", "banana", "cereja", "damasco" e "figo".

Passo 2: Imprima a primeira fruta da lista.

Passo 3: Imprima a terceira fruta da lista.

Passo 4: Imprima a última fruta da lista usando um índice negativo.

Passo 5: Tente acessar um índice que não existe na 
lista (por exemplo, índice 10) e observe o erro gerado.

Passo 6: Usando índices negativos, imprima a segunda última fruta da lista.
"""

#Solução

#Passo 1: Crie uma lista chamada frutas contendo os seguintes 
#itens: "maçã", "banana", "cereja", "damasco" e "figo".
frutas = ["maçã", "banana", "cereja", "damasco", "figo"]

#Passo 2: Imprima a primeira fruta da lista.
print(frutas[0])

#Passo 3: Imprima a terceira fruta da lista.
print(frutas[2])

#Passo 4: Imprima a última fruta da lista usando um índice negativo.
print(frutas[-1])

#Passo 5: Tente acessar um índice que não existe na 
#lista (por exemplo, índice 10) e observe o erro gerado.
#print(frutas[10])

#Passo 6: Usando índices negativos, imprima a segunda última fruta da lista.
print(frutas[-2])

"""
Operações Básicas com Listas
        Adicionar elementos: append(), insert()
        Remover elementos: remove(), pop()
        Concatenar listas: +, extend()
        Repetir listas: *
        Verificar se um item está na lista: in
"""

#1. Adicionar elementos

#a. append() - Adiciona um item ao final da lista:
frutas = ["maçã", "banana"]
frutas.append("cereja")
print(frutas)  # Saída: ['maçã', 'banana', 'cereja']

#b. insert() - Insere um item em uma posição específica:
frutas = ["maçã", "banana", "cereja"]
frutas.insert(1, "abacate")  # Insere "abacate" na posição de índice 1
print(frutas)  # Saída: ['maçã', 'abacate', 'banana', 'cereja']


#2. Remover elementos

#a. remove() - Remove o primeiro item da lista que tem o valor especificado:
frutas = ["maçã", "banana", "cereja"]
frutas.remove("banana")
print(frutas)  # Saída: ['maçã', 'cereja']

#b. pop() - Remove o item da posição especificada (ou o último 
#item, se o índice não for especificado):
frutas = ["maçã", "banana", "cereja"]
frutas.pop(1)  # Remove o item de índice 1
print(frutas)  # Saída: ['maçã', 'cereja']

frutas.pop()  # Remove o último item
print(frutas)  # Saída: ['maçã']

#3. Concatenar listas

#a. + - Une duas listas:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
uniao = lista1 + lista2
print(uniao)  # Saída: [1, 2, 3, 4, 5, 6]

#b. extend() - Adiciona os elementos de uma 
#lista (ou qualquer iterável) ao final da lista atual:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)  # Saída: [1, 2, 3, 4, 5, 6]

#4. Repetir listas

#* - Repete a lista um número específico de vezes:
repeticao = ["a", "b"] * 3
print(repeticao)  # Saída: ['a', 'b', 'a', 'b', 'a', 'b']

#5.  Verificar se um item está na lista

#in - Retorna True se um elemento está presente na lista, 
#caso contrário retorna False:
frutas = ["maçã", "banana", "cereja"]
print("banana" in frutas)  # Saída: True
print("uva" in frutas)     # Saída: False

"""
Estes são exemplos práticos de operações básicas que você pode 
realizar com listas em Python. Ao dominar essas operações, você estará bem 
equipado para manipular e trabalhar com listas de forma eficaz.
"""
print()

"""
Exercício: Operações Básicas com Listas

Objetivo: Familiarizar-se com operações fundamentais em listas, como 
adicionar, remover elementos, concatenar listas, repetir e verificar a presença de um item.

Instruções:

    1. Comece com uma lista vazia chamada animais.

    2. Adicione os seguintes animais à lista usando o método 
    append(): "gato", "cachorro" e "pássaro".

    3. Insira "peixe" na segunda posição da lista usando 
    o método insert().

    4. Remova "gato" da lista usando o método remove().

    5. Remova o último animal da lista usando o método pop() e armazene-o 
    em uma variável chamada animal_removido.

    6. Crie uma segunda lista chamada novos_animais com os 
    valores "tartaruga" e "hamster".

    7. Concatene as duas listas (animais e novos_animais) usando o 
    operador + e armazene o resultado na lista todos_animais.

    8. Duplique os elementos da lista todos_animais usando o 
    operador * e armazene o resultado em animais_duplicados.

    9. Verifique se "cachorro" está na lista todos_animais usando o 
    operador in e imprima o resultado.
"""

#Solução:

#1. Comece com uma lista vazia chamada animais.
animais = []
print(animais)

#2. Adicione os seguintes animais à lista usando o método 
#append(): "gato", "cachorro" e "pássaro".
animais.append("gato")
animais.append("cachorro")
animais.append("pássaro")
print(animais)

#3. Insira "peixe" na segunda posição da lista usando 
#o método insert().
animais.insert(1, "peixe")
print(animais)

#4. Remova "gato" da lista usando o método remove().
animais.remove("gato")
print(animais)

#5. Remova o último animal da lista usando o método pop() e armazene-o 
#em uma variável chamada animal_removido.
animal_removido = animais.pop() # Remove o último item
print(animais)
print(animal_removido)

#6. Crie uma segunda lista chamada novos_animais com os 
#valores "tartaruga" e "hamster".
novos_animais = ["tartaruga", "hamster"]
print(novos_animais)

#7. Concatene as duas listas (animais e novos_animais) usando o 
#operador + e armazene o resultado na lista todos_animais.
todos_animais = animais + novos_animais
print(todos_animais)

#8. Duplique os elementos da lista todos_animais usando o 
#operador * e armazene o resultado em animais_duplicados.
animais_duplicados = todos_animais * 2
print(animais_duplicados)

#9. Verifique se "cachorro" está na lista todos_animais usando o 
#operador in e imprima o resultado.

if "cachorro" in todos_animais:
    
    print("Cachorro está na lista!")
    
else:
    
    print("Cachorro não está na lista!")

"""
Métodos de Listas
        sort(): ordena a lista in-place.
        reverse(): inverte a ordem dos elementos in-place.
        count(): conta o número de ocorrências de um elemento.
        index(): retorna o índice da primeira ocorrência de um elemento.
"""

#Métodos de Listas

#Suponhamos que temos uma lista de números e uma lista de frutas:
numeros = [23, 1, 45, 6, 12]
frutas = ["banana", "maçã", "banana", "cereja", "maçã", "damasco"]

#1. sort(): ordena a lista in-place

#O método sort() ordena os itens da lista em uma ordem crescente por 
#padrão. Para números, isso é uma ordem numérica e para strings, é uma ordem alfabética.
print(numeros)
numeros.sort()
print(numeros)  # Saída: [1, 6, 12, 23, 45]

print()

print(frutas)
frutas.sort()
print(frutas)  # Saída: ['banana', 'banana', 'cereja', 'damasco', 'maçã', 'maçã']

print()

#Para ordenar em ordem decrescente, podemos usar o argumento reverse=True:
numeros.sort(reverse=True)
print(numeros)  # Saída: [45, 23, 12, 6, 1]

#2. reverse(): inverte a ordem dos elementos in-place.

print("\n-------------\n")

#O método reverse() simplesmente inverte a ordem dos elementos da lista.
numeros.reverse()
print(numeros)  # Saída: [1, 6, 12, 23, 45] (supondo que estivesse em ordem decrescente antes de chamarmos reverse())

frutas.reverse()
print(frutas)  # Saída: ['maçã', 'maçã', 'damasco', 'cereja', 'banana', 'banana']

#3. count(): conta o número de ocorrências de um elemento.

#O método count() retorna o número de vezes que um elemento aparece na lista.
ocorrencias_banana = frutas.count("banana")
print(ocorrencias_banana) # Saída 2

ocorrencias_numero_6 = numeros.count(6)
print(ocorrencias_numero_6) #Saída 1

#4. index(): retorna o índice da primeira ocorrência de um elemento.

#O método index() retorna o índice da primeira ocorrência do elemento 
#especificado. Se o elemento não estiver presente, ele gerará um erro.
indice_banana = frutas.index("banana")
print(indice_banana)  # Saída: 4 (pois nós invertemos a lista anteriormente com reverse())

indice_23 = numeros.index(23)
print(indice_23) #Saída: 3

"""
Esses são os métodos fundamentais das listas em Python e seus usos 
práticos. Ao trabalhar com listas, é útil estar familiarizado(a) com esses 
métodos, pois eles são frequentemente empregados para manipulação e análise de dados.
"""
print()

"""
Exercício: Métodos de Listas

Objetivo: Aprofundar a compreensão sobre os métodos específicos das listas em Python.

Instruções:

    1. Crie uma lista chamada números contendo os 
    valores: 23, 11, 89, 34, 11, 56, 78, 90, 23, 45.

    2. Ordene a lista em ordem crescente usando o 
    método sort() e imprima o resultado.

    3. Use o método reverse() para inverter a ordem dos elementos 
    da lista e imprima o resultado.

    4. Conte quantas vezes o número 11 aparece na lista usando o 
    método count() e imprima o resultado.

    5. Encontre o índice da primeira ocorrência do número 78 usando o 
    método index() e imprima o resultado.

    6. Tente encontrar o índice de um número que não está na 
    lista (por exemplo, 100) e capture a exceção usando um 
    bloco try-except para exibir uma mensagem amigável.
"""

#Solução:

#1. Crie uma lista chamada números contendo os 
#valores: 23, 11, 89, 34, 11, 56, 78, 90, 23, 45.
numeros = [23, 11, 89, 34, 11, 56, 78, 90, 23, 45]

print(f"Lista normal: {numeros}")

#2. Ordene a lista em ordem crescente usando o 
#método sort() e imprima o resultado.
numeros.sort()

print(f"Lista ordenada: {numeros}")

#3. Use o método reverse() para inverter a ordem dos elementos 
#da lista e imprima o resultado.
numeros.reverse()

print(f"Lista invertida: {numeros}")

#4. Conte quantas vezes o número 11 aparece na lista usando o 
#método count() e imprima o resultado.
contagem = numeros.count(11)

print(f"O número 11 aparece {contagem} vezes na lista.")

#5. Encontre o índice da primeira ocorrência do número 78 usando o 
#método index() e imprima o resultado.
indice = numeros.index(78)

print(f"O número 78 aparece pela primeira vez no indice {indice}.")

#6. Tente encontrar o índice de um número que não está na 
#lista (por exemplo, 100) e capture a exceção usando um 
#bloco try-except para exibir uma mensagem amigável.

try:
    
    indice_nao_existente = numeros.index(100)
    
    print(indice_nao_existente)
    
except ValueError:
    
    print("O número 100 não está na lista.")
    


"""
Slicing de Listas
        Como acessar subconjuntos de listas: minha_lista[1:3]
        Omissão de índices iniciais ou finais: minha_lista[:2], minha_lista[2:]
        Slicing com passos: minha_lista[::2]
        
O "slicing" (fatiamento) é uma maneira poderosa de acessar subconjuntos de 
listas. 

Vamos explorar isso com exemplos práticos."""

#Considere a seguinte lista para nossos exemplos:
minha_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#licing de Listas
#1. Como acessar subconjuntos de listas

#Para obter um subconjunto de elementos da lista, especificamos os 
#índices de início e fim separados por dois pontos :. Lembre-se de que o índice 
#de início é inclusivo, enquanto o índice de término é exclusivo.

subconjunto = minha_lista[1:4]
print(subconjunto)  # Saída: [1, 2, 3]

#2. Omissão de índices iniciais ou finais

#Se omitirmos o índice inicial, o Python começará o fatiamento desde o início 
#da lista. Se omitirmos o índice final, ele continuará até o final da lista.
# Pega todos os elementos até o índice 2 (exclusivo)

primeiros_elementos = minha_lista[:2]
print(primeiros_elementos)  # Saída: [0, 1]

# Pega todos os elementos a partir do índice 2
elementos_depois_do_indice_2 = minha_lista[2:]
print(elementos_depois_do_indice_2) # Saída: [2, 3, 4, 5, 6, 7, 8, 9]

#3. Slicing com passos

#Podemos também especificar um passo (ou incremento) para o fatiamento. 
#Por exemplo, um passo de 2 pegaria todos os outros elementos.
# Pega todos os elementos com um passo de 2 (pegando alternadamente)

elementos_alternados = minha_lista[::2]
print(elementos_alternados)  # Saída: [0, 2, 4, 6, 8]

# Podemos combinar isso com índices iniciais e finais também
subconjunto_alternado = minha_lista[2:8:2]
print(subconjunto_alternado)  # Saída: [2, 4, 6]

"""
Vamos detalhar a operação de slicing minha_lista[2:8:2].

No slicing, o formato geral é lista[início:fim:passo].

    Início (início): É onde o slicing começa. Se especificado, como neste 
    caso, o slice começará neste índice.

    Fim (fim): É onde o slicing termina, mas é exclusivo, o que significa que 
    o índice de término especificado não será incluído no slice.

    Passo (passo): É o intervalo entre os índices. Isso define de quantos em 
    quantos índices a lista será "fatiada".

Usando a nossa lista exemplo:
minha_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Quando fazemos:
subconjunto = minha_lista[2:8:2]

Isso pode ser lido como: "A partir da lista minha_lista, pegue todos os elementos 
começando no índice 2 até o índice 8 (mas não inclua o índice 8) em intervalos de 2 índices."

Então, isso nos dá:

    minha_lista[2] é 2
    minha_lista[4] é 4 (pulamos o índice 3 por causa do passo de 2)
    minha_lista[6] é 6 (novamente pulamos o índice 5 por causa do passo de 2)

Assim, o subconjunto resultante será: [2, 4, 6]
"""


"""
O "slicing" de listas em Python é uma ferramenta extremamente útil, que 
permite manipular e acessar os dados de maneiras versáteis. Dominar essa técnica 
pode facilitar significativamente muitas operações de manipulação de dados.
"""
print()

"""
Exercício: Slicing de Listas

Objetivo: Familiarizar-se com o conceito de "slicing" em listas, acessando 
subconjuntos de listas e utilizando passos para selecionar elementos específicos.

Instruções:

    1. Crie uma lista chamada cores com os seguintes 
    elementos: "vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza".

    2. Acesse e imprima as cores "verde" e "azul" usando slicing.

    3. Imprima as duas primeiras cores da lista utilizando slicing.

    4. Imprima todas as cores a partir da cor "amarelo" usando slicing.

    5. Imprima todas as cores em posições ímpares na 
    lista (ou seja, "vermelho", "azul", "laranja", "marrom") usando slicing com passos.

    6. Inverta a ordem das cores na lista usando slicing e imprima o resultado.
"""

#Solução:

#1. Crie uma lista chamada cores com os seguintes 
#elementos: "vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza".
cores = ["vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza"]
print(f"Lista de cores: {cores}")

#2. Acesse e imprima as cores "verde" e "azul" usando slicing.
subconjunto = cores[1:3]

print(f"Cores entre verde e azul: {subconjunto}")

#3. Imprima as duas primeiras cores da lista utilizando slicing.
primeiras = cores[:2]

print(f"As duas primeiras cores são: {primeiras}")

#4. Imprima todas as cores a partir da cor "amarelo" usando slicing.
a_partir_amarelo = cores[3:]

print(f"Cores a partir do amarelo: {a_partir_amarelo}")

#5. Imprima todas as cores em posições ímpares na 
#lista (ou seja, "vermelho", "azul", "laranja", "marrom") usando slicing com passos.

cores_impares = cores[::2]

print(f"Cores em posição impares: {cores_impares}")

#6. Inverta a ordem das cores na lista usando slicing e imprima o resultado.

inverso = cores[::-1]
print(f"Cores na ordem inversa: {inverso}")

"""
List Comprehensions
        Uma maneira concisa de criar listas: [x**2 for x in range(10) if x % 2 == 0]
        
"List Comprehensions" são uma das características mais úteis e elegantes de Python. 

Elas oferecem uma maneira concisa de criar listas, e são frequentemente 
mais compreensíveis e mais eficientes do que usar loops."""

#1. Exemplo básico:

#Vamos começar com um exemplo simples. Imagine que queremos 
#criar uma lista dos quadrados dos números de 0 a 9:
quadrados = [x**2 for x in range(10)]
print(quadrados)
# Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Exemplo básico e tradicional

# Inicializando uma lista vazia chamada "quadrados"
quadrados = []

# Loop através de números de 0 a 9 (pois range(10) gera números de 0 até 9)
for x in range(10):
    
    # Calculando o quadrado do número atual e adicionando à lista "quadrados"
    quadrados.append(x**2)

# Imprimindo a lista "quadrados"
print(quadrados)

#-----------------------------------------------------

print()

#2. Tradicional

#Se quisermos criar uma lista dos quadrados dos números, mas apenas para os números pares de 0 a 9:
quadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(quadrados_pares)
# Saída: [0, 4, 16, 36, 64]

#Aqui, x % 2 == 0 é uma condição que verifica se o número é par. Portanto, 
#estamos pegando o quadrado de x apenas para valores de x que são pares.

#Exemplo Com condicional e tradicional

# Inicializando uma lista vazia chamada "quadrados_pares"
quadrados_pares = []

# Loop através de números de 0 a 9 (pois range(10) gera números de 0 até 9)
for x in range(10):
    
    # Verificando se o número atual é par
    if x % 2 == 0:
        
        # Calculando o quadrado do número par atual e adicionando à lista "quadrados_pares"
        quadrados_pares.append(x**2)

# Imprimindo a lista "quadrados_pares"
print(quadrados_pares)

#------------------------------------------------------

print()

#3. Exemplo adicional com duas variáveis:

#Vamos supor que temos duas listas de números e queremos criar uma 
#lista de todos os pares possíveis de números que somam 5:
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

combinacoes = [(x, y) for x in a for y in b if x + y == 5]
print(combinacoes)

# Definindo duas listas a e b
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

# Inicializando uma lista vazia chamada "combinacoes"
combinacoes = []

# Loop através de cada elemento em 'a'
for x in a:
    
    # Loop através de cada elemento em 'b'
    for y in b:
        
        # Verificando se a soma de x e y é igual a 5
        if x + y == 5:
            
            # Se for verdade, adiciona a combinação (x, y) à lista "combinacoes"
            combinacoes.append((x, y))

# Imprimindo a lista "combinacoes"
print(combinacoes)

        

"""
Exercício: List Comprehensions

Objetivo: Familiarizar-se com a criação de listas usando a notação 
concisa de "List Comprehensions" em Python.

Instruções:

    1. Use uma list comprehension para criar uma lista dos dez primeiros 
    números elevados ao cubo e imprima o resultado.

    2. Use uma list comprehension para criar uma lista contendo todos os números 
    de 1 a 20 que são divisíveis por 3. Imprima o resultado.

    3. Dada a lista de palavras frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"], 
    use uma list comprehension para criar uma lista com as frutas que possuem mais de 5 caracteres. 
    Imprima o resultado.

    4. Dada a lista notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82], use 
    uma list comprehension para obter todas as notas acima de 75 e imprima o resultado.
"""

#Solução:

#1. Use uma list comprehension para criar uma lista dos dez primeiros 
#números elevados ao cubo e imprima o resultado.

cubos = [x**3 for x in range(10)]
print(f"Os dez primeiros números elevados ao cubo: {cubos}")


#Exemplo tradicional

# Inicializando uma lista vazia chamada "cubos"
cubos = []

# Loop através de números de 0 a 9 (pois range(10) gera números de 0 até 9)
for x in range(10):
    
    # Calculando o cubo do número atual e adicionando à lista "cubos"
    cubos.append(x**3)

# Imprimindo a lista "cubos" formatada
print(f"Os dez primeiros números elevados ao cubo: {cubos}")


#2. Use uma list comprehension para criar uma lista contendo todos os números 
#de 1 a 20 que são divisíveis por 3. Imprima o resultado.

divisiveis_por_3 = []

#Exemplo tradicional

divisiveis_por_3 = [x for x in range(1, 21) if x % 3 == 0]
print(f"Números de 1 a 20 divisíveis por 3: {divisiveis_por_3}")

#Exemplo tradicional

# Inicializando uma lista vazia chamada "divisiveis_por_3"
divisiveis_por_3 = []

# Loop através de números de 1 a 20 (pois range(1, 21) gera números de 1 até 20)
for x in range(1, 21):
    
    # Verificando se o número atual é divisível por 3
    if x % 3 == 0:
        
        # Se for verdade, adiciona o número à lista "divisiveis_por_3"
        divisiveis_por_3.append(x)

# Imprimindo a lista "divisiveis_por_3" formatada
print(f"Números de 1 a 20 divisíveis por 3: {divisiveis_por_3}")       
        

print()

#3. Dada a lista de palavras frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"], 
#use uma list comprehension para criar uma lista com as frutas que possuem mais de 5 caracteres. 
#Imprima o resultado.



frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"]

frutas_longas = [fruta for fruta in frutas if len(fruta) > 5]

print(f"Frutas com mais de 5 caracteres: {frutas_longas}")

#Exemplo tradicional

# Inicializando uma lista vazia chamada "frutas_longas"
frutas_longas = []

# Loop através de cada fruta na lista "frutas"
for fruta in frutas:
    
    # Verificando se o comprimento da fruta atual é maior que 5
    if len(fruta) > 5:
        
        # Se for verdade, adiciona a fruta à lista "frutas_longas"
        frutas_longas.append(fruta)

# Imprimindo a lista "frutas_longas" formatada
print(f"Frutas com mais de 5 caracteres: {frutas_longas}")

#--------------------------------------------------------

print()


#4. Dada a lista notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82], use 
#uma list comprehension para obter todas as notas acima de 75 e imprima o resultado.

notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82]
notas_altas = [nota for nota in notas if nota > 75]
print(f"Notas acima de 75: {notas_altas}")

#Exemplo tradicional

# Inicializando uma lista vazia chamada "notas_altas"
notas_altas = []

# Loop através de cada nota na lista "notas"
for nota in notas:
    
    # Verificando se a nota atual é maior que 75
    if nota > 75:
        
        # Se for verdade, adiciona a nota à lista "notas_altas"
        notas_altas.append(nota)

# Imprimindo a lista "notas_altas" formatada
print(f"Notas acima de 75: {notas_altas}")


"""
Listas Aninhadas (listas de listas)
        Criando e acessando listas dentro de listas.
        Utilizando loops aninhados para iterar sobre elas.
        
Listas aninhadas, ou listas de listas, são basicamente listas que 
têm outras listas como seus elementos. Elas são úteis em muitas situações, 
especialmente ao representar estruturas bidimensionais como matrizes.

"""

#1. Criando Listas Aninhadas:

#Vamos considerar que queremos representar uma matriz 3x3:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Aqui, matriz é uma lista de 3 elementos, onde cada elemento é, por sua vez, uma lista de 3 números.

#2. Acessando Listas Aninhadas:

#Para acessar um elemento específico, você precisa especificar dois índices: o índice 
#da lista externa e o índice da lista interna.

#Por exemplo, para acessar o número 5:
elemento = matriz[1][1]
print(elemento)

#O primeiro índice [1] refere-se à segunda lista [4, 5, 6], e o segundo 
#índice [1] refere-se ao segundo elemento dessa lista, que é 5.

#3. Utilizando Loops Aninhados para Iterar:

# Para iterar sobre cada elemento da matriz, usamos loops for aninhados:
# Loop externo: itera sobre cada linha da matriz
for linha in matriz:
    
    # Loop interno: itera sobre cada número (ou elemento) dentro da linha atual
    for numero in linha:
        
        # Imprime o número atual seguido por um espaço, sem mudar de linha devido ao parâmetro "end=' '"
        print(numero, end=' ')
    
    # Uma vez que todos os números de uma linha são impressos, esta linha imprime uma quebra de linha
    # para separar visualmente as linhas da matriz ao imprimir
    print()  

#Aqui, o loop externo itera sobre cada linha da matriz, enquanto o loop 
#interno itera sobre cada numero dentro da respectiva linha.



#4. Exemplo Prático:

#Vamos supor que queremos calcular a transposta dessa matriz. 
#A transposta de uma matriz é obtida trocando suas linhas por colunas:

# Inicializando uma lista vazia chamada "transposta"
transposta = []

# Loop através de cada coluna da matriz original
for i in range(len(matriz[0])):
    
    # Inicializa uma linha temporária para construir uma linha da matriz transposta
    linha_temporaria = []
    
    # Loop através de cada linha da matriz original
    for j in range(len(matriz)):
        
        # Adiciona o elemento da posição j,i (transposto) à linha temporária
        linha_temporaria.append(matriz[j][i])
        
    # Adiciona a linha temporária completa à matriz transposta
    transposta.append(linha_temporaria)

"""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""

"""
Exercício: Listas Aninhadas

Objetivo: Aprofundar o entendimento sobre listas dentro de listas e como interagir com elas usando loops aninhados.

Instruções:

    Crie uma matriz 3x3 chamada matriz com os seguintes valores:
    
1, 2, 3
4, 5, 6
7, 8, 9

Represente essa matriz como uma lista de listas.

1. Acesse e imprima o valor localizado na segunda linha e terceira coluna (deve ser o número 6).

2. Utilizando loops aninhados, calcule e imprima a soma de todos os valores presentes na matriz.

3. Usando loops aninhados, imprima a matriz linha por linha, e cada elemento separado por uma tabulação (\t).

Valor na segunda linha e terceira coluna: 6
Soma dos valores da matriz: 45
Matriz:
1	2	3	
4	5	6	
7	8	9	

Esse exercício oferece uma prática abrangente sobre a interação com listas 
aninhadas e a manipulação de elementos dentro de matrizes.

"""

#Solução

#Crie uma matriz 3x3 chamada matriz com os seguintes valores:

#Vamos considerar que queremos representar uma matriz 3x3:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#1. Acesse e imprima o valor localizado na 
#segunda linha e terceira coluna (deve ser o número 6).

valor = matriz[1][2]

print(f"Valor na segunda linha e terceira coluna: {valor}") # Saída: 6

#2. Utilizando loops aninhados, calcule e imprima a soma de todos
#os valores presentes na matriz.

# Inicializando a variável "soma" com 0. Esta variável armazenará a soma total de todos os números na matriz.
soma = 0

# Loop externo: itera sobre cada linha da matriz
for linha in matriz:
    
    # Loop interno: itera sobre cada número (ou elemento) dentro da linha atual
    for numero in linha:
        
        # Adiciona o valor do número atual à variável "soma"
        #soma = soma + numero
        soma += numero

# Após a conclusão dos loops, a variável "soma" contém a soma total de todos os números da matriz.
print(f"Soma dos valores da matriz: {soma}")  # Saída: 45

print()

#3. Usando loops aninhados, imprima a matriz linha por linha, 
#e cada elemento separado por uma tabulação (\t).

print("Matriz:")

# Loop externo: itera sobre cada linha da matriz
for linha in matriz:

    # Loop interno: itera sobre cada número (ou elemento) dentro da linha atual
    for numero in linha:
    
        # Imprime o número atual seguido por uma tabulação (representada por "\t"), 
        # mantendo os números na mesma linha ao imprimir
        print(numero, end="\t")
    
    # Uma vez que todos os números de uma linha são impressos, 
    # esta linha imprime uma quebra de linha para separar as linhas da matriz visualmente ao imprimir
    print()  




"""
Utilidades e Funções com Listas
        len(): retorna o número de elementos na lista.
        max(): retorna o maior valor.
        min(): retorna o menor valor.
        sum(): retorna a soma dos elementos.
"""

#Exemplo Prático:

#Considere a seguinte lista de números:
numeros = [6, 3, 8, 15, 2, 7, 14]
print(numeros)

#len() - Contando o número de elementos:

#Esta função retorna o número de elementos na lista.
tamanho = len(numeros)
print(f"O número de elementos na lista é: {tamanho}")


#max(): retorna o maior valor.

#Esta função retorna o maior valor na lista.
maior_valor = max(numeros)
print(f"O maior valor na lista é: {maior_valor}")


#min(): retorna o menor valor.

#Esta função retorna o menor valor na lista.
menor_valor = min(numeros)
print(f"O menor valor na lista é: {menor_valor}")

#sum() - Somando os elementos:

#Esta função retorna a soma total dos elementos na lista.
soma_total = sum(numeros)
print(f"A soma dos elementos na lista é: {soma_total}")

"""
Juntas, essas funções oferecem uma maneira rápida e eficaz 
de obter informações básicas sobre os conteúdos de uma lista em Python.
"""
print()


"""
Exercício: Utilidades e Funções com Listas

Objetivo: Compreender e aplicar funções úteis que interagem 
com listas em Python.

Instruções:

    Dada a lista valores = [23, 45, 67, 89, 12, 56, 78, 90, 34, 56], determine 
    e imprima o número de elementos na lista usando a função len().

    Ainda utilizando a lista valores, encontre e imprima o maior e o menor valor 
    presente na lista usando as funções max() e min().

    Calcule e imprima a soma de todos os elementos na lista valores 
    usando a função sum().

    Crie uma lista pesos com os seguintes valores: 58.5, 63.2, 71.3, 69.4, 68.2. 
    Calcule e imprima a média dos pesos usando as funções sum() e len().
"""

#Solução:

#Dada a lista valores = [23, 45, 67, 89, 12, 56, 78, 90, 34, 56], determine 
#e imprima o número de elementos na lista usando a função len().

valores = [23, 45, 67, 89, 12, 56, 78, 90, 34, 56]
print(valores)

numero_elementos = len(valores)
print(f"O número de elementos na lista de valores é: {numero_elementos}")

#Ainda utilizando a lista valores, encontre e imprima o maior e o menor valor 
#presente na lista usando as funções max() e min().

maior_valor = max(valores)
menor_valor = min(valores)

print(f"O maior valor na lista de valores é: {maior_valor}")
print(f"O menor valor na lista de valores é: {menor_valor}")

#Calcule e imprima a soma de todos os elementos na lista valores 
#usando a função sum().

soma_valores = sum(valores)

print(f"A som dos elementos da lista de valores é: {soma_valores}")

#Crie uma lista pesos com os seguintes valores: 58.5, 63.2, 71.3, 69.4, 68.2. 
#Calcule e imprima a média dos pesos usando as funções sum() e len().

print()
pesos = [58.5, 63.2, 71.3, 69.4, 68.2]

print(pesos)

media_pesos = sum(pesos) / len(pesos)

print(f"A média dos pesos é: {media_pesos:.2f}")

"""
Iteração em Listas
        Usando o loop for.
        Usando enumerate() para obter índice e valor ao iterar.
"""

#Exemplo prático

#Vamos considerar a seguinte lista de frutas:
frutas = ["maçã", "banana", "cereja", "damasco", "figo"]

#Usando o loop for para iterar sobre os valores da lista:

#Neste exemplo, vamos imprimir cada fruta da lista.
for fruta in frutas:
    
    print(fruta)
    
#Usando enumerate() para obter índice e valor ao iterar:

#A função enumerate() retorna tanto o índice quanto o valor ao iterar 
#sobre uma lista. Isso é útil quando você quer saber a posição (índice) 
#de cada item na lista enquanto itera.

for indice, fruta in enumerate(frutas):
    print(f"Fruta no índice {indice} é {fruta}")


"""
Nota: Em Python, a indexação começa em 0, então a primeira 
fruta "maçã" está no índice 0, a segunda "banana" no índice 1 e assim por diante.

Com essas técnicas, você pode facilmente iterar sobre listas em Python, acessando 
não apenas os valores dos itens, mas também seus índices.
"""
print()


"""
Exercício: Iteração em Listas

Objetivo: Familiarizar-se com a iteração através de listas usando o 
loop for e a função enumerate() para acessar o índice e o valor dos elementos.

Instruções:

    Dada a lista nomes = ["Alice", "Bruno", "Clara", "Daniel", "Eduarda"], use um 
    loop for para imprimir cada nome na lista.

    Utilizando a mesma lista nomes, imprima o nome juntamente com a sua posição na 
    lista (índice). Para isso, utilize a função enumerate().

    Dada a lista notas = [85, 90, 78, 92, 88], use a função enumerate() para imprimir o 
    nome do aluno da lista nomes e a sua respectiva nota da lista notas.
    
Este exercício permite praticar a iteração em listas e combinar informações 
de múltiplas listas usando índices, tudo isso enquanto se familiarizam com a função útil enumerate().

"""

#Solução:

#Dada a lista nomes = ["Alice", "Bruno", "Clara", "Daniel", "Eduarda"], use um 
#loop for para imprimir cada nome na lista.

nomes = ["Alice", "Bruno", "Clara", "Daniel", "Eduarda"]

print(nomes)

for nome in nomes:
    
    print(nome)

#Utilizando a mesma lista nomes, imprima o nome juntamente com a sua posição na 
#lista (índice). Para isso, utilize a função enumerate().

print()

for indice, nome in enumerate(nomes):
    
    print(f"{indice + 1}: {nome}")

#Dada a lista notas = [85, 90, 78, 92, 88], use a função enumerate() para imprimir o 
#nome do aluno da lista nomes e a sua respectiva nota da lista notas.

notas = [85, 90, 78, 92, 88]

print()

print(notas)
print(nomes)

for indice, nome in enumerate(nomes):
    
    print(f"{nome} obteve nota {notas[indice]}")

"""
Listas e Strings
        Conversão de strings para listas: list(), split().
        Conversão de listas para strings: join().
"""

#Exemplo prático

#Conversão de strings para listas

#A) Usando list():

#Ao usar a função list() em uma string, cada caractere da string 
#será um elemento da lista resultante.
s = "olá"
lista_s = list(s)
print(lista_s)  # Saída: ['o', 'l', 'á']

#B) split():

#A função split() é usada para dividir uma string em uma lista com 
#base em um delimitador especificado. Se nenhum delimitador for especificado, ela 
#dividirá a string nos espaços em branco.
frase = "Python é divertido"
palavras = frase.split()
print(palavras)  # Saída: ['Python', 'é', 'divertido']

data = "12/10/2023"
elementos_data = data.split("/")
print(elementos_data)

#Conversão de listas para strings

#Usando join():

print()

#A função join() é usada para converter uma lista em uma string. Ela une 
#os elementos de uma lista em uma única string com base em um delimitador especificado.
lista_palavras = ['Python', 'é', 'incrível']

frase_juntada = ' '.join(lista_palavras)
print(frase_juntada)  # Saída: "Python é incrível"

lista_data = ["25", "12", "2023"]

print(lista_data)

data_juntada = '/'.join(lista_data)
print(data_juntada)

"""
Essas são operações comuns quando estamos trabalhando com processamento de texto 
ou manipulação de dados em Python. Conhecer como converter entre strings e 
listas é essencial para muitas tarefas!
"""
print()

"""
Exercício: Listas e Strings

Objetivo: Familiarizar-se com as operações de conversão entre 
listas e strings, usando métodos como list(), split(), e join().

Instruções:

    Dada a string palavra = "Python", converta-a para uma lista de 
    caracteres e imprima a lista resultante. Use o método list() para isso.

    Dada a frase frase = "Aprendendo Python é divertido!", divida-a em uma 
    lista de palavras e imprima a lista resultante. Utilize o método split().

    Usando a lista do Passo 2, junte as palavras para formar a frase original 
    novamente e imprima-a. Utilize o método join().

    Dada a lista itens = ["maçã", "banana", "cereja"], converta-a em uma string onde 
    cada item é separado por uma vírgula e um espaço e imprima a string resultante. 
    
    Por exemplo: "maçã, banana, cereja".
    
Saída esperada:

Lista de caracteres: ['P', 'y', 't', 'h', 'o', 'n']
Lista de palavras: ['Aprendendo', 'Python', 'é', 'divertido!']
Frase reconstruída: Aprendendo Python é divertido!
String de itens: maçã, banana, cereja

Este exercício ajuda os alunos a entender e praticar as transformações 
entre listas e strings, utilizando os métodos comuns para tais operações.
"""

#Solução:

#Dada a string palavra = "Python", converta-a para uma lista de 
#caracteres e imprima a lista resultante. Use o método list() para isso.

palavra = "Python"

lista_palavra = list(palavra)

print("Lista de caracteres:", lista_palavra)

#Dada a frase frase = "Aprendendo Python é divertido!", divida-a em uma 
#lista de palavras e imprima a lista resultante. Utilize o método split().

frase = "Aprendendo Python é divertido!"

lista_palavras = frase.split()

print("Lista de palavras:", lista_palavras)

#Usando a lista do Passo 2, junte as palavras para formar a frase original 
#novamente e imprima-a. Utilize o método join().

frase_recontruida = " ".join(lista_palavras)

print("Frase resconstruída:", frase_recontruida)

#Dada a lista itens = ["maçã", "banana", "cereja"], converta-a em uma string onde 
#cada item é separado por uma vírgula e um espaço e imprima a string resultante. 

itens = ["maçã", "banana", "cereja"]

string_itens = ", ".join(itens)

print("String de itens:", string_itens)

"""
Exercício: Lista de Compras

Crie um programa em Python que permita ao usuário adicionar 
itens a uma lista de compras. O programa deve exibir um menu com as seguintes opções:

    1. Adicionar item à lista
    2. Remover item da lista
    3. Exibir lista de compras
    4. Sair

O programa deve continuar executando até que o usuário escolha a opção 4 para sair.

"""

# Inicializa a lista de compras vazia
lista_compras = []

# Loop principal para manter o programa em execução
while True:
    
    print("\nMenu:")
    print("1. Adicionar item à lista")
    print("2. Remover item da lista")
    print("3. Exibir lista de compras")
    print("4. Sair")

    # Solicita ao usuário que escolha uma opção do menu
    opcao = int(input("Escolha uma opção: "))

    # Se a opção escolhida for 1:
    if opcao == 1:
        
        # Solicita o item a ser adicionado
        item = input("Digite o item que deseja adicionar à lista: ")
        
        # Adiciona o item à lista de compras utilizando o método append()
        lista_compras.append(item)
        
        print("Item adicionado à lista!")

    # Se a opção escolhida for 2:
    elif opcao == 2:
        
        # Verifica se a lista de compras está vazia
        if len(lista_compras) == 0:
            
            print("A lista de compras está vazia.")
            
        else:
            
            # Solicita o item a ser removido
            item = input("Digite o item que deseja remover da lista: ")
            
            # Verifica se o item está presente na lista
            if item in lista_compras:
            
                # Remove o item da lista utilizando o método remove()
                lista_compras.remove(item)
                
                print("Item removido da lista!")
                
            else:
                
                print("O item não está na lista.")

    # Se a opção escolhida for 3:
    elif opcao == 3:
        
        print("\nLista de Compras:")
        
        # Itera sobre os itens da lista de compras
        for item in lista_compras:
            
            # Imprime cada item com um hífen no início
            print("-", item)

    # Se a opção escolhida for 4:
    elif opcao == 4:
        
        print("Saindo...")
        
        # Encerra o loop e sai do programa
        break

    # Se a opção escolhida não for válida:
    else:
        
        print("Opção inválida. Escolha uma opção válida.")

    # Adiciona uma linha em branco após cada operação
    print()
        

"""
Exercício: Classificação de Números

Seu desafio é escrever um programa que faça o seguinte:

    Peça ao usuário para inserir 5 números inteiros, um por um.
    Armazene esses números em uma lista.
    Classifique os números na lista em ordem crescente.
    Imprima a lista classificada.

Requisitos:

    Utilize um loop (como um for ou while) para coletar os números do usuário.
    Utilize o método append da lista para adicionar cada número à lista.
    Utilize o método sort da lista para classificar os números.

Dicas:

    Você pode utilizar um loop for com range(5) para repetir um bloco de 
    código 5 vezes, uma vez para cada número a ser inserido.

Exemplo de Saída:

Digite um número: 4
Digite um número: 2
Digite um número: 5
Digite um número: 1
Digite um número: 3
Números em ordem crescente: [1, 2, 3, 4, 5]
"""

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Usa um loop for para repetir o bloco de código 5 vezes
for i in range(5):
    
    # Pede ao usuário para inserir um número
    numero = int(input("Digite um número: "))
    
    # Adiciona o número inserido pelo usuário à lista de números
    numeros.append(numero)

# Classifica os números na lista em ordem crescente
numeros.sort()

# Imprime a lista classificada
print("Números em ordem crescente:", numeros)













