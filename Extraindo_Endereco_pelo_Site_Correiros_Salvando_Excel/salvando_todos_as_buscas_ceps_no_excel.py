# Este script automatiza a pesquisa de endereços pelo CEP no site dos Correios
# e armazena os resultados em um arquivo Excel especificado.
# Ele utiliza o Selenium para interagir com o navegador Chrome e o PyAutoGUI
# para pausas temporárias. Além disso, faz uso da biblioteca openpyxl para
# carregar e manipular os dados em um arquivo Excel existente.

# Importando as bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
from openpyxl import load_workbook
import os

# Caminho do arquivo Excel que contém os CEPs a serem pesquisados e onde serão
# armazenados os resultados
nome_arquivo_cep = 'C:\\Valor_do_Dolar_e_Euro\\PesquisaEndereco_2.xlsx'

# Carrega o arquivo Excel e seleciona a planilha 'CEP'
planilhaDadosEndereco = load_workbook(nome_arquivo_cep)
sheet_selecionada = planilhaDadosEndereco['CEP']

# Inicializando o WebDriver do Chrome
abrirNavegador = webdriver.Chrome()
abrirNavegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

# Espera 3 segundos para a página carregar
tempoEspera.sleep(3)

# Preenche o campo de endereço com um CEP inicial
abrirNavegador.find_element(By.XPATH, '//*[@id="endereco"]').send_keys('05892387')

# Espera 3 segundos após preencher o CEP
tempoEspera.sleep(3)

# Clica no botão de pesquisa
abrirNavegador.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()

# Espera 4 segundos para os resultados serem carregados
tempoEspera.sleep(4)

# Itera sobre as linhas da planilha 'CEP' para pesquisar cada CEP
for linha in range(2, len(sheet_selecionada['A']) + 1):
    # Clica no botão de nova busca para limpar o campo de endereço
    tempoEspera.sleep(3)
    abrirNavegador.find_element(By.XPATH, '//*[@id="btn_nbusca"]').click()
    
    # Obtém o valor do CEP da célula na coluna A da linha atual
    valor_celula = sheet_selecionada['A{}'.format(linha)].value

    # Insere o valor do CEP no campo de endereço
    abrirNavegador.find_element(By.XPATH, '//*[@id="endereco"]').send_keys(valor_celula)

    # Espera 3 segundos após preencher o CEP
    tempoEspera.sleep(3)

    # Clica no botão de pesquisa
    abrirNavegador.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()

    # Espera 4 segundos para os resultados serem carregados
    tempoEspera.sleep(4)
    
    # Extrai os dados de rua, bairro, cidade e CEP dos resultados da pesquisa
    rua = abrirNavegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
    bairro = abrirNavegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
    cidade = abrirNavegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
    cep = abrirNavegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text

    # Adiciona os dados do endereço à planilha 'Dados'
    sheet_Dados_Imprimir_Endereco = planilhaDadosEndereco['Dados']
    linhaCorrentePlanilhaCEP = len(sheet_Dados_Imprimir_Endereco['A']) + 1
    
    colunaA = "A" + str(linhaCorrentePlanilhaCEP)
    colunaB = "B" + str(linhaCorrentePlanilhaCEP)
    colunaC = "C" + str(linhaCorrentePlanilhaCEP)
    colunaD = "D" + str(linhaCorrentePlanilhaCEP)

    # Atribui os valores às células correspondentes na planilha 'Dados'
    sheet_Dados_Imprimir_Endereco[colunaA] = rua
    sheet_Dados_Imprimir_Endereco[colunaB] = bairro
    sheet_Dados_Imprimir_Endereco[colunaC] = cidade
    sheet_Dados_Imprimir_Endereco[colunaD] = cep
 
# Salva as alterações no arquivo Excel
planilhaDadosEndereco.save(filename=nome_arquivo_cep)

# Abre o arquivo Excel após a conclusão das pesquisas
os.startfile(nome_arquivo_cep)
