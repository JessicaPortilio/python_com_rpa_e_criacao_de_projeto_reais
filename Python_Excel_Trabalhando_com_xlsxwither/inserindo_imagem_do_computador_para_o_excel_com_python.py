# Importação das bibliotecas necessárias
# Importa a biblioteca xlsxwriter com um alias
import xlsxwriter as opcoesDoXlsxWriter  
# Importa a biblioteca os para operações de sistema
import os  

# Definição do nome do arquivo Excel
nomeCaminhoArquivo = 'ArquivoImagem.xlsx'
# Cria um objeto Workbook
workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)  

# Adiciona uma nova worksheet chamada "Dados"
sheetPadrao = workbook.add_worksheet("Dados")

# Adicionando dados na worksheet
sheetPadrao.write("B3", "Imagem do pinterest")  # Escreve o texto "Imagem do pinterest" na célula B3

# Insere uma imagem na célula B5
# Certifique-se de que a imagem 'tech.jpg' está no mesmo diretório que este script
sheetPadrao.insert_image('B5', 'tech.jpg')

# Fecha o arquivo para salvar as alterações
workbook.close()

# Abre o arquivo Excel gerado utilizando o aplicativo padrão do sistema operacional
os.startfile(nomeCaminhoArquivo)
