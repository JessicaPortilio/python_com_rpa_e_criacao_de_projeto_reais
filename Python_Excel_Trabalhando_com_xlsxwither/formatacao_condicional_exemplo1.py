# Importação das bibliotecas necessárias
# Importa a biblioteca xlsxwriter com um alias
import xlsxwriter as opcoesDoXlsxWriter  
# Importa a biblioteca os para operações de sistema
import os  

# Definição do nome do arquivo Excel
nomeCaminhoArquivo = 'FormatacaoCondicional.xlsx'
planilhaExcel = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)  # Cria um objeto Workbook

# Adiciona uma nova worksheet chamada "Dados"
sheetDados = planilhaExcel.add_worksheet("Dados")

# Adiciona um formato de preenchimento verde com o texto em branco
formatoMaior = planilhaExcel.add_format({'bg_color': 'green',
                                        'font_color': 'white'})

# Adiciona um formato de preenchimento vermelho com o texto em branco
formatoMenor = planilhaExcel.add_format({'bg_color': 'red',
                                        'font_color': 'white'})

# Coloca alguns dados de amostra para executar a formatação condicional
inserirDados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 50, 12, 34],
    [59, 58, 76, 51],
    [43, 80, 34, 12],
    [91, 58, 73, 19],
]

# Adiciona uma descrição para a formatação condicional
sheetDados.write('A1', "Células com valores >= 50 estão em verde e < 50 estão em vermelho")

# Escreve os dados na planilha, começando da linha 3 e coluna 2
for linha, range in enumerate(inserirDados):
    sheetDados.write_row(linha + 2, 1, range)

# Adiciona formatação condicional para células com valores >= 50
sheetDados.conditional_format('B4:E7', {'type': 'cell',
                                       'criteria': '>=',
                                       'value': 50,
                                       'format': formatoMaior})

# Adiciona formatação condicional para células com valores < 50
sheetDados.conditional_format('B4:E7', {'type': 'cell',
                                       'criteria': '<',
                                       'value': 50,
                                       'format': formatoMenor})

# Fecha o arquivo para salvar as alterações
planilhaExcel.close()

# Abre o arquivo Excel gerado utilizando o aplicativo padrão do sistema operacional
os.startfile(nomeCaminhoArquivo)
