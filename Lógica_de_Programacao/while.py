#While Loops
#While - Enquanto

# Inicializa a variável 'numero' com o valor 1
numero = 1     

# Continua o loop enquanto 'numero' for menor que 5
while numero < 5:
    
    # Imprime o valor atual de 'numero'
    print(numero)
    
    # Incrementa 'numero' em 1 para a próxima iteração
    #numero = numero + 1
    numero += 1


    
"""
Explicação:

    Definindo Variável: A variável numero é inicializada com o valor 1.

    Loop While: A estrutura while cria um loop que continuará executando enquanto 
    a condição especificada for verdadeira. Neste caso, o loop continuará enquanto 
    numero for menor que 5.

    Corpo do Loop: Dentro do loop, há duas instruções:
    
        Imprimir Número: A função print(numero) imprime o valor atual da variável numero.
        
        Incrementar Número: A linha numero += 1 aumenta o valor de numero em 1. Isso é 
        equivalente a numero = numero + 1. É um passo importante para garantir que a condição 
        do loop eventualmente se torne falsa, evitando assim um loop infinito.

    Execução do Loop: O loop será executado enquanto numero for menor que 5. Veja 
    como ele se comporta em cada iteração:
    
        Iteração 1: numero é 1, impresso, e então incrementado para 2.
        Iteração 2: numero é 2, impresso, e então incrementado para 3.
        Iteração 3: numero é 3, impresso, e então incrementado para 4.
        Iteração 4: numero é 4, impresso, e então incrementado para 5.
        
        O loop termina, pois numero agora é 5, o que não satisfaz a condição numero < 5.

Saída:

A saída do programa será:
1
2
3
4

O código demonstra uma utilização básica do loop while para imprimir uma sequência 
de números, incrementando o valor em cada iteração até que uma condição de término seja atingida.

"""

print()

#Contar de 4 a 1
contador = 4

# Enquanto a variável contador for maior ou igual a 1, o loop continuará
while contador >= 1:
    
    # Imprime o valor atual da variável contador
    print(contador)  
    
    # Decrementa o valor da variável contador em 1
    #contador = contador - 1
    contador -= 1
    
    
print()

#Contar de 10 a 1 de 2 em 2

# Inicializa a variável contador com o valor 10
contador = 10

# Enquanto a variável contador for maior ou igual a 1, o loop continuará
while contador >= 1:
    
    # Imprime o valor atual da variável contador
    print(contador)  
    
    # Decrementa o valor da variável contador em 2
    contador -= 2 


"""
Exercício:

Crie um algoritmo que solicite ao usuário uma senha.
E só sai do looping do While quando for digitado a senha corretamente
"""
# Define a senha correta do sistema como '123'
senhaSistema = '123'

# Solicita ao usuário que digite a senha
senhaDigitada = input('Digite sua senha: ')

# Continua o loop enquanto a senha digitada pelo usuáiro for diferente da senha correta do sistema
while (senhaSistema != senhaDigitada):
    # Imprime uma mensagem indicando que a senha está incorreta
    print(f'Senha incorreta, tente novamente!')
    # Solicita ao usuário que digite a senha novamente
    senhaDigitada = input('\nDigite sua senha: ')

# Imprime uma mensagem de sucesso quando o usuário digita a senha correta e o loop termina
print(f'\nMuito bem! Você digitou a senha correta!')


while True:
    
    user_input = input('Digite "sair" para encerrar: ')

    if user_input == 'sair':
        break


import random

numero_secreto = random.randint(1, 100)
tentativas = 0

# print(numero_secreto)

while True:
    palpite = int(input('Digite o seu palpite: '))
    tentativas +=1

    if palpite < numero_secreto:
        print('O número secreto é maior. Tente novamente!')
    elif palpite > numero_secreto:
        print('O número secreto é menor. Tente novamente!')
    else:
        print(f'Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas')
        break

"""
Exercício:

Crie um algoritmo que leia n números inteiros digitados pelo usuário,
e só pare quando o usuário digitar 0.

No final, imprima na tela a soma de todos os números digitados

"""

somaNumerosDigitados = 0

numero = int(input('Digite um número ou 0 para sair: '))

while numero != 0:
    somaNumerosDigitados += numero
    numero = int(input('Digite um número ou 0 para sair: '))

print(f'Total: {somaNumerosDigitados}')


"""
Exercício:

Crie um algoritmo que leia números inteiros positivos digitados pelo usuário
até que o usuário digite um número menor que 0. No final. imprima o maior número digitado.
"""

maiorNumero = -1

numeroDigitado = int(input('Digite um número inteiro e mairo que ZERO: '))

while numeroDigitado >= 0:
    if numeroDigitado > maiorNumero:
        maiorNumero = numeroDigitado
    
    numeroDigitado = int(input('Digite um número inteiro e mairo que ZERO: '))

print(f'Maior número: {maiorNumero}')

