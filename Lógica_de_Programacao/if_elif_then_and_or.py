#Python função If ou seja função Se

numero1 = 90
numero2 = 12

#Se a variável número1 é maior que a variável número 2
if numero1 > numero2:
    
    print("O número da variável  numero1 é maior que o número da variável numero2")

#Python função If... elif
#if - Se
#elif - Senão Se

numero1 = 6
numero2 = 6

if numero1 > numero2:
    
    print("O número da variável  numero1 é maior que o número da variável numero2")
    
elif numero1 == numero2:
    
    print("O número da variável numero1 é igual ao número da variável numero2")

"""
Exercício:

Adivinhe o Número Secreto

Você foi desafiado a adivinhar um número secreto entre 1 e 10!

    Execute o programa.
    Insira um número inteiro entre 1 e 10 quando solicitado.
    O programa irá informar se você adivinhou corretamente o número secreto ou não.

Seu objetivo é descobrir qual é o número secreto. Você pode executar o programa 
quantas vezes quiser até adivinhar corretamente.

Nota: Para fins deste exercício, o número secreto é fixo e é igual a 7. Em uma 
versão mais avançada do exercício, você poderia modificar o programa para escolher um número 
secreto aleatório cada vez que é executado.
"""

# Define o número secreto que o usuário deve adivinhar
numero_secreto = 7

# Solicita ao usuário para inserir um número inteiro entre 1 e 10
chute = int(input("Tente adivinhar o número secreto entre 1 e 10: "))

# Verifica se o número inserido pelo usuário é igual ao número secreto
if chute == numero_secreto:
    
    # Se o usuário adivinhar corretamente, imprime uma mensagem de sucesso
    print("Parabéns! Você adivinhou o número secreto.")

#else - Senão
else:
    
    # Se o usuário adivinhar errado, imprime uma mensagem de erro
    print("Desculpe, você não adivinhou o número secreto. Tente novamente!")


"""
Exercício:

Verifique a Elegibilidade para Votar

Neste exercício, você vai executar um programa que determina 
se uma pessoa está ou não elegível para votar com base em sua idade.

    Execute o programa.
    Insira sua idade quando solicitado.
    O programa irá informar se você é elegível para votar ou não.

Note que a idade mínima para votar é de 18 anos.
"""

# Pergunta ao usuário sua idade
idade = int(input("Por favor, digite sua idade: "))

#if - se
# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    
    # Se a idade for maior ou igual a 18, imprime que o usuário está elegível para votar
    print("Você é elegivel para votar.")

#else - senão
else:
    
    # Se a idade for menor que 18, imprime que o usuário não está elegível para votar
    print("Você não é elegivel para votar.")


"""
Abaixo está uma tabela que explica os diferentes operadores de comparação 
que você pode usar com uma instrução if em Python. Esses operadores permitem 
comparar valores, o que é frequentemente necessário em programação condicional.

Operador    Descrição              Exemplo      Resultado
>           Maior que              5 > 3        True
<           Menor que              5 < 3        False
==          Igual a                5 == 5       True
!=          Diferente de           5 != 3       True
>=          Maior que ou igual a   5 >= 5       True
<=          Menor que ou igual a   5 <= 3       False

Você pode usar esses operadores em uma instrução if para testar condições 
específicas. Aqui estão alguns exemplos de como você poderia usar esses 
operadores em condições:

if x > y:
    print("x é maior que y")
elif x < y:
    print("x é menor que y")
elif x == y:
    print("x é igual a y")
else:
    print("x e y são incomparáveis")

Esses operadores formam a base para muitas construções lógicas e condicionais 
em Python e são ferramentas essenciais na caixa de ferramentas de qualquer programador.
"""

#Função If... elif ... else
#Se... Senão Se ... Senão

numero1 = 9
numero2 = 6

if numero1 > numero2:
    
    print(f"O {numero1} é maior que o {numero2}")
    
elif numero1 == numero2:
    
    print(f"O {numero1} é IGUAL ao {numero2}")
    
else:
    
    print(f"O {numero1} é MENOR que o {numero2}")


#and - E

numero1 = 50
numero2 = 21
numero3 = 200

if numero1 > numero2 and numero3 > numero1:
    
    print("As duas condições são verdadeiras")
    
"""
Explicação:

    Definindo Variáveis: Três variáveis são definidas, numero1 com o valor 
    50, numero2 com o valor 21, e numero3 com o valor 200.

    Condição Composta (if):
        Primeira Condição: Verifica se numero1 é maior que numero2, ou seja, 
        se 50 é maior que 21. Essa condição é verdadeira.
        
        Segunda Condição: Verifica se numero3 é maior que numero1, ou 
        seja, se 200 é maior que 50. Essa condição também é verdadeira.
        
        Operador and: A cláusula if usa o operador lógico and, o que significa 
        que ambas as condições devem ser verdadeiras para que o bloco de código 
        sob o if seja executado.

    Execução da Condição: Como ambas as condições são verdadeiras, o bloco de 
    código indentado abaixo da declaração if é executado. Isso resulta na impressão 
    da mensagem "As duas condições são verdadeiras" no console.

O código usa o operador lógico and para verificar duas condições simultaneamente e 
imprimir uma mensagem se ambas forem verdadeiras. Neste exemplo, como ambas as condições 
são verdadeiras, a mensagem será impressa.

"""

"""
Exercício:

Classificação de Notas

Neste exercício, seu objetivo é executar um programa que 
classifica as notas de um estudante em diferentes categorias.

    Execute o programa.
    
    Insira a nota do estudante quando solicitado (entre 0 e 100).
    
    O programa irá informar a classificação da nota de acordo com os seguintes critérios:
        Excelente: 90-100
        Bom: 70-89
        Satisfatório: 50-69
        Insuficiente: 0-49
"""

nota = int(input("Por favor, digite a nota do estudante (0-100): "))

#Verifica em qual categoria a nota se encaixa
if nota >= 90 and nota <= 100:
    
    print("Excelente!")
    
elif nota >= 70 and nota <= 89:
    
    print("Bom!")
    
elif nota >= 50 and nota <= 69:
    
    print("Satisfatório!")
    
else:
    
    print("Insuficiente!")


"""
Exercício:

Calculadora de Descontos

Você é um cliente em uma loja que está tendo uma promoção especial. Dependendo 
do valor da sua compra, você pode receber um desconto!

    Execute o programa.
    
    Insira o valor da sua compra quando solicitado.
    
    O programa irá calcular e informar o valor do desconto aplicado e o valor final 
    com o desconto.

Os descontos são aplicados da seguinte forma:

    Compras acima de R$1000 recebem 20% de desconto.
    Compras de R$500 a R$1000 recebem 10% de desconto.
    Compras abaixo de R$500 não recebem desconto.
    
    
"""

# Solicita ao usuário o valor da compra
valor_compra = float(input("Por favor, digite o valor da sua compra: $"))

# Verifica em qual categoria de desconto a compra se encaixa
if valor_compra > 1000:
    
    # Se a compra for maior que R$1000, aplica um desconto de 20%
    desconto = 0.20 * valor_compra
    
    # Imprime uma mensagem informando o desconto de 20%
    print("Você recebeu 20% de desconto!")
    
elif valor_compra >= 500 and valor_compra <= 1000:
    
    # Se a compra for entre R$500 e R$1000, aplica um desconto de 10%
    desconto = 0.10 * valor_compra
    
    # Imprime uma mensagem informando o desconto de 10%
    print("Você recebeu 10% de desconto!")
    
else:
    
    # Se a compra for menor que $500, não aplica desconto
    desconto = 0
    
    # Imprime uma mensagem informando que não há desconto
    print("Você não recebeu desconto.")

# Calcula o valor final após o desconto
valor_final = valor_compra - desconto

# Imprime o valor do desconto e o valor final da compra
print(f"Valor do desconto: R${desconto:.2f}")
print(f"Valor final da compra: R${valor_final:.2f}")

#If ... Or
#Se ... Ou

numero1 = 19
numero2 = 150
numero3 = 18

if numero1 > numero2 or numero1 > numero3:
    
    print(f"O {numero1} é maior que {numero2} ou o {numero1} é maior que {numero3}!")
    
"""
Explicação:

    Definindo Variáveis: Três variáveis são definidas, numero1 com o valor 19, numero2 
    com o valor 150, e numero3 com o valor 18.

    Condição Composta (if):
    
        Primeira Condição: Verifica se numero1 é maior que numero2, ou seja, se 
        19 é maior que 150. Essa condição é falsa.
        
        Segunda Condição: Verifica se numero1 é maior que numero3, ou seja, se 
        19 é maior que 18. Essa condição é verdadeira.
        
        Operador or: A cláusula if usa o operador lógico or, o que significa 
        que pelo menos uma das condições deve ser verdadeira para que o bloco de 
        código sob o if seja executado.

    Execução da Condição: Como pelo menos uma das condições é verdadeira (a segunda), o 
    bloco de código indentado abaixo da declaração if é executado. Isso resulta na impressão 
    da mensagem "Meu número 1 é maior que umas ou mais condições" no console.

O código usa o operador lógico or para verificar duas condições simultaneamente e imprimir uma 
mensagem se pelo menos uma delas for verdadeira. Neste exemplo, como a segunda condição é 
verdadeira, a mensagem será impressa.
"""

"""
Exercício

Entrada para um Evento Exclusivo

Você foi convidado para um evento exclusivo. Para entrar, você deve 
atender a pelo menos uma das seguintes condições:

    Ter um convite VIP.
    Estar na lista de convidados.
    Ser um membro do clube.

    Execute o programa.
    
    Responda às perguntas fornecidas com 'sim' ou 'não'.
    O programa irá informar se você pode entrar no evento ou não.
    
    
    Bem-vindo(a) ao evento!
    Desculpe, você não pode entrar no evento.
    
"""

# Pergunta ao usuário se possui um convite VIP
convite_vip = input("Você possui um convite VIP? (sim/não):")

# Pergunta ao usuário está na lista de convidados
na_lista = input("Você está na lista de convidados? (sim/não):")

# Pergunta ao usuário se é um membro do clube
membro_clube = input("Você é um membro do clube? (sim/não):")
       
# Verifica se o usuário atende a pelo menos uma das condições
if convite_vip == "sim" or na_lista  == "sim" or membro_clube == "sim":
                  
    # Se atender a pelo menos uma das condições, permite a entrada
    print("Bem-vindo(a) ao evento!")
                     
else:
    
    # Se não atender a nenhuma das condições, nega a entrada
    print("Desculpe, você não pode entrar no evento.")

#Exercicio Par ou Impar
#Crie um algoritmo que solicite a entrada de um número positivo e inteiro e imprima se o
#número é PAR ou IMPAR

n1 = int(input("Digite um número: "))

verificaNumero = n1 % 2

if verificaNumero == 0:
    
    print(f"O número {n1} é PAR")
    
else:
    
    print(f"O número {n1} é IMPAR")
    
"""
Explicação:

    Entrada do Usuário: A função input("Digite um número ") solicita ao usuário 
    que digite um número. O texto dentro dos parênteses é a mensagem mostrada ao usuário.

    Conversão para Inteiro: A função int() converte a entrada do usuário (que é uma 
    string) em um número inteiro. Esse valor é então armazenado na variável n1.

    Verificando Par ou Ímpar: O operador % calcula o resto da divisão de n1 por 2. Se o 
    número for par, o resto dessa divisão será 0; se for ímpar, será 1. O resultado é 
    armazenado na variável verificaNumero.

    Condição (if-else):
    
        Se Par: Se verificaNumero for igual a 0, isso significa que n1 é par, e 
        a mensagem "O número ", n1, " é PAR" é impressa.
        
        Se Ímpar: Se verificaNumero não for igual a 0 (ou seja, for 1), isso 
        significa que n1 é ímpar, e a mensagem "O número ", n1, " é IMPAR" é impressa.

O código é um exemplo simples de como receber uma entrada do usuário e realizar 
uma operação aritmética para determinar uma propriedade específica do número (neste caso, 
se ele é par ou ímpar) e, em seguida, imprimir uma mensagem correspondente.
"""

#Estrutura condicional ternária

#age - idade

age = 18
status = "adulto" if age >= 18 else "menor de idade"
print(status) #Saída: "adulto"

"""
Neste exemplo, a variável status recebe o valor "adulto" se 
age for maior ou igual a 18 e "menor de idade" caso contrário. Essa 
linha de código usa uma expressão condicional para fazer isso de forma 
concisa em uma única linha. Isso pode ser útil para tornar o código mais 
compacto, mas deve ser usado com cuidado para não comprometer a legibilidade.
"""

#Suponhamos que você queira determinar se um número é par ou impar:

numero = 42
resultado = "par" if numero % 2 == 0 else "impar"
print(resultado) #Saída: "par"

"""
Neste exemplo, a variável resultado receberá o valor "par" se 
o número for divisível por 2 e "ímpar" caso contrário. Isso é 
feito usando uma expressão condicional em uma única linha, que 
avalia a condição numero % 2 == 0 e seleciona o valor correspondente.
"""

#Suponha que você tenha pontuação e queira categoriza-la
#como "baixa", "média" ou "alta"

score = 85
categoria = "baixa" if score < 50 else "média" if score < 80 else "alta"
print(categoria)

"""
Exemplo de uma expressão condicional aninhada (ou ternária) em Python. 

Vamos dividi-la em partes para entender melhor:

    "baixa" if score < 50: Se a pontuação (score) for menor que 50, a expressão inteira 
    será avaliada como "baixa".

    "média" if score < 80: Se a primeira condição não for atendida (ou seja, a pontuação 
    é maior ou igual a 50) e a pontuação for menor que 80, a expressão será avaliada 
    como "média".

    "alta": Se nenhuma das condições acima for atendida (ou seja, a pontuação é 
    maior ou igual a 80), a expressão será avaliada como "alta".

Portanto, a expressão inteira é equivalente a uma série de verificações if ... elif ... else que 
categoriza a pontuação em "baixa", "média" ou "alta" com base nos critérios definidos.

Aqui está uma representação equivalente usando uma estrutura condicional mais tradicional:

if score < 50:
    category = "baixa"
elif score < 80:
    category = "média"
else:
    category = "alta"

A versão de uma linha é mais concisa, mas a versão expandida pode ser mais legível, especialmente 
se houver muitas condições aninhadas.
"""


"""
Exercício: Verificar faixa etária
Instruções:



Dada uma idade como entrada, seu programa deve classificar a pessoa em uma das seguintes faixas etárias e exibir a classificação correspondente:



Infantil: 0 a 12 anos

Adolescente: 13 a 17 anos

Adulto: 18 a 59 anos

Idoso: 60 anos ou mais

Utilize a estrutura condicional if, elif e else para realizar a classificação.
"""

idade = 25  # Altere esse valor para testar diferentes faixas etárias


# Escreva sua estrutura condicional abaixo

if idade >= 0 and idade <= 12:
    print(f'Infantil: {idade} anos')
elif idade >= 13 and idade <= 17:
    print(f'Adolescente: {idade} anos')
elif idade >= 18 and idade <= 59:
    print(f'Adulto: {idade} anos')
else:
    print(f'Idoso: {idade} anos')