# Importa as bibliotecas necessárias
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from openpyxl import load_workbook
import os

# Inicia o navegador Chrome
navegador = opcoesSelenium.Chrome()
# Navega para o site específico onde a tabela está localizada
navegador.get('https://rpachallengeocr.azurewebsites.net/')

# Define o nome do arquivo Excel que será usado para armazenar os dados
nome_arquivo = 'Dados_Tabela.xlsx'
# Carrega a planilha Excel
planilhaDadosTabela = load_workbook(nome_arquivo)
# Seleciona a aba 'Dados' da planilha
sheet_selecionada = planilhaDadosTabela['Dados']

# Inicia um loop para iterar por 3 páginas da tabela no site
i = 1
while i < 4:
    # Encontra a tabela no site usando XPath
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
    # Encontra todas as linhas da tabela
    linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')
    # Encontra todas as colunas da tabela
    colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')
    
    # Seleciona a aba 'Dados' da planilha (redundante, mas pode ser útil se a aba mudar no futuro)
    sheet_dados = planilhaDadosTabela['Dados']

    # Loop por cada linha da tabela
    for linhaAtual in linhas:
        # Imprime o texto da linha no console para verificação
        print(linhaAtual.text)
        # Define a linha para inserir dados na planilha Excel
        linha = len(sheet_dados['A']) + 1
        
        # Define as colunas para inserção de dados
        colunaA = "A" + str(linha) # A1, A2, ...
        colunaB = "B" + str(linha) # B1, B2, ...
        colunaC = "C" + str(linha) # C1, C2, ...
        
        # Obtém o texto da linha atual e o divide em partes separadas por espaço
        texto = linhaAtual.text
        texto2 = texto.split(" ")
        
        # Atribui os valores das partes separadas às colunas da planilha
        if len(texto2) >= 3: # Certifica-se de que há pelo menos 3 partes para evitar erros
            sheet_dados[colunaA] = texto2[0]
            sheet_dados[colunaB] = texto2[1]
            sheet_dados[colunaC] = texto2[2]
      
    # Incrementa o contador de páginas
    i += 1
    # Aguarda 2 segundos antes de continuar
    sleep(2)
    
    # Clica no botão "Próximo" para ir para a próxima página da tabela
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    
    # Aguarda 2 segundos para garantir que a próxima página seja carregada
    sleep(2)

# Salva o arquivo Excel com as novas informações
planilhaDadosTabela.save(filename=nome_arquivo)

# Abre o arquivo Excel atualizado para visualização
os.startfile(nome_arquivo)
