# Importa a biblioteca xlsxwriter com um alias
import xlsxwriter as opcoesDoXlsxWriter  
# Importa a biblioteca os para operações de sistema
import os  

# Define o nome do arquivo Excel
nomeCaminhoArquivo = 'Grafico.xlsx'

# Cria um novo workbook e uma nova planilha chamada "Resumo"
planilhaExcel = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = planilhaExcel.add_worksheet("Resumo")

# Define o formato de célula com negrito
linhaNegrito = planilhaExcel.add_format({'bold': 1})

# Define os títulos e dados a serem inseridos na planilha
titulos = ['Vendedores', 'Total Vendas']
dadosTabela = [
    ["Ana", "Pedro", "Allan", "Francisco", "Rosa", "Amanda"],
    [400, 300, 89, 34, 350, 120],
]

# Insere os títulos na primeira linha (linha 1)
sheetDados.write_row('A1', titulos, linhaNegrito)
# Insere os nomes dos vendedores na coluna A, começando na linha 2
sheetDados.write_column('A2', dadosTabela[0])
# Insere os valores de vendas na coluna B, começando na linha 2
sheetDados.write_column('B2', dadosTabela[1])

# Cria um gráfico de colunas
graficoColunas = planilhaExcel.add_chart({'type': 'column'})

# Configura as séries do gráfico com categorias e valores
graficoColunas.add_series({
    'name': '=Resumo!$B$1',  # Nome da série é o título "Total Vendas"
    'categories': '=Resumo!$A$2:$A$7',  # Categorias são os nomes dos vendedores
    'values': '=Resumo!$B$2:$B$7',  # Valores são os totais de vendas
})

# Adiciona um título ao gráfico e define os rótulos dos eixos X e Y
graficoColunas.set_title({'name': 'Gráfico total de vendas'})
graficoColunas.set_x_axis({'name': 'Vendedores'})
graficoColunas.set_y_axis({'name': 'Vendas'})

# Define um estilo de gráfico do Excel
graficoColunas.set_style(11)

# Insere o gráfico na planilha na posição D2 com deslocamento
sheetDados.insert_chart('D2', graficoColunas, {'x_offset': 25, 'y_offset': 10})

# Fecha o arquivo Excel para garantir que todos os dados sejam salvos
planilhaExcel.close()

# Abre o arquivo Excel gerado
os.startfile(nomeCaminhoArquivo)
