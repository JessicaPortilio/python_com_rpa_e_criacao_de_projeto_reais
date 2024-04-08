#Imprimindo a posição das letras

posicaoLetra = "Python"
print(posicaoLetra[0])
print(posicaoLetra[1])
print(posicaoLetra[2])
print(posicaoLetra[3])
print(posicaoLetra[4])


"""
"slicing" (fatiamento) em Python para extrair partes de uma string. 


    frase = "Olá, mundo!": Essa linha atribui a string "Olá, mundo!" à variável frase.

    parte = frase[4:8]: Isso fatia a string da posição 4 até a posição 8 (exclusiva). Em 
    Python, a indexação começa em 0, então a posição 4 é o quinto caractere da string, que é um 
    espaço, e a posição 8 é o nono caractere, que é a letra 'd'. Então, essa fatia inclui os 
    caracteres nas posições 4, 5, 6 e 7, que são " mun". O valor de parte será a string " mun".

    print(parte): Imprime o valor de parte, que é " mun".

    primeiros = frase[:5]: Isso fatia a string da posição inicial (inclusa) até a 
    posição 5 (exclusiva). Como não há um valor antes dos dois pontos, ele assume o 
    início da string. Portanto, essa fatia inclui os caracteres nas posições 0, 1, 2, 3 e 4, que 
    são "Olá,". O valor de primeiros será a string "Olá,".

    print(primeiros): Imprime o valor de primeiros, que é "Olá,".

    ultimos = frase[-6:]: Isso fatia a string da posição -6 até o final da string. Em 
    Python, índices negativos contam a partir do final da string, então a posição -6 é o sexto 
    caractere a partir do final, que é a letra 'm'. Como não há valor depois dos dois pontos, ele assume 
    o final da string. Portanto, essa fatia inclui os caracteres 'mundo!'. O valor de ultimos será a string "mundo!".

    print(ultimos): Imprime o valor de ultimos, que é "mundo!".


"""

# Slice
frase = "Olá, mundo!"

# Obtendo uma parte da string usando slice
parte = frase[4:8]
print(parte)  # Saida:  mun

# Obtendo os primeiros 5 caracteres da string
primeiros = frase[:5]
print(primeiros)  # Saida: Olá,

# Obtendo os últimos 6 caracteres da string
ultimos = frase[-6:]
print(ultimos)  # Saida: mundo!

#Verifica se a palavra python está na frase


frase = "O módulo de python é muito legal"

print("python" in frase)

"""
O operador in é usado em Python para verificar a presença de um valor dentro 
de uma sequência (como uma string, lista, ou tupla). Neste caso, está sendo 
usado para verificar se uma determinada substring está contida em uma string maior.
"""

#verifica se a palavra python está na frase
frase = "O módulo de python é muito legal"

#if - se
if "python" in frase:
    print("Sim, a palavra python está presente na frase.")



#strip - Usamos para remover espaços em branco do inicio e do final da frase

frase = "        O módulo de python é muito legal       "

print(frase.strip())


"""
O uso do método split em uma string, que é uma maneira útil de dividir uma string em uma 
lista de substrings com base em um determinado separador.

    frase = "Olá, como vai você?": Essa linha atribui a string "Olá, como vai você?" à variável frase.

    palavras = frase.split(): O método split é chamado na string frase sem qualquer argumento, o que 
    significa que ele usará espaços em branco como o separador padrão. A string original é dividida onde 
    quer que haja um espaço, e as partes resultantes são retornadas como uma lista de strings. Neste caso, 
    a lista resultante será ['Olá,', 'como', 'vai', 'você?'].

    print(palavras): Esta linha imprime a lista de palavras que foi criada, resultando na saída:

     ['Olá,', 'como', 'vai', 'você?']

O método split é frequentemente usado para dividir uma string em palavras ou em partes menores 
com base em um delimitador específico.

"""


#split, join e strip são métodos muito úteis da str
frase = "Olá, como vai você?"
palavras = frase.split()  # Dividindo a frase em palavras usando o espaço em branco como separador
print(palavras)
# Saída: ['Olá,', 'como', 'vai', 'você?']


"""
método join, que é o oposto do método split que você viu anteriormente. Ele é usado para juntar 
uma lista de strings em uma única string, usando um delimitador específico. 


    palavras = ['Olá,', 'como', 'vai', 'você?']: Essa linha cria uma lista chamada palavras 
    contendo quatro strings.

    frase = ' '.join(palavras): Esta linha usa o método join, chamando-o na 
    string ' ' (um espaço em branco). O método join pega a lista palavras como argumento e 
    concatena seus elementos em uma única string, colocando um espaço em branco entre cada 
    elemento. O resultado é a string "Olá, como vai você?", que é então atribuído à variável frase.

    print(frase): Esta linha imprime o valor da variável frase, resultando na saída:

    Olá, como vai você?

Em resumo, o método join é uma maneira eficiente de combinar uma lista de strings em uma única 
string, usando um delimitador específico (neste caso, um espaço em branco).
"""


#Método join(): O método join() junta os elementos de uma lista em uma única string, utilizando um separador especificado entre cada elemento.

palavras = ['Olá,', 'como', 'vai', 'você?']
frase = ' '.join(palavras)  # Juntando as palavras com um espaço em branco entre elas
print(frase)
# Saída: "Olá, como vai você?"


texto = "   Olá!    "
texto_strip = texto.strip()  # Removendo espaços em branco do início e do final
print(texto_strip)
# Saída: "Olá!"

"""
Nessa parte do código, a função strip() é chamada sem argumentos, e ela remove 
todos os espaços em branco no início e no final da string armazenada na variável texto. 

Espaços em branco incluem espaços, tabulações e caracteres de nova linha. No exemplo 
dado, a string " Olá! " tem três espaços antes e quatro espaços depois do texto "Olá!". Após a 
chamada strip(), a variável texto_strip contém a string "Olá!" sem espaços extras, e essa 
string é impressa.
"""

texto = "********Olá!*********"
texto_strip = texto.strip('*')  # Removendo os caracteres '*' do início e do final
print(texto_strip)
# Saída: "Olá!"

"""
Nesta parte do código, a função strip() é chamada com o argumento "*", o que significa 
que ela vai remover todas as ocorrências do caractere "*" no início e no final da string. A 
string "********Olá!*********" tem oito asteriscos antes e nove asteriscos depois do 
texto "Olá!". A chamada strip('*') remove todos esses asteriscos, resultando na 
string "Olá!", que é armazenada na variável texto_strip e impressa.

Em resumo, a função strip() sem argumentos remove espaços em branco do início e do 
final de uma string, e com um argumento, remove todas as ocorrências desse caractere 
específico do início e do final da string.
"""

#Utilizando Formated Strings

nome = "Alice"
idade = 25
altura = 1.65

# Criando uma mensagem formatada usando f-string
mensagem = f"Olá, meu nome é {nome}. Tenho {idade} anos e minha altura é {altura:.2f} metros."

print(mensagem)


"""
Explicação:

    Definindo Variáveis: Três variáveis são definidas: nome, que é uma 
    string com o valor "Alice"; idade, que é um inteiro com o valor 25; e 
    altura, que é um número de ponto flutuante com o valor 1.65.

    Criando a Mensagem Formatada (f-string): Uma f-string é uma forma de formatar 
    strings em Python 3.6 ou superior, onde você pode incorporar expressões entre 
    chaves {} que serão avaliadas em tempo de execução.
    
        {nome}: Substituído pelo valor da variável nome, que é "Alice".
        {idade}: Substituído pelo valor da variável idade, que é 25.
        {altura:.2f}: Substituído pelo valor da variável altura, que é 1.65, formatado 
        com duas casas decimais. O .2f dentro das chaves significa que o número deve ser formatado 
        como um número de ponto flutuante com duas casas decimais.
"""


# Métodos para Strings
texto = "OLá, mundo!"

# Método upper() - Converte a string para maiúsculas
texto_upper = texto.upper()
print(texto_upper)  # Output: OLÁ, MUNDO!

# Método lower() - Converte a string para minúsculas
texto_lower = texto.lower()
print(texto_lower)  # Output: olá, mundo!

# Método capitalize() - Capitaliza a primeira letra da string
#a primeira letra "o" é convertida em maiúscula, resultando em "Olá, mundo!". As demais letras permanecem em minúsculas.
texto_capitalize = texto.capitalize()
print(texto_capitalize)  # Output: Olá, mundo!

# Método count() - Conta o número de ocorrências de um determinado caractere ou substring na string
ocorrencias = texto.count("o")
print(ocorrencias)  # Output: 2

# Método replace() - Substitui todas as ocorrências de uma substring por outra
texto_substituido = texto.replace("mundo", "amigo")
print(texto_substituido)  # Output: Olá, amigo!

# Método split() - Divide a string em uma lista de substrings com base em um caractere delimitador
palavras = texto.split(",")
print(palavras)  # Output: ['Olá', ' mundo!']

# Método join() - Junta uma lista de strings em uma única string, separadas por um caractere específico
lista_palavras = ['Olá', 'mundo!']
texto_junto = ",".join(lista_palavras)
print(texto_junto)  # Output: Olá,mundo!

# Exercício de Manipulação de Strings em Python

# 1. Crie uma variável chamada "nome" e atribua a ela o valor "Maria".
nome = "Maria"

# 2. Crie uma variável chamada "sobrenome" e atribua a ela o valor "Silva".
sobrenome = "Silva"

# 3. Crie uma variável chamada "idade" e atribua a ela o valor 30.
idade = 30

# 4. Concatene as variáveis "nome" e "sobrenome" em uma nova variável chamada "nome_completo".
nome_completo = nome + " " + sobrenome

# 5. Imprima na tela o valor da variável "nome_completo".
print(nome_completo)

# 6. Crie uma variável chamada "mensagem" que utilize a função format para criar uma frase 
# personalizada com as variáveis "nome_completo" e "idade".
mensagem = "Olá, meu nome é {} e tenho {} anos.".format(nome_completo, idade)

# 7. Imprima na tela o valor da variável "mensagem".
print(mensagem)

# Exercício de Manipulação de Strings em Python

# 1. Crie uma variável chamada "frase" e atribua a ela a seguinte 
#frase: "Python é uma linguagem de programação poderosa e versátil."

frase = "Python é uma linguagem de programação poderosa e versátil."

# 2. Imprima na tela o tamanho da frase, ou seja, a quantidade de 
#caracteres presentes nela.

tamanho_frase = len(frase)
print("Tamanho da frase:", tamanho_frase)

# 3. Crie uma variável chamada "palavra" e atribua a ela a primeira 
#palavra da frase.

palavra = frase.split()[0]
print("Primeira palavra da frase:", palavra)

# 4. Converta a variável "frase" para letras maiúsculas e atribua o 
#resultado a uma nova variável chamada "frase_maiuscula".

frase_maiuscula = frase.upper()
print("Frase em maiúsculas:", frase_maiuscula)

# 5. Substitua a palavra "poderosa" por "incrível" na variável 
#"frase" e atribua o resultado a uma nova variável chamada "frase_substituida".

frase_substituida = frase.replace("poderosa", "incrível")
print("Frase com substituição:", frase_substituida)


nome_completo = "Maria de Freitas Cardoso"

# 1. Exiba o nome do usuário em letras maiúsculas
print(nome_completo.upper())

# 2. Exiba o nome do usuário em letras minúsculas
print(nome_completo.lower())

# 3. Conte e exiba quantas letras (sem considerar espaços) o nome do usuário tem
print(len(nome_completo.replace(" ", "")))

# 4. Exiba o primeiro nome do usuário
print(nome_completo.split()[0])


# 5. Exiba o último nome do usuário
print(nome_completo.split()[-1])