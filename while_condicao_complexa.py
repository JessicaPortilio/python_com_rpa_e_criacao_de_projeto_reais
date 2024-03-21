# While Usando uma Condição Complexa

# O exemplo abaixo demonstra um programa que continua 
# incrementando x e decrementando y enquanto x for menor que 10
# e y for maior que 10

# Inicializando duas variáveis, x e y
x, y = 5, 15

# O Loop continuará enquanto ambos as condições forem verdadeiras: x < 10 e y > 10
while x < 10 and y > 10:
    print(f'x: {x}, y: {y}') # imprimindo os valores atuais de x e y

    x += 1 # Incrementando x em 1
    y -= 1 # Decrementando y em 1

print('Loop concluído')
print(f'Valores finais x: {x}, y: {y}')


# While Usando uma Condição Complexa

numero_secreto1 = 7
numero_secreto2 = 3

tentativas = 5

adivinhou1 = False
adivinhou2 = False

while tentativas > 0 and (not adivinhou1 or not adivinhou2):
    print(f'Tentativas restatentes : {tentativas}')

    palpite1 = int(input('Adivinhe o primeiro número secreto (1-10): '))
    palpite2 = int(input('Adivinhe o segundo número secreto (1-10): '))

    if palpite1 == numero_secreto1:
        print('Você adivinhou o primeiro número!')
        adivinhou1 = True
    
    if palpite2 == numero_secreto2:
        print('Você adivinhou o segundo número!')
        adivinhou2 = True
    
    if not adivinhou1 or not adivinhou2:
        print('Tente novamente!')

        tentativas -= 1

if adivinhou1 and adivinhou2:
    print('Parabéns! Você adivinhou ambos os números!')
else:
    print(f'Você não conseguiu adivinhar os números. Eles eram {numero_secreto1} e {numero_secreto2}')


"""
Exercício: Soma dos primeiros números ímpares

Seu objetivo neste exercício é calcular a soma 
dos primeiros n números ímpares utilizando um loop while.

Instruções:

Você já possui uma variável chamada n, 
que determina quantos dos primeiros números ímpares você deseja somar.

Inicie com três variáveis:

contador com valor 0, que servirá para contar quantos 
números ímpares já foram somados.

soma também com valor 0, que armazenará a soma total dos números ímpares.

numero_impar_atual com valor 1, que representará o número ímpar 
atual a ser somado à variável soma.


Utilize um loop while que continue sua execução até que o valor 
de contador seja igual a n.


Dentro do loop:


Adicione o valor de numero_impar_atual à variável soma.

Incremente o valor de numero_impar_atual em 2, 
para obter o próximo número ímpar.

Incremente o contador para indicar que um número ímpar foi somado.

Ao final do loop, use a função print() para exibir o valor de soma, 
que conterá a soma dos primeiros n números ímpares.


Dica: Números ímpares são aqueles que não são divisíveis por 2. 
O próximo número ímpar sempre será 2 unidades maior que o atual.

"""

n = 10
contador = 0
soma = 0
numero_impar_atual =1

while contador < n:
    soma += numero_impar_atual
    #print(numero_impar_atual)
    numero_impar_atual += 2
    contador += 1


print("A soma dos primeiros", n, "números ímpares é:", soma)