# Importa a biblioteca xlsxwriter com um alias
import xlsxwriter as opcoesDoXlsxWriter  
# Importa a biblioteca os para operações de sistema
import os  

# Define o nome do arquivo Excel a ser criado
nomeCaminhoArquivo = 'PrimeiroExemplo.xlsx'  
# Cria um objeto Workbook
workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
# Adiciona uma nova worksheet ao Workbook  
sheetPadrao = workbook.add_worksheet()  

# Adicionando cabeçalhos de colunas e dados na worksheet

# Escreve o cabeçalho "Nome" na célula A1
sheetPadrao.write("A1", "Nome")  
# Escreve o cabeçalho "Idade" na célula B1
sheetPadrao.write("B1", "Idade")  
# Escreve o nome "Amanda" na célula A2
sheetPadrao.write("A2", "Amanda")
# Escreve a idade 21 na célula B2  
sheetPadrao.write("B2", 21)  
# Escreve o nome "Allan" na célula A3
sheetPadrao.write("A3", "Allan")  
# Escreve a idade 28 na célula B3
sheetPadrao.write("B3", 28)  

# Fechando o arquivo para salvar as alterações
workbook.close()

# Abrindo o arquivo Excel gerado utilizando o aplicativo padrão do sistema operacional
os.startfile(nomeCaminhoArquivo)

