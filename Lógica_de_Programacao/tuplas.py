"""
Tuplas:

    Definição de Tuplas:
        Tuplas são uma das estruturas de dados embutidas no Python. São similares às 
        listas, mas são imutáveis, o que significa que uma vez definidas, os elementos 
        não podem ser modificados.

    Criação de Tuplas:
        Como criar uma tupla usando parênteses: t = (1, 2, 3)
        Tupla com um único elemento: t = (1,)
        Tupla sem parênteses: t = 1, 2, 3
        Uso da função tuple(): t = tuple([1, 2, 3])

    Acesso aos Elementos:
        Como acessar elementos usando índices: t[0]
        Fatiamento de tuplas: t[1:3]

    Imutabilidade:
        Tentativas de alterar um elemento de uma tupla resultarão em um erro.
        Mas se um elemento da tupla for mutável, como uma lista, você pode modificar esse elemento.

    Operações com Tuplas:
        Concatenação: (1, 2) + (3, 4)
        Repetição: (1, 2) * 3
        Verificar se um elemento está na tupla: 2 in (1, 2, 3)

    Métodos de Tuplas:
        count(): conta o número de vezes que um elemento aparece na tupla.
        index(): retorna o índice do primeiro elemento que corresponde ao valor especificado.

    Desempacotamento de Tuplas:
        Atribuindo valores de uma tupla a múltiplas variáveis: a, b, c = (1, 2, 3)

    Aplicações Práticas:
        Retornando múltiplos valores de uma função usando tuplas.
        Uso de tuplas em loops for: for a, b in [(1,2), (3,4)]:
        Trocando valores entre duas variáveis: a, b = b, a

    Comparando Tuplas:
        Tuplas podem ser comparadas usando operadores de comparação: (1, 2) < (1, 3)

    Diferenças entre Listas e Tuplas:

    Quando e por que usar uma em vez da outra.

"""
print()

"""
Definição de Tuplas:
        Tuplas são uma das estruturas de dados embutidas no Python. São similares às 
        listas, mas são imutáveis, o que significa que uma vez definidas, os elementos 
        não podem ser modificados.
"""

"""
Exemplo Prático: Informações de um Livro

Suponha que você esteja criando um sistema para uma biblioteca. Uma 
das tarefas é representar informações sobre um livro. Você pode escolher 
tuplas para representar essas informações porque, uma vez que um livro é adicionado 
ao sistema, certas informações sobre ele, como o título, autor e ISBN, geralmente não mudam.

Portanto, para um livro com título "A Arte da Guerra", autor "Sun Tzu" e 
ISBN "978-8572835080", você pode representar essas informações como uma tupla:
"""

livro = ("A Arte da Guerra", "Sun Tzu", "978-8572835080")


#Agora, vamos tentar algumas operações:

#Acessar informações:

titulo = livro[0]  # Acessa o título do livro
autor = livro[1]   # Acessa o autor do livro
isbn = livro[2]    # Acessa o ISBN do livro

print(titulo)  # Saída: A Arte da Guerra
print(autor)   # Saída: Sun Tzu
print(isbn)    # Saída: 978-8572835080

#Tentar modificar uma informação:
#Se você tentar modificar o título do livro, por exemplo, você
#encontrará um erro devido à imutabilidade das tuplas.

#livro[0] = "A Arte da Estratégia"  # Isso causará um erro!

"""
Ao executar o código acima, você receberá um TypeError informando 
que as tuplas não suportam a atribuição de item.

Essa imutabilidade pode ser útil para garantir a integridade dos dados em 
cenários em que as informações não devem ser alteradas após serem definidas.
"""
print()


"""
Criação de Tuplas:

        1. Como criar uma tupla usando parênteses: t = (1, 2, 3)
        2. Tupla com um único elemento: t = (1,)
        3. Tupla sem parênteses: t = 1, 2, 3
        4. Uso da função tuple(): t = tuple([1, 2, 3])
        
Vamos criar um exemplo prático relacionado ao planejamento de viagens.

Exemplo Prático: Planejando uma Viagem

Imagine que você está planejando uma viagem e deseja armazenar informações 
sobre diferentes cidades que deseja visitar, como o nome da cidade, o país e 
o número estimado de dias que planeja ficar.
"""

#1. Criando uma tupla usando parênteses:

#Você decide visitar Paris por 5 dias.

destino1 = ("Paris", "França", 5)
print(destino1)  # Saída: ('Paris', 'França', 5)

#2. Tupla com um único elemento:

#Suponhamos que você só saiba o nome da cidade por enquanto e 
#ainda não decidiu por quanto tempo ficará ou até mesmo em qual país 
#está localizada. Então, você cria uma tupla com apenas um elemento.

destino_indefinido = ("Kyoto",)
print(destino_indefinido)  # Saída: ('Kyoto',)

#3. Tupla sem parênteses:

#Você decide visitar Roma na Itália por 4 dias, e decide 
#usar uma sintaxe simplificada para criar a tupla.

destino2 = "Roma", "Itália", 4
print(destino2)  # Saída: ('Roma', 'Itália', 4)


#4. Uso da função tuple():

#Você tem uma lista das cidades dos EUA que deseja visitar, e a 
#quantidade de dias que deseja ficar em cada uma delas. Você decide 
#convertê-la em uma tupla para garantir que os dados não sejam modificados acidentalmente.

lista_destinos_EUA = ["Nova York", "EUA", 7]
destino3 = tuple(lista_destinos_EUA)
print(destino3)  # Saída: ('Nova York', 'EUA', 7)

print()

"""
Exercício: Armazenando Informações sobre Livros

Contexto: Você administra uma pequena biblioteca e decide 
armazenar informações sobre seus livros usando tuplas para garantir 
que os dados sejam consistentes e imutáveis.

Objetivo: Crie tuplas para representar informações de livros usando 
diferentes métodos de criação de tuplas.

Instruções:

    1. Criar uma tupla usando parênteses:
        Crie uma tupla chamada livro1 para armazenar informações sobre um 
        livro: título, autor e ano de publicação. 
        Use a seguinte informação: "Orgulho e Preconceito", "Jane Austen", 1813.

    2. Tupla com um único elemento:
        Você recebeu uma doação de um livro, mas só sabe o título por 
        enquanto. Crie uma tupla chamada livro_indefinido com apenas o título: "O Pequeno Príncipe".

    3. Tupla sem parênteses:
        Para o próximo livro, use uma sintaxe simplificada. Crie uma tupla 
        chamada livro2 para armazenar: "1984", "George Orwell", 1949.

    4. Uso da função tuple():
        Você tem uma lista de informações sobre um novo livro. Converta esta 
        lista em uma tupla para garantir sua imutabilidade. 
        
        A lista é: ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954]. Nomeie a tupla como livro3.

    Teste suas tuplas:
        Mostre cada uma das informações armazenadas usando a função print.

Isso dara a você uma prática valiosa na criação de tuplas usando 
várias técnicas, bem como uma compreensão de por que e quando 
usar tuplas em vez de listas ou outros tipos de dados.
"""

#Resposta:

#1. Criar uma tupla usando parênteses:
#        Crie uma tupla chamada livro1 para armazenar informações sobre um 
#        livro: título, autor e ano de publicação. 
#        Use a seguinte informação: "Orgulho e Preconceito", "Jane Austen", 1813.

livro1 = ("Orgulho e Preconceito", "Jane Austen", 1813)
print(livro1)


#    2. Tupla com um único elemento:
#        Você recebeu uma doação de um livro, mas só sabe o título por 
#        enquanto. Crie uma tupla chamada livro_indefinido com apenas o título: "O Pequeno Príncipe".

livro_indefinido = ("O Pequeno Príncipe",)
print(livro_indefinido)

#    3. Tupla sem parênteses:
#        Para o próximo livro, use uma sintaxe simplificada. Crie uma tupla 
#        chamada livro2 para armazenar: "1984", "George Orwell", 1949.

livro2 = "1984", "George Orwell", 1949
print(livro2)


#    4. Uso da função tuple():
#        Você tem uma lista de informações sobre um novo livro. Converta esta 
#        lista em uma tupla para garantir sua imutabilidade. 
       
#        A lista é: ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954]. Nomeie a tupla como livro3.

#    Teste suas tuplas:
#        Mostre cada uma das informações armazenadas usando a função print.

lista_livro3 = ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954]
livro3 = tuple(lista_livro3)
print(livro3)


"""
Acesso aos Elementos:
        Como acessar elementos usando índices: t[0]
        Fatiamento de tuplas: t[1:3]
"""

"""
Exemplo Prático: Agenda de Contatos

Contexto: Você tem uma agenda onde armazena informações 
de seus contatos em tuplas. Cada tupla contém o nome do 
contato, o número de telefone e o endereço de e-mail. 

Você deseja acessar e exibir essas informações.
"""

#1. Como acessar elementos usando índices:

#Vamos começar criando uma tupla com informações de um contato.

contato = ("João Silva", "123-456-7890", "joao.silva@email.com")

# Acessando o nome:
nome = contato[0]
print("Nome:", nome)  # Saída: Nome: João Silva

# Acessando o telefone:
telefone = contato[1]
print("Telefone:", telefone)  # Saída: Telefone: 123-456-7890

#2. Fatiamento de tuplas:

#Imagine agora que você só quer mostrar o nome e o número de telefone, omitindo o e-mail.
info_relevante = contato[:2]

print("Informações Relevantes:", info_relevante)  # Saída: Informações Relevantes: ('João Silva', '123-456-7890')

"""
Explicação: Usando o fatiamento [:2], pegamos todos os elementos da tupla 
desde o início até o índice 2 (exclusivo), que nos dá o nome e o telefone do contato.

Este exemplo prático demonstra como as tuplas podem ser utilizadas para armazenar 
informações relacionadas e como acessar ou extrair essas informações usando índices e fatiamento.
"""
print()


"""
Exercício: Gerenciando Inventário de Produtos

Contexto: Você trabalha em um depósito e possui um inventário de produtos 
armazenados em tuplas. Cada tupla contém o nome do produto, a quantidade em 
estoque e o preço unitário. Sua tarefa é acessar e exibir certas informações desses produtos.

Objetivo: Acesse e exiba informações específicas dos produtos usando índices e fatiamento de tuplas.

Instruções:

    Definindo um Produto:
        Comece definindo uma tupla chamada produto com as seguintes 
        informações: "Laptop", 10 (quantidade em estoque), 1500.00 (preço em dólares).

    Acessando elementos usando índices:
        Exiba o nome do produto.
        Em seguida, exiba a quantidade em estoque.

    Fatiamento de tuplas:
        Mostre as informações excluindo o preço (ou seja, nome e quantidade 
        em estoque) usando fatiamento de tuplas.

Questões:

a) Qual é o nome do produto?

b) Quantos itens desse produto estão em estoque?

c) Sem mostrar o preço, quais são as informações disponíveis sobre o produto?

"""

#1. Definindo um Produto:
#      Comece definindo uma tupla chamada produto com as seguintes 
#      informações: "Laptop", 10 (quantidade em estoque), 1500.00 (preço em dólares).

produto = ("Laptop", 10, 1500.00)
print(produto)

#2.    Acessando elementos usando índices:
#        Exiba o nome do produto.
#        Em seguida, exiba a quantidade em estoque.

nome_produto = produto[0]
quantidade_estoque = produto[1]
print(f"Produto: {nome_produto} - Quantidade em Estoque: {quantidade_estoque}")

#3.    Fatiamento de tuplas:
#        Mostre as informações excluindo o preço (ou seja, nome e quantidade 
#        em estoque) usando fatiamento de tuplas.

info_relevantes = produto[:2]
print(f"Informações Relevante: {info_relevantes}")

print()
#Respostas às questões

#a) Qual é o nome do produto?
print(f"a) Qual é o nome do produto? {nome_produto}")

#b) Quantos itens desse produto estão em estoque?

print(f"b) Quantos itens desse produto estão em estoque? {quantidade_estoque}")

#c) Sem mostrar o preço, quais são as informações disponíveis sobre o produto?
print(f"c) Sem mostrar o preço, quais são as informações disponíveis sobre o produto? {info_relevantes}")

"""
Imutabilidade:
        Tentativas de alterar um elemento de uma tupla resultarão em um erro.
        Mas se um elemento da tupla for mutável, como uma lista, você pode modificar esse elemento.
"""

"""
Exemplo Prático: Restrições de Segurança no Aeroporto

Contexto: Em um sistema de aeroporto, você deseja armazenar regras 
de segurança em relação à bagagem de mão dos passageiros. 

Algumas regras são imutáveis (como dimensões da bagagem), enquanto 
outras, como os itens proibidos, podem ser atualizados periodicamente.
"""

#1. Tentativas de alterar um elemento de uma tupla resultarão em um erro:

#Você tem uma tupla que armazena as dimensões máximas permitidas para a bagagem 
#de mão em centímetros (altura, largura, profundidade).
dimensoes_bagagem = (55, 35, 25)

#Agora, por alguma razão, você decide tentar alterar a altura máxima permitida:
# Isto causará um erro!

#dimensoes_bagagem[0] = 60

#Se você tentar executar o código acima, obterá um TypeError, indicando que 
#os elementos da tupla não podem ser modificados.

#2. Mas se um elemento da tupla for mutável, como uma lista, você pode modificar esse elemento:

#No mesmo sistema do aeroporto, você possui uma tupla que armazena itens 
#proibidos na bagagem de mão. A lista de itens pode ser atualizada quando necessário.

itens_proibidos = ["líquidos acima de 100ml", "objetos cortantes", "material explosivo"]
regras_bagagem = (dimensoes_bagagem, itens_proibidos)

# que uma nova regra seja implementada e agora é proibido transportar 
#baterias de lítio na bagagem de mão. Mesmo que a tupla regras_bagagem 
#seja imutável, o elemento itens_proibidos é uma lista, que é mutável. 

#Portanto, você pode adicionar à lista:

regras_bagagem[1].append("baterias de lítio")
print(regras_bagagem[1])

#Neste exemplo prático, podemos ver como as propriedades de 
#imutabilidade das tuplas funcionam, bem como a exceção quando um de 
#seus elementos é mutável, como uma lista.
print()

"""
Exercício: Gerenciando Vendas de Produtos

Contexto: Você é um gerente de vendas em uma loja de eletrônicos. Cada 
produto vendido é registrado em uma tupla que contém o nome do produto, seu 
preço fixo e uma lista das vendas realizadas durante o mês (quantidades vendidas a cada dia).

Objetivo: Entenda a imutabilidade das tuplas enquanto gerencia o registro de vendas 
diárias de um produto específico.

Instruções:

    1. Registro de Produto:
    
        Crie uma tupla chamada produto com as seguintes 
        
        informações: "Smartphone", 1000.00 (preço em dólares), 
        [2, 3, 4] (vendas nos três primeiros dias do mês).

    2. Tentativa de Alteração de Imutabilidade:
        Tente alterar o preço do "Smartphone" para 1100.00.
        Observe o erro gerado e explique por que ele ocorre.

    3. Atualização de Vendas:
        Um novo lote de "Smartphone" foi vendido e você vendeu mais 
        5 unidades no quarto dia. Adicione esse número à lista de vendas.
        
        Exiba a lista de vendas atualizada para o "Smartphone".

Questões:

a) Ao tentar alterar o preço do "Smartphone", qual erro você encontrou?

b) Qual é o registro de vendas atualizado após adicionar as vendas do quarto dia?

Este exercício visa ensinar sobre a imutabilidade das tuplas em 
um contexto prático de vendas. Ao tentar modificar o preço, enfrentarão um 
erro e, assim, compreenderá a natureza imutável das tuplas. No entanto, ao atualizar 
o registro de vendas, que é uma lista mutável dentro da tupla, aprenderá sobre a 
capacidade de modificar elementos mutáveis mesmo dentro de estruturas imutáveis.
"""

#Solução:

#1. Registro de Produto:
    
#       Crie uma tupla chamada produto com as seguintes 
        
#        informações: "Smartphone", 1000.00 (preço em dólares), 
#        [2, 3, 4] (vendas nos três primeiros dias do mês).

produto = ("Smartphone", 1000.00, [2, 3, 4])
print(produto)
print()

#2. Tentativa de Alteração de Imutabilidade:
#        Tente alterar o preço do "Smartphone" para 1100.00.
#        Observe o erro gerado e explique por que ele ocorre.

# A seguinte linha causará um erro, pois tentamos modificar um elemento imutável de uma tupla.
# Para demonstrar, a linha está comentada, mas se descomentada e executada, causaria um TypeError.
# produto[1] = 1100.00

# 3. Atualização de Vendas:
#        Um novo lote de "Smartphone" foi vendido e você vendeu mais 
#        5 unidades no quarto dia. Adicione esse número à lista de vendas.
        
#        Exiba a lista de vendas atualizada para o "Smartphone".

produto[2].append(5)
vendas_atualizadas = produto[2]

print(produto)

print()

print("Questões:\n")

print("a) Ao tentar alterar o preço do Smartphone, qual erro você encontrou?")
print("O erro ao tentar alterar o preço do Smartphone é:")
print("TypeError: 'tuple' object does not support item assignment")

print("b) Vendas atualizadas:", vendas_atualizadas)  # Saída: b) Vendas atualizadas: [2, 3, 4, 5]

"""
Nesta solução, comentamos a linha que tenta alterar o preço do "Smartphone", pois 
sabemos que isso causará um erro. O objetivo é que o aluno faça essa tentativa por 
conta própria para enfrentar o erro e, assim, compreender a imutabilidade das tuplas. 

Em seguida, demonstramos como modificar uma lista que está dentro da tupla, exibindo 
a natureza mutável das listas mesmo quando elas estão contidas em uma tupla imutável.
"""

print()


"""
Operações com Tuplas:
        Concatenação: (1, 2) + (3, 4)
        Repetição: (1, 2) * 3
        Verificar se um elemento está na tupla: 2 in (1, 2, 3)
"""

"""
Exemplo Prático: Planejamento de Viagem

Contexto: Imagine que você está planejando uma viagem por várias 
cidades. As cidades são representadas por números, e você deseja organizar a 
ordem das visitas, verificar cidades repetidas e ver se visitou uma cidade específica.
"""

#1. Concatenação de Tuplas - Adicionando destinos à sua viagem

#Suponha que você já planejou visitar as cidades 1 e 2. 
#Depois de pensar um pouco, decidiu também visitar as cidades 3 e 4.
primeiras_cidades = (1, 2)
proximas_cidades = (3, 4)

roteiro_viagem = primeiras_cidades + proximas_cidades
print(roteiro_viagem)  # Saída: (1, 2, 3, 4)

#2. Repetição - Visitando algumas cidades mais de uma vez:

#Suponha que as cidades 1 e 2 sejam seus destinos favoritos e 
#você deseja visitá-las três vezes durante sua viagem.
cidades_favoritas = (1, 2)

roteiro_repetido = cidades_favoritas * 3
print(roteiro_repetido)  # Saída: (1, 2, 1, 2, 1, 2)

#3. Verificando se uma cidade está em seu roteiro:

#Durante o planejamento, você se pergunta se incluiu a cidade 2 em seu roteiro.

roteiro_total = (1, 2, 3, 4, 1, 2, 1, 2)

cidade_inclusa = 2 in roteiro_total
print(cidade_inclusa)  # Saída: True

"""
Neste exemplo prático, utilizamos as operações básicas com 
tuplas para organizar um roteiro de viagem. Concatenamos cidades para 
estender nosso roteiro, repetimos visitas a cidades favoritas e verificamos se uma 
cidade específica está incluída no planejamento.
"""
print()



"""
Exercício: Manipulando Sequências de Números

Contexto: Você está trabalhando com sequências de números em um software 
de análise. Para isso, você utiliza tuplas, uma vez que as sequências são fixas 
e não precisam de alterações. Contudo, existem algumas operações com as sequências 
que você precisa realizar para obter novos conjuntos de dados.

Objetivo: Utilize operações com tuplas para manipular e analisar sequências de números.

Instruções:

    1. Concatenação de Sequências:
        Você possui duas sequências: A = (1, 2) e B = (3, 4).
        Crie uma nova sequência C combinando as sequências A e B.

    2. Repetição de Sequências:
        Suponha que você queira repetir a sequência A três vezes para criar uma nova sequência D.
        Faça essa operação e registre o resultado em D.

    3. Análise de Elemento em Sequência:
        Utilizando a sequência E = (1, 2, 3, 4, 1, 2, 1, 2), verifique se o número 2 está presente.

Questões:

a) Qual é a sequência resultante C após a concatenação?

b) Qual é a sequência D após repetir a sequência A três vezes?

c) O número 2 está presente na sequência E?

O exercício busca ensinar as operações básicas que podem ser 
realizadas com tuplas. Ao final, você deve ser capaz de manipular 
e combinar diferentes tuplas para obter novos conjuntos de dados.
"""

#Solução:

#   1. Concatenação de Sequências:
#       Você possui duas sequências: A = (1, 2) e B = (3, 4).
#       Crie uma nova sequência C combinando as sequências A e B.

A = (1, 2)
B = (3, 4)

C = A + B

print(C)

#   2. Repetição de Sequências:
#      Suponha que você queira repetir a sequência A três vezes para criar uma nova sequência D.
#      Faça essa operação e registre o resultado em D.

D = A * 3

print(D)

#   3. Análise de Elemento em Sequência:
#       Utilizando a sequência E = (1, 2, 3, 4, 1, 2, 1, 2), verifique se o número 2 está presente.

E = (1, 2, 3, 4, 1, 2, 1, 2)

numero_presente = 2 in E

print(numero_presente)

print()
#Respostas as Questões:

#a) Qual é a sequência resultante C após a concatenação?
print("a) C =", C)

#b) Qual é a sequência D após repetir a sequência A três vezes?
print("b) D =", D)

#c) O número 2 está presente na sequência E?
print("c)", numero_presente)


"""
Métodos de Tuplas:
        count(): conta o número de vezes que um elemento aparece na tupla.
        index(): retorna o índice do primeiro elemento que corresponde ao valor especificado.
"""

"""
Exemplo Prático: Gerenciamento de Vendas de Produtos

Contexto: Imagine que você é um gerente em uma loja de eletrônicos e deseja analisar 
as vendas dos produtos ao longo da semana. Cada produto vendido é representado por 
um código numérico.
"""

#1. Uso do método count():

#Suponha que você tenha uma tupla que representa as vendas de produtos 
#durante a semana: vendas = (101, 102, 103, 101, 102, 101, 104), onde cada 
#número é um código de produto.

#Se quisermos saber quantas vezes o produto de código 101 foi 
#vendido durante a semana, pode usar o método count():


vendas = (101, 102, 103, 101, 102, 101, 104)
vendas_produto_101 = vendas.count(101)
print(f"O produto 101 foi vendido {vendas_produto_101} vezes.")

#Uso do método index():

#Agora, imagine que você queira saber quando o produto de 
#código 103 foi vendido pela primeira vez durante a semana. 

#Para isso, pode usar o método index():
vendas = (101, 102, 103, 101, 102, 101, 104, 103)
primeiro_dia_venda_103 = vendas.index(103) + 1
print(f"O produto 103 foi vendido pela primeira vez no {primeiro_dia_venda_103}° dia da semana.")

"""
Neste exemplo, utilizamos os métodos count() e index() das tuplas para analisar 
as vendas de produtos em uma loja. O método count() nos ajudou a determinar a 
quantidade de vendas de um produto específico, enquanto o método index() nos 
informou quando um produto foi vendido pela primeira vez.
"""
print()

"""
Exercício: Análise de Avaliações de Filmes

Contexto: Você é um analista em uma plataforma de streaming e recebeu 
uma lista de avaliações de um filme recém-lançado. As avaliações são dadas como 
estrelas, variando de 1 a 5. Você deve analisar essas avaliações para fornecer 
insights sobre a recepção do filme.

Dados fornecidos: avaliacoes = (5, 4, 4, 3, 5, 2, 4, 3, 5, 5, 1, 4, 3, 5, 2)

Objetivo: Use os métodos de tupla para responder às seguintes perguntas:

    Quantidade de Avaliações de 5 estrelas:
        Quantas vezes o filme foi avaliado com 5 estrelas?
    Primeira Avaliação de 1 estrela:
        Em que posição da sequência aparece a primeira avaliação de 1 estrela?

Instruções:

a) Utilize o método count() para determinar o número de avaliações 
de 5 estrelas na tupla avaliacoes.

b) Utilize o método index() para encontrar a posição da primeira 
avaliação de 1 estrela na tupla avaliacoes.

Questões:

a) Quantas avaliações de 5 estrelas o filme recebeu?

b) Qual é a posição da primeira avaliação de 1 estrela?

Este exercício tem como objetivo familiarizar com os métodos count() 
e index() de tuplas, aplicando-os em um contexto prático de análise de 
dados. 

Ao final, você deve ser capazes de utilizar esses métodos para 
extrair informações relevantes de uma tupla.
"""

#Solução:

#Dados fornecidos
avaliacoes = (5, 4, 4, 3, 5, 2, 4, 3, 5, 5, 1, 4, 3, 5, 2)

#A) Quantas avaliações de 5 estrelas o filme recebeu?
numero_de_cinco_estrelas = avaliacoes.count(5)

print(f"a) O filme recebeu {numero_de_cinco_estrelas} avaliações de 5 estrelas.")

#B) Qual é a posição da primeira avaliação de 1 estrela?
posicao_primeira_uma_estrela = avaliacoes.index(1) + 1 # Adicionamos 1 porque os índices começam em 0

print(f"b) A primeira avaliação de 1 estrela está na {posicao_primeira_uma_estrela}ª posição.")

"""
Desempacotamento de Tuplas:
        Atribuindo valores de uma tupla a múltiplas variáveis: a, b, c = (1, 2, 3)
"""

"""
Exemplo Prático: Gestão de Estudantes

Contexto: Imagine que você é um professor e recebe informações de um estudante em 
forma de tupla. Essa tupla contém o nome do estudante, sua idade e sua nota média. 

Para facilitar o acesso a esses dados, você pode desempacotar a tupla em variáveis individuais.
"""

#Exemplo:

#1. Dados fornecidos:

#Suponha que você tenha a seguinte tupla com informações do estudante: 

estudante_info = ("João", 20, 85.5) # onde "João" é o nome do estudante, 20 
                                    #é sua idade e 85.5 é sua nota média.
    

#2. Desempacotamento:

#Agora, para desempacotar esses dados em variáveis individuais, você pode fazer o seguinte:


nome, idade, nota_media = estudante_info

print(f"Nome do Estudante: {nome}")
print(f"Idade: {idade}")
print(f"Nota Média: {nota_media}")

"""
Neste exemplo, através do desempacotamento de tuplas, conseguimos 
atribuir os valores contidos em estudante_info a três variáveis 
separadas (nome, idade e nota_media). Isso permite um acesso mais 
direto e claro aos valores individualmente.
"""
print()

"""
Exercício: Gestão de Pacotes de Viagem

Contexto: Você trabalha em uma agência de turismo e tem pacotes 
de viagem que são representados como tuplas. Cada pacote contém o 
destino, o número de noites e o preço. Para facilitar o processamento 
desses pacotes, você precisa desempacotar os detalhes em variáveis individuais.

Dados fornecidos:

Considere o seguinte pacote de viagem: pacote_viagem = ("Paris", 5, 1500), onde:

    "Paris" é o destino da viagem.
    5 é o número de noites.
    1500 é o preço do pacote em dólares.

Objetivo: Desempacote os detalhes do pacote de viagem em variáveis individuais e imprima as informações.

Instruções:

    Atribua os valores da tupla pacote_viagem a três variáveis: destino, noites e preco.
    Imprima o destino, o número de noites e o preço do pacote.

Questões:

a) Qual é o destino do pacote de viagem?
b) Por quantas noites é o pacote?
c) Qual é o preço do pacote?

Este exercício visa ajudar a compreenderem e praticarem o desempacotamento 
de tuplas, uma técnica útil para atribuir múltiplos valores a variáveis de 
uma vez. Ao final, os alunos devem ser capazes de extrair informações de 
uma tupla e utilizá-las separadamente.
"""

#Solução:

# Dados fornecidos
pacote_viagem = ("Paris", 5, 1500)

# Desempacotamento da tupla
destino, noites, preco = pacote_viagem

# Imprimir as informações do pacote
print(f"a) Destino: {destino}")
print(f"a) Número de Noites: {noites}")
print(f"a) Preço: R$ {preco}")


"""
 Aplicações Práticas:
        Retornando múltiplos valores de uma função usando tuplas.
        Uso de tuplas em loops for: for a, b in [(1,2), (3,4)]:
        Trocando valores entre duas variáveis: a, b = b, a
"""

"""
Exemplo Prático: Analisando Vendas

Contexto: Você é um analista em uma loja e precisa acompanhar as 
vendas diárias de dois produtos: A e B. Seu objetivo é calcular o total 
vendido e o produto mais vendido no dia.
"""

#1. Retornando múltiplos valores de uma função usando tuplas

#Você quer criar uma função que retorna o total vendido e o produto mais vendido do dia.
def analisar_vendas(vendas_A, vendas_B):
    
    total_vendido = vendas_A + vendas_B
    mais_vendido = "A" if vendas_A > vendas_B else "B"
    return total_vendido, mais_vendido

total, top_produto = analisar_vendas(100, 85)
print(f"Total Vendido: {total}")
print(f"Produto Mais Vendido: {top_produto}")

print()

#2. Uso de tuplas em loops for

#Suponha que você tenha uma lista de vendas de ambos os produtos em 
#pares para alguns dias, e você quer imprimir as vendas de cada dia.
vendas = [(100, 90), (110, 115), (105, 100)]

for vendas_A, vendas_B in vendas:
    print(f"Vendas de A: {vendas_A}, Vendas de B: {vendas_B}")
    
print()

#3. Trocando valores entre duas variáveis

#No final do dia, você percebeu que confundiu as vendas dos 
#produtos A e B e precisa trocar os valores para corrigir.
vendas_A = 100
vendas_B = 85
vendas_A, vendas_B = vendas_B, vendas_A
print(f"Vendas Corrigidas - A: {vendas_A}, B: {vendas_B}")

"""
Esses são exemplos práticos de como as tuplas podem ser úteis 
em diferentes situações na programação, especialmente em Python, onde 
elas são amplamente utilizadas para desempacotamento, retorno múltiplo de funções e em iterações.
"""

"""
Exercício: Gerenciamento de Estoque

Contexto: Você trabalha no controle de estoque de uma empresa de 
eletrônicos. A empresa vende dois produtos populares: smartphones e smartwatches. 

Diariamente, você precisa calcular o total de produtos vendidos, identificar 
qual produto foi mais vendido e reorganizar os números caso haja algum erro nas entradas.

Instruções:

    1. Retornando múltiplos valores de uma função usando tuplas.
        - Crie uma função chamada resumo_vendas que aceite 
        dois argumentos: vendas_smartphones e vendas_smartwatches.
        
        - A função deve retornar o total de vendas e o nome do produto 
        mais vendido (seja "smartphone" ou "smartwatch").
        
        - Exemplo de entrada: 80 smartphones vendidos e 70 smartwatches vendidos.
        - Pergunta: Qual é o total de vendas e qual produto foi mais vendido?

    2. Uso de tuplas em loops for.
        - Dada a lista vendas_semana = [(70, 65), (80, 82), (90, 88)], onde 
        cada tupla representa as vendas de smartphones e smartwatches em um dia, respectivamente.
        
        - Use um loop for para imprimir as vendas de smartphones e smartwatches para cada dia.
        - Pergunta: Quais foram as vendas de smartphones e smartwatches para cada dia?

    3. Trocando valores entre duas variáveis.
        - Suponha que você cometeu um erro e registrou as vendas de segunda-feira 
        de forma invertida: vendas_segunda = (65, 70), onde o primeiro valor é para 
        smartwatches e o segundo para smartphones.
        
        - Corrija essa entrada invertendo os valores.
        - Pergunta: Qual é a entrada corrigida para as vendas de segunda-feira?

Nota: Este exercício visa ajudar a compreenderem a versatilidade e aplicabilidade 
das tuplas em diferentes cenários de programação. 

Ao final, você será capaz de usar tuplas para múltiplas finalidades e manipular dados de forma eficiente.
"""

#Solução:

#1. Retornando múltiplos valores de uma função usando tuplas.

def resumo_vendas(vendas_smartphones, vendas_smartwatches):
    
    total_vendas = vendas_smartphones + vendas_smartwatches
    mais_vendido = "smartphone" if vendas_smartphones > vendas_smartwatches else "smartwatch"
    

    return total_vendas, mais_vendido


total, top_produto = resumo_vendas(80, 70)

print(f"Total de Vendas: {total}")
print(f"Produto Mais Vendido: {top_produto}")

print()

#2. Uso de tuplas em loops for.

vendas_semana = [(70, 65), (80, 82), (90, 88)]

for smartphones, smartwatches in vendas_semana:
    print(f"Vendas de smartphones: {smartphones}, Vendas de smartwatches: {smartwatches}")
    
print()

#3. Trocando valores entre duas variáveis.

vendas_segunda = (65, 70)

#utiliza um recurso do Python chamado fatiamento (slicing). 
#Especificamente, o [::-1] é um atalho para inverter a ordem dos 
#elementos dentro de uma sequência (que pode ser uma lista, string, tupla, etc.).
vendas_segunda = vendas_segunda[::-1]

print(f"Vendas corrigidas de segunda-feira - Smartphones: {vendas_segunda[0]}, Smartwatches: {vendas_segunda[1]}")
    

"""
Comparando Tuplas:
        Tuplas podem ser comparadas usando operadores de comparação: (1, 2) < (1, 3)
"""

"""
Exemplo Prático: Comparando Tuplas

No Python, quando duas tuplas são comparadas, a comparação é realizada 
elemento por elemento, começando pelo primeiro. Assim que um par de 
elementos é encontrado onde um é menor (ou maior) que o outro, a comparação 
retorna True ou False e não prossegue para os próximos elementos. 

Se todos os elementos comparados forem iguais e uma das tuplas for mais curta 
que a outra, a tupla mais curta é considerada menor.

Aqui estão alguns exemplos para ilustrar isso:
"""

#1. Comparando o Primeiro Elemento:
t1 = (1, 2)
t2 = (1, 3)
print(t1 < t2)  # Isso imprimirá True, porque 2 (de t1) é menor que 3 (de t2).

#2. Ignorando Elementos Iguais:
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print(t1 < t2)  # Isso imprimirá True, porque, apesar de 1 e 2 
                #serem iguais em ambas as tuplas, 3 (de t1) é menor que 4 (de t2).
    
    
#3. Comparando Tuplas de Diferentes tamanhos:
t1 = (1, 2)
t2 = (1, 2, 3)
print(t1 < t2)  # Isso imprimirá True, porque t1 é mais curta 
                #que t2, mesmo que todos os seus elementos correspondentes sejam iguais.
    
#4. Comparação de Elementos de Diferentes Tipos:
#Supondo que as tuplas tenham elementos de diferentes tipos, o Python irá 
#compará-los com base em suas ordens de classificação interna (por exemplo, int antes de string).
t1 = (1, "apple")
t2 = (2, "banana")
print(t1 < t2)  # Isso imprimirá True porque 1 é menor que 2. 
                #A comparação não chega a comparar "apple" com "banana".

"""
Estes exemplos mostram como as tuplas são comparadas no Python. Esta forma 
de comparação é muito útil em diversas situações, como quando as tuplas são 
usadas como chaves em dicionários ou quando estão em uma lista e você quer ordená-las.
"""
print()

"""
Exercício: Comparação de Tuplas

Dadas as seguintes tuplas:

t1 = (3, 5)
t2 = (3, 4, 10)
t3 = (3, 6)
t4 = (2, 100)
t5 = (3, 5)

Responda as seguintes questões:

    1. Qual é maior: t1 ou t2?
    2. t3 é maior que t1?
    3. Compare t4 e t1. Qual é menor?
    4. t1 e t5 são iguais?

Nota: O objetivo deste exercício é fazer com que entendam o conceito
de comparação de tuplas em profundidade, observando 
a ordem dos elementos e como os diferentes elementos em diferentes posições 
influenciam o resultado da comparação.
"""

#Solução:

t1 = (3, 5)
t2 = (3, 4, 10)
t3 = (3, 6)
t4 = (2, 100)
t5 = (3, 5)

#Repostas

#1. Qual é maior: t1 ou t2?
    
if t1 > t2:
    
    r1 = "t1"

else:
    
    r1 = "t2"
    
print(f"1. {r1} é maior")

#2. t3 é maior que t1?

r2 = t3 > t1

print(f"2. t3 é maior que t1? {r2}")

#3. Compare t4 e t1. Qual é menor?

if t4 < t1:
    
    r3 = "t4"

else:
    
    r3 = "t1"
    
print(f"3. {r3} é menor")

#4. t1 e t5 são iguais?

r4 = t1 == t5

print(f"4. t1 e t2 são iguais? {r4}")

"""
Diferenças entre Listas e Tuplas:

    Quando e por que usar uma em vez da outra
"""

"""
Exemplo Prático sobre Diferenças entre Listas e Tuplas:

Imagine que você é um desenvolvedor de software trabalhando em um 
sistema de gerenciamento para uma biblioteca. O sistema mantém um registro 
de todos os livros disponíveis na biblioteca. Cada livro tem atributos como 
título, autor, ISBN, ano de publicação, etc.
"""

#1. Listas:
#Para os livros que são emprestados frequentemente, você deseja manter 
#uma lista de "livros mais emprestados". Esta lista é dinâmica; os livros podem 
#ser adicionados ou removidos com base em sua popularidade de empréstimo.
livros_mais_emprestados = ['O Pequeno Príncipe', '1984', 'Dom Quixote']

#Agora, suponha que 'O Senhor dos Anéis' se tornou um livro popular 
#recentemente e você deseja adicioná-lo à lista.
livros_mais_emprestados.append('O Senhor dos Anéis')

#Neste caso, as listas são ideais porque elas são mutáveis e você pode 
#facilmente alterar seu conteúdo.

print(livros_mais_emprestados)

#-------------------------------

#Tuplas:
#Para cada livro, as informações básicas, como título, autor e ISBN, são fixas. 
#Elas não mudam uma vez que o livro é adicionado ao sistema. Aqui, uma tupla é uma boa escolha.
livro_info = ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', '978-3-16-148410-0')

#Uma vez definida, você não pode alterar os detalhes do livro nesta tupla. 
#Isso garante a imutabilidade e a integridade dos dados. Se por algum motivo você 
#precisar atualizar essas informações, você teria que criar uma nova tupla.

"""
Quando e Por Que Usar Uma em Vez da Outra:

    Listas:
        - Quando os dados são dinâmicos e podem mudar ao longo do tempo.
        - Quando você precisa de métodos como append(), remove(), etc.
        - Para sequências de tamanho variável.
        
    Tuplas:
        - Quando os dados não devem ser alterados (imutabilidade).
        - Para garantir a integridade dos dados.
        - Para usar como chave em dicionários (listas não podem ser usadas como chaves).
        - Para melhorar a eficiência, pois tuplas são geralmente mais rápidas 
        para iteração e processamento do que listas, devido à sua imutabilidade.

Espero que este exemplo tenha ajudado a entender as diferenças entre listas e tuplas e quando usar cada uma delas!
"""
print()

"""
Exercício: Diferenças entre Listas e Tuplas

Contexto:
Você é o arquiteto de software de uma startup de turismo. Seu software 
precisa lidar com informações sobre destinos turísticos e os feedbacks 
dos usuários sobre esses destinos.

Tarefas:

    1. Destinos Turísticos:
    Cada destino turístico tem informações fixas como nome, país, e um 
    código identificador único. Essas informações não mudam uma vez que o destino é adicionado ao sistema.
    
        Crie uma representação adequada para um destino turístico no sistema.

    2. Feedbacks dos Usuários:
    Os usuários do sistema podem adicionar feedbacks sobre os destinos 
    visitados. Estes feedbacks são dinâmicos, já que os usuários 
    podem adicionar, editar ou deletar seus comentários.
        
        Crie uma representação adequada para armazenar feedbacks de um destino turístico.

    3. Análise:
        Explique por que você escolheu a estrutura de dados 
        específica (lista ou tupla) para cada um dos casos acima.
        
        Dê um exemplo de uma situação em que seria desvantajoso usar a estrutura 
        de dados oposta em cada um dos casos.

Objetivo:
O principal objetivo deste exercício é fazer com que você pense sobre a natureza 
mutável das listas e a natureza imutável das tuplas, e como essa característica influencia 
a decisão de qual estrutura de dados usar em diferentes cenários práticos.
"""

#Solução: Diferenças entre Listas e Tuplas

#1. Destinos Turísticos:

#Como o nome, país e código identificador de um destino turístico 
#são fixos e não mudam uma vez que o destino é adicionado ao 
#sistema, é apropriado usar uma tupla.
destino_turistico = ("Torre Eiffel", "França", "FR-001")

print(destino_turistico)

print()


#2. Feedbacks dos Usuários

#Os feedbacks dos usuários são dinâmicos, e é necessário ter 
#a capacidade de adicionar, editar ou remover comentários. Portanto, uma 
#lista é a estrutura de dados adequada.
feedbacks_torre_eiffel = [
    "Maravilhoso!",
    "A vista é espetacular.",
    "Muito lotado durante a temporada alta."
]

print(feedbacks_torre_eiffel)

print()

#Para adicionar um novo feedback:
feedbacks_torre_eiffel.append("Recomendo visitar à noite.")


print(feedbacks_torre_eiffel)


#3. Análise:

"""
3. Análise:

        - Para o Destino Turístico: Eu escolhi a tupla porque é imutável, 
        garantindo que os detalhes fundamentais do destino não sejam alterados 
        acidentalmente durante a execução do programa.

        - Desvantagem de usar lista aqui: Se usássemos uma lista para representar 
        um destino turístico, correríamos o risco de modificar acidentalmente as 
        informações fundamentais, como o nome do destino ou seu código identificador. 
        Além disso, as tuplas são, em geral, mais leves em termos de uso de memória do que listas.

        - Para os Feedbacks dos Usuários: Escolhi a lista porque permite mutabilidade, o 
        que é necessário para acomodar as adições, edições e remoções dinâmicas de 
        feedbacks dos usuários.

        Desvantagem de usar tupla aqui: Se usássemos uma tupla para armazenar 
        feedbacks, cada vez que quiséssemos adicionar, editar ou remover um comentário, 
        teríamos que criar uma nova tupla. Isso não seria eficiente e tornaria o processo 
        de gerenciamento de feedbacks complicado e menos dinâmico.

Espero que esta solução ajude a entender as considerações práticas ao escolher entre 
listas e tuplas em diferentes cenários!
"""
print()





