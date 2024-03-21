"""
O que é uma variável?

Uma variável é um nome que se refere a um valor armazenado na memória do computador. 
Em programação, as variáveis são usadas para armazenar dados que podem ser utilizados 
e manipulados ao longo de um programa.

Em Python, as variáveis não são declaradas com um tipo específico. 

No entanto, os tipos de dados que você pode armazenar em uma variável incluem:
"""

#Principais tipos de variaveis

#Inteiros (int): Números inteiros, sem parte decimal.
inteiro = 42
print("Inteiro:", inteiro)

#Ponto Flutuante (float): Números reais, que têm uma parte decimal.
flutuante = 42.0
print("Flutuante:", flutuante)

#Complexos (complex): Números complexos, que têm uma parte real e uma parte imaginária.
complexo = 3 + 4j
print("Complexo:", complexo)

#Strings (str): Sequências de caracteres.
texto = "Olá, Mundo!"
print("Texto:", texto)


"""
Os termos "mutável" e "imutável" referem-se à capacidade de alterar o conteúdo 
de um objeto depois que ele foi criado.

Mutável: Significa que o conteúdo do objeto pode ser alterado após a sua criação. As 
listas em Python são mutáveis, o que significa que você pode modificar seus elementos.

    
Imutável: Significa que o conteúdo do objeto não pode ser alterado após a sua criação. As 
tuplas em Python são imutáveis, o que significa que, uma vez criada, você não pode modificar 
seus elementos.

"""
#Listas (list): Uma coleção ordenada e mutável.
lista = [1, 2, 3, 3]
print("Lista:", lista)

#Tuplas (tuple): Uma coleção ordenada e imutável.
tupla = (1, 2, 3, 4, 5)
print("Tupla:", tupla)

#Conjuntos (set): Uma coleção não ordenada de itens únicos.
conjunto = {1, 2, 3, 3}
print("Conjunto:", conjunto)

#Dicionários (dict): Uma coleção não ordenada de pares chave-valor.
dicionario = {"chave": "valor"}
print("Dicionário:", dicionario)

#Booleanos (bool): Valores verdadeiro ou falso.
booleano = True
print("Booleano:", booleano)

#NoneType (None): Um tipo especial que representa a ausência de valor.
nenhum = None
print("NoneType (None):", nenhum)


#Variaveis

idade = 30
nome = "Nicole"

print("Nome:", nome)
print("Idade:", idade)
print("Nome:", nome, ", Idade:", idade)

"""
idade = 30: Nesta linha, estamos declarando uma variável chamada 
idade e atribuindo o valor 30 a ela. Essa variável pode ser usada posteriormente 
no código para referenciar esse valor.

nome = "Nicole": Aqui, estamos declarando uma variável chamada nome e atribuindo 
a ela a string "Nicole". Assim como a variável idade, essa variável também pode ser 
usada posteriormente no código.

print("Nome: ", nome, " Idade: ", idade): Esta linha usa a função print para 
imprimir uma string na tela. Ela começa com a string literal "Nome: ", seguida pelo valor 
da variável nome, que é "Nicole", uma string literal com espaço e " Idade: ", e finalmente 
o valor da variável idade, que é 30.
"""


#Podemos obter o tipo de uma variável usando a função type

"""
nome = str("Ana Paula"): A string "Ana Paula" é passada para a função str(), que 
retorna a mesma string. A função str() é desnecessária neste caso, pois "Ana Paula" já 
é uma string. A variável nome é atribuída a essa string.

idade = int(31): O número inteiro 31 é passado para a função int(), que retorna o mesmo 
número. Novamente, a função int() é desnecessária aqui, pois 31 já é um inteiro. A variável idade é 
atribuída a esse valor inteiro.

print(type(nome)): A função type() retorna o tipo da variável nome, que é <class 'str'>, já que nome 
é uma string. Esse valor é então impresso, resultando na saída:

"""

nome = str("Ana Paula")
idade = 31

print(type(nome))
print(type(idade))

#As variáveis diferenciam letras maiúsculas de minúsculas

i = 30
I = "Ana"

print(i)
print(I)

#Podemos também atribuir valores a várias variáveis em uma só linha

"""
O código está utilizando a desempacotamento de tuplas para atribuir 
várias variáveis em uma única linha e, em seguida, imprimindo essas variáveis. 

var1, var2, var3, var4 = "Texto 1", "Texto 2", "Texto 3", "Texto 4":
Nesta linha, quatro strings são atribuídas a quatro variáveis respectivas 
em uma única operação. 

A variável var1 é atribuída à string "Texto 1", 
var2 à string "Texto 2", 
var3 à string "Texto 3", 
var4 à string "Texto 4".
"""
var1, var2, var3, var4 = "Texto 1", "Texto 2", "Texto 3", "Texto 4"

print(var1)
print(var2)
print(var3)
print(var4)

#Podemos atribuir o mesmo valor a várias variáveis em uma única linha

var1 = var2 = var3 = var4 = "Ana Paula"

print(var1)
print(var2)
print(var3)
print(var4)

#Se tiver uma coleção de valores em uma tupla, podemos extrair em variáveis. Isso é chamado de descompactar

exemplo = "Texto 1", "Texto 2", "Texto 3", "Texto 4"
var1, var2, var3, var4 = exemplo

print(exemplo)
print(var1)
print(var2)
print(var3)
print(var4)

#Para juntar textos e variáveis em Python usamos o caracter + ou ,

nome = "Ana Paula"

print("O nome dela é " + nome)

numero1 = "Dez"
numero2 = "Cinco"

print(numero1 + numero2)

#Para juntar textos e variáveis em Python usamos o caracter + ou ,

"""
Definindo duas variáveis, nome e sobrenome, que contêm strings. Em seguida, 
usamos a concatenação de strings para juntar essas variáveis e imprimi-las como um 
nome completo. 

    Vamos analisar cada parte:

    nome = "Thuane": Atribui a string "Thuane" à variável nome.

    sobrenome = "Alves": Atribui a string "Alves" à variável sobrenome.

    print("Nome completo: " + nome + " " + sobrenome)
    
        - "Nome completo: " é uma string literal que será o começo da saída.
        - nome é a variável que contém a string "Thuane", e ela é concatenada à string anterior.        
        - " " é uma string literal contendo um espaço, e ela é usada para separar o nome e o sobrenome na saída.
        - sobrenome é a variável que contém a string "Alves", e ela é concatenada ao restante da string.

    A concatenação dessas partes resulta na string "Nome completo: Thuane Alves", que é então impressa.
    
"""

nome = "Thuane"
sobrenome = "Alves"

print("Nome completo: " + nome + " " + sobrenome)

# Exercício de Variáveis em Python

# 1. Declare uma variável chamada "idade" e atribua o valor 25 a ela.
idade = 25

# 2. Declare uma variável chamada "nome" e atribua o valor "João" a ela.
nome = "João"

# 3. Declare uma variável chamada "saldo" e atribua o valor 100.50 a ela.
saldo = 100.50

# 4. Crie uma variável chamada "soma" e atribua a ela a soma das variáveis "idade" e "saldo".
soma = idade + saldo

# 5. Imprima na tela o valor da variável "soma".
print("A soma é:", soma)


# Exercício de Variáveis em Python

# 1. Crie uma variável chamada "nota1" e atribua o valor 7.5 a ela.
nota1 = 7.5

# 2. Crie uma variável chamada "nota2" e atribua o valor 8.3 a ela.
nota2 = 8.3

# 3. Crie uma variável chamada "nota3" e atribua o valor 6.9 a ela.
nota3 = 6.9

# 4. Calcule a média das três notas e atribua o resultado a uma variável chamada "media".
media = (nota1 + nota2 + nota3) / 3

# 5. Imprima na tela o valor da variável "media" formatado com duas casas decimais.
print("A média é:", format(media, ".2f"))


# 1. Crie uma variável chamada nome e atribua o seu nome a ela como um valor.
nome = 'Jessica'

# 2. Crie duas variáveis chamadas idade e ano_atual. 
idade = 32
ano_atual = 2024

# 3. Calcule o ano em que você nasceu.
ano_nascimento = ano_atual - idade

# 4. Incremente a variável idade em 1.
idade +=1 

# 5. Imprima as mensagens.
print(nome)
print(idade)
print(ano_atual)
print(ano_nascimento)