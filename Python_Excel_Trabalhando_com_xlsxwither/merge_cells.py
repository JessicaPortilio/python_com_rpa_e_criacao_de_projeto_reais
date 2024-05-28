# Importa a biblioteca xlsxwriter com um alias
import xlsxwriter as opcoesDoXlsxWriter  
# Importa a biblioteca os para operações de sistema
import os  

# Definição do nome do arquivo Excel
nomeCaminhoArquivo = 'MergeCells.xlsx'
# Cria um objeto Workbook
workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)  

# Adiciona uma nova worksheet padrão
sheetPadrao = workbook.add_worksheet()

# Define a formatação para células mescladas
add_merge_celulas = workbook.add_format({
    'bold': True,  # Define a fonte como negrito
    'border': 6,  # Define a borda das células com espessura 6
    'align': 'center',  # Centraliza o texto horizontalmente
    'valign': 'vcenter',  # Centraliza o texto verticalmente
    'size': 30,  # Define o tamanho da fonte como 30
    'fg_color': 'blue',  # Define a cor de fundo como azul
    'font_color': 'white',  # Define a cor da fonte como branca
})

# Mescla células de B3 a I5 e adiciona o texto "Aula de Merge Células" com a formatação definida
sheetPadrao.merge_range('B3:I5', 'Aula de Merge Células', add_merge_celulas)

# Fecha o arquivo para salvar as alterações
workbook.close()

# Abre o arquivo Excel gerado utilizando o aplicativo padrão do sistema operacional
os.startfile(nomeCaminhoArquivo)
