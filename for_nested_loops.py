# For Nested Looops

"""
For Nested Loops refere-se à prática de aninhar um ou mais
loops for dentro de outro loop for. Em outras palavras, é quando
você tem um loop for dentro do corpo de outro loop for. Esse conceito
é aplicável em várias linguagens de programação, incluindo Python
"""

# Exemplo de Loops aninhados

for i in range(1, 4):
    for j in range(1, 4):
        print(f'{i} * {j} = {i *j}')


"""
Compreensão de lista (list comprehension) em Python, 
que é uma maneira concisa de criar lista. Aqui está
um exemplo que combina um for e um if em uma única
linha para criar uma lista de quadrados dos números ímpares
de 0 a 9:

"""

quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)

texto = "Hello World"
consoantes = [char for char in texto if char.lower() not in 'aeiou']
print(consoantes)

consoantes2  = []

for char in texto:
     if char.lower() not in 'aeiou':
         consoantes2.append(char)
         #print(consoantes2)
print(consoantes2)


"""
Exercício 
Crie um programa em Python que solicite ao usuário que 
digite um número inteiro não negativo.
Em seguida, calcule e exiba o fatorial desse número.

Digite um número inteiro não negativo: 5
O fatorial de 5 é: 120

"""

n = int(input('Digite um número inteiro não negativo: '))

fatorial = 1
for multiplicador in range(1, n+1):
    fatorial *= multiplicador

    print(f'{multiplicador}! = ',end=' ')

    for i in range(1, multiplicador + 1):
        print(i, end=' ')

        if i != multiplicador:

            print('* ', end=' ')


    print(f'= {fatorial}')



# For Criando um Retangulo
    
"""
******
******
******

"""

coluna = 5
linha = 3

for i in range(linha):
    for j in range(coluna):
        print('*', end=' ')
    print()

# Criando um triângulo com a ponta no meios usando Loops

altura = 5
for i in range(altura):
    espacos = altura - i - 1
    asteriscos = 2 * i + 1
    print(' ' * espacos + "*" * asteriscos)