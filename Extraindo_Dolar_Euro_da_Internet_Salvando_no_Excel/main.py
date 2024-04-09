from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoPausaComputador  # Importando o PyAutoGUI com um alias
import pyautogui
import xlsxwriter
import os

# Inicializando o WebDriver
abrirNavegador = webdriver.Chrome()
abrirNavegador.get('https://www.google.com/')

tempoPausaComputador.sleep(4)  # Espera 4 segundos para carregar a página

# Procura o campo de busca pelo nome e insere 'Dolar hoje'
abrirNavegador.find_element(By.NAME, "q").send_keys('Dolar hoje')

tempoPausaComputador.sleep(4)  # Espera 4 segundos

# Pressiona a tecla Enter para fazer a busca
abrirNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

tempoPausaComputador.sleep(4)  # Espera 4 segundos

# Extrai o valor do dólar do resultado da busca no Google
valorDolarPeloGoogle = abrirNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

tempoPausaComputador.sleep(4)  # Espera 4 segundos

print(valorDolarPeloGoogle)  # Imprime o valor do dólar

tempoPausaComputador.sleep(2)  # Espera 2 segundos

# Limpa o campo de busca
abrirNavegador.find_element(By.NAME, "q").send_keys("")

tempoPausaComputador.sleep(4)  # Espera 4 segundos

pyautogui.press('tab')  # Simula o pressionamento da tecla 'Tab'

tempoPausaComputador.sleep(4)  # Espera 4 segundos

pyautogui.press('enter')  # Simula o pressionamento da tecla 'Enter'

tempoPausaComputador.sleep(4)  # Espera 4 segundos

# Insere 'Euro hoje' no campo de busca
abrirNavegador.find_element(By.NAME, "q").send_keys('Euro hoje')

tempoPausaComputador.sleep(4)  # Espera 4 segundos

# Pressiona a tecla Enter para fazer a busca
abrirNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

tempoPausaComputador.sleep(4)  # Espera 4 segundos

# Extrai o valor do euro do resultado da busca no Google
valorEuroPeloGoogle = abrirNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

tempoPausaComputador.sleep(4)  # Espera 4 segundos

print(valorEuroPeloGoogle)  # Imprime o valor do euro

tempoPausaComputador.sleep(2)  # Espera 2 segundos

# Define o caminho e nome do arquivo Excel a ser criado
nomeCaminhoArquivo = 'C:\\Valor_do_Dolar_e_Euro\\Impime Dolar e Euro Google.xlsx'

# Cria um novo arquivo Excel
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)

# Adiciona uma planilha ao arquivo
planilha1 = planilhaCriada.add_worksheet()

# Escreve os títulos 'Dolar' e 'Euro' nas células A1 e B1, respectivamente
planilha1.write('A1', 'Dolar')
planilha1.write('B1', 'Euro')

# Escreve os valores do dólar e do euro nas células A2 e B2, respectivamente
planilha1.write('A2', valorDolarPeloGoogle)
planilha1.write('B2', valorEuroPeloGoogle)

# Substitui as vírgulas por pontos nos valores do dólar e do euro
valorDolarPeloGoogle = valorDolarPeloGoogle.replace(',','.')
valorEuroPeloGoogle = valorEuroPeloGoogle.replace(',','.')

# Converte os valores do dólar e do euro para o tipo float
valor_Dolar_Tipo_Float = float(valorDolarPeloGoogle)
valor_Euro_Tipo_Float = float(valorEuroPeloGoogle)

# Escreve os valores convertidos nas células A3 e B3, respectivamente
planilha1.write('A3', valor_Dolar_Tipo_Float)
planilha1.write('B3', valor_Euro_Tipo_Float)

# Fecha o arquivo Excel
planilhaCriada.close()

# Abre o arquivo Excel
os.startfile(nomeCaminhoArquivo)
