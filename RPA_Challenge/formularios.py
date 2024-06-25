from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from openpyxl import load_workbook

# Define o caminho e o nome do arquivo Excel contendo os dados do formulário.
nomeCaminhoArquivo = 'challenge.xlsx'

# Abre a planilha Excel especificada.
planilha_aberta = load_workbook(filename=nomeCaminhoArquivo)

# Seleciona a aba específica da planilha chamada 'Dados'.
sheet_selecionada = planilha_aberta['Dados']

abrirnavegador = webdriver.Chrome()
abrirnavegador.get('https://rpachallenge.com/')
        
b = abrirnavegador.find_element(By.XPATH, "//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")
b.click()

sleep(2)
for linha in range(2, len(sheet_selecionada['A']) + 1):
    First_Name = sheet_selecionada[f'A{linha}'].value
    Last_Name = sheet_selecionada[f'B{linha}'].value
    Company_Name = sheet_selecionada[f'C{linha}'].value
    Role_in_Company = sheet_selecionada[f'D{linha}'].value
    Address = sheet_selecionada[f'E{linha}'].value
    Email = sheet_selecionada[f'F{linha}'].value
    Phone_Number = sheet_selecionada[f'G{linha}'].value
    if Address and Company_Name and Phone_Number and Role_in_Company and Last_Name and First_Name and Email:
        
	# '//' Seleciona todos os elementos em qualquer lugar do documento que segue este caminho input
	# seleciona os elementos input que possuem o atributo ng-reflect-name o símbolo @ em um XPath é usado para
	# selecionar atributos de um elemento HTML, neste caso seleciona input que possue o atributo ng-reflect-name com
	# o valor labelAddress
        textobox = abrirnavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
        textobox.clear()
        textobox.send_keys(Address)
        
        
        textobox = abrirnavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
        textobox.clear()
        textobox.send_keys(Company_Name)
        
        
        textobox = abrirnavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
        textobox.clear()
        textobox.send_keys(Phone_Number)
        
       
        textobox = abrirnavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
        textobox.clear()
        textobox.send_keys(Role_in_Company)
        
        textobox = abrirnavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
        textobox.clear()
        textobox.send_keys(Last_Name)
        
        textobox = abrirnavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
        textobox.clear()
        textobox.send_keys(First_Name)
        
        textobox = abrirnavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
        textobox.clear()
        textobox.send_keys(Email)
        sleep(0.1)
        botao = abrirnavegador.find_element(By.XPATH, "//input[@type='submit']")
        botao.click()
        