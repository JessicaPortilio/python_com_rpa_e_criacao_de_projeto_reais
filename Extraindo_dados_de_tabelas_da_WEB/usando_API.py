import requests
from openpyxl import Workbook

# Função para buscar produtos na API do Mercado Livre
def buscar_produtos(query):
    # URL base da API do Mercado Livre para buscar produtos
    url = 'https://api.mercadolibre.com/sites/MLB/search'
    
    # Parâmetros da solicitação
    params = {
        'q': query,    # Consulta de pesquisa
        'limit': 30    # Limite de resultados
    }
    
    # Faz a solicitação GET para a API
    response = requests.get(url, params=params)
    
    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Retorna os resultados em formato JSON
        return response.json()['results']
    else:
        # Se a solicitação falhar, imprime uma mensagem de erro
        print('Erro ao buscar produtos:', response.text)
        return None

# Exemplo de como usar a função buscar_produtos
produtos = buscar_produtos('carteira')

if produtos:
    # Cria um novo arquivo Excel
    workbook = Workbook()
    sheet = workbook.active
    
    # Adiciona os cabeçalhos das colunas
    sheet.append(['Nome', 'Preço', 'URL'])
    
    # Adiciona os dados dos produtos
    for produto in produtos:
        nome = produto['title']
        preco = produto['price']
        url = produto['permalink']
        sheet.append([nome, preco, url])
    
    # Salva o arquivo Excel
    nome_arquivo_excel = 'Produtos_API.xlsx'
    workbook.save(nome_arquivo_excel)
    
    print(f'Dados salvos com sucesso em "{nome_arquivo_excel}"!')
else:
    print('Nenhum produto encontrado.')
