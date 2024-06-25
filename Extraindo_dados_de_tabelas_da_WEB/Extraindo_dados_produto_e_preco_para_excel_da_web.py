# Importa as bibliotecas necessárias para o projeto
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from openpyxl import load_workbook
from openpyxl.utils import quote_sheetname
import os

# Define o nome do arquivo Excel que será usado para armazenar os dados
nome_arquivo = 'ProdutoWeb.xlsx'
# Carrega a planilha Excel
planilhaDadosTabela = load_workbook(nome_arquivo)
# Seleciona a aba 'Dados' da planilha
sheet_selecionada = planilhaDadosTabela['Dados']

# Inicia o navegador Chrome
navegador = opcoesSelenium.Chrome()
# Navega para o site específico onde a tabela está localizada
navegador.get('https://www.mercadolivre.com.br/')

# Procura o campo de busca e insere 'carteira'
navegador.find_element(By.NAME, 'as_word').send_keys('carteira')

# Espera 2 segundos para simular uma pausa natural do usuário
sleep(2)

# Clica no botão de busca para realizar a pesquisa
navegador.find_element(By.XPATH, '/html/body/header/div/div[2]/form/button').click()

# Espera 6 segundos para garantir que a página de resultados carregue completamente
sleep(4)

# Encontra todos os elementos de produtos listados na página
dadosProdutos = navegador.find_elements(By.CLASS_NAME, 'ui-search-layout__item')

# Define os cabeçalhos das colunas na primeira linha (caso ainda não estejam definidos)
sheet_selecionada['A1'] = 'Produto'
sheet_selecionada['B1'] = 'Preço'
sheet_selecionada['C1'] = 'URL'

# Itera sobre cada produto listado
for informacoes in dadosProdutos:
    # Extrai o nome do produto
    nomeProduto = informacoes.find_element(By.CLASS_NAME, 'ui-search-item__title').text
    # Extrai o preço do produto (parte inteira)
    precoProduto = informacoes.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text
    try:
        # Tenta extrair o valor dos centavos usando a classe específica
        centavosProduto = informacoes.find_element(By.CLASS_NAME, 'andes-money-amount__cents--superscript-24').text
    except:
        # Se não houver centavos, define como '00'
        centavosProduto = '00'
    
    # Extrai a URL do produto
    urlProduto = informacoes.find_element(By.TAG_NAME, "a").get_attribute("href")
    
    #print(nomeProduto + " - " + precoProduto + "," + str(centavosProduto) + " - " + urlProduto)
    
    # Define a próxima linha disponível na planilha para inserir dados
    linha = len(sheet_selecionada['A']) + 1
        
    # Define as colunas para inserção de dados
    colunaA = "A" + str(linha) # A1, A2, ...
    colunaB = "B" + str(linha) # B1, B2, ...
    colunaC = "C" + str(linha) # C1, C2, ...
    
    # Formata o preço juntando a parte inteira e os centavos
    precoTexto = precoProduto + ',' + centavosProduto
    # Remove pontos do preço para evitar problemas de formatação
    precoSemPonto = precoTexto.replace('.','')
    # Substitui vírgulas por pontos para converter para formato de ponto flutuante
    precoSemPonto2 = precoSemPonto.replace(',','.')
    
    # Converte o preço formatado para um valor float
    precoSemPonto2 = float(precoSemPonto2)
    
    # Insere os dados do produto nas respectivas colunas da planilha
    sheet_selecionada[colunaA] = nomeProduto
    sheet_selecionada[colunaB] = precoSemPonto2
    sheet_selecionada[colunaC] = urlProduto

# Salva o arquivo Excel com as novas informações
planilhaDadosTabela.save(filename=nome_arquivo)

# Abre o arquivo Excel atualizado para visualização
os.startfile(nome_arquivo)
