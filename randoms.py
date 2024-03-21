# Números randomicos - Números aleatórios
import random

print(random.randrange(1, 1000))


# Gerar um número de ponto flutuante aleatório entre 0 e 1:
print(random.random())

# Gerar um número inteiro aleatório entre dois valores (inclusive):
print(random.randint(10, 20)) # Gera um número entre 10 e 20, inclusive.

# Escolher aleatoriamente um elemento de uma lista:
frutas = ["maçã", "banana", "cereja"]
print(random.choice(frutas)) # Escolhe uma fruta aleatoriamente da lista.

# Embaralhar aleatoriamente uma lista:
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros) # A lista 'numeros' agora está embaralhada.

# Gerar um número de ponto flutuante aleatório em um intervalo específico:
print(random.uniform(5.5, 9.5)) # Gera um número de ponto flutuante entre 5.5 e 9.5.