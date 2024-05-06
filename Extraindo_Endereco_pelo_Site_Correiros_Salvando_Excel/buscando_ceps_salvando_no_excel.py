from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera  # Importando o PyAutoGUI com um alias
from openpyxl import load_workbook
import pyautogui
import xlsxwriter
import os

# Inicializando o WebDriver
abrirNavegador = webdriver.Chrome()
abrirNavegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

tempoEspera.sleep(3)  # Espera 4 segundos para carregar a página

abrirNavegador.find_element(By.XPATH, '//*[@id="endereco"]').send_keys('05892387')

tempoEspera.sleep(3)

abrirNavegador.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()

tempoEspera.sleep(2)

rua = abrirNavegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
tempoEspera.sleep(1)
print(rua)

tempoEspera.sleep(2)

bairro = abrirNavegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
tempoEspera.sleep(1)
print(bairro)

tempoEspera.sleep(2)

cidade = abrirNavegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
tempoEspera.sleep(1)
print(cidade)

tempoEspera.sleep(2)

cep = abrirNavegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
tempoEspera.sleep(1)
print(cep)

tempoEspera.sleep(3)

nome_arquivo_cep = 'C:\\Valor_do_Dolar_e_Euro\\PesquisaEndereco_1.xlsx'
planilhaDadosEndereco = load_workbook(nome_arquivo_cep)

sheet_selecionada = planilhaDadosEndereco['Dados']


valor_celula_A2 = sheet_selecionada['A2'].value

# Verifica se a célula A2 está vazia
if sheet_selecionada['A2'].value is None:
    linha = 2  # Começa a gravar a partir da célula A2
else:
    # Obtém a próxima linha disponível
    linha = len(sheet_selecionada['A']) + 1
    
colunaA = "A" + str(linha)
colunaB = "B" + str(linha)
colunaC = "C" + str(linha)
colunaD = "D" + str(linha)

sheet_selecionada[colunaA] = rua
sheet_selecionada[colunaB] = bairro
sheet_selecionada[colunaC] = cidade
sheet_selecionada[colunaD] = cep

planilhaDadosEndereco.save(filename=nome_arquivo_cep)

os.startfile(nome_arquivo_cep)


