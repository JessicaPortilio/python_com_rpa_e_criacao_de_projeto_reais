# Importa a biblioteca xlsxwriter com um alias
import xlsxwriter as opcoesDoXlsxWriter  
# Importa a biblioteca os para operações de sistema
import os 

# Define o nome do arquivo Excel
nomeCaminhoArquivo = 'FormatacaoCondicionalIcones.xlsx'
# Cria um novo workbook e uma nova planilha chamada "Dados"
planilhaExcel = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = planilhaExcel.add_worksheet("Dados")

# Dados de amostra a serem inseridos na planilha
inserirDados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 50, 12, 35],
    [59, 58, 76, 51],
    [43, 80, 34, 12],
    [91, 42, 73, 19],
    [18, 30, 45, 12],
]

# Adiciona um título na célula A1
sheetDados.write('A1', "Exemplos de formatação condicional com conjunto de ícones")

# Insere os dados de amostra a partir da linha 3 e coluna 2
for linha, range in enumerate(inserirDados):
    sheetDados.write_row(linha + 2, 1, range)

# Aplica formatação condicional com diferentes conjuntos de ícones nas linhas específicas
sheetDados.conditional_format('B4:E4', {
    'type': 'icon_set',
    'icon_style': '3_traffic_lights',
    'icons': [
        {'criteria': '>=', 'type': 'number', 'value': 50},  # Verde para valores >= 50
        {'criteria': '>=', 'type': 'number', 'value': 35},  # Amarelo para valores >= 35
        {'criteria': '<', 'type': 'number', 'value': 35}    # Vermelho para valores < 35
    ]
})

sheetDados.conditional_format('B5:E5', {
    'type': 'icon_set',
    'icon_style': '3_traffic_lights',
    'icons': [
        {'criteria': '>=', 'type': 'number', 'value': 50},
        {'criteria': '>=', 'type': 'number', 'value': 35},
        {'criteria': '<', 'type': 'number', 'value': 35}
    ],
    'reverse_icons': True
})

sheetDados.conditional_format('B6:E6', {
    'type': 'icon_set',
    'icon_style': '3_arrows',
    'icons': [
        {'criteria': '>=', 'type': 'number', 'value': 50},
        {'criteria': '>=', 'type': 'number', 'value': 35},
        {'criteria': '<', 'type': 'number', 'value': 35}
    ]
})

sheetDados.conditional_format('B7:E7', {
    'type': 'icon_set',
    'icon_style': '4_arrows',
    'icons': [
        {'criteria': '>=', 'type': 'number', 'value': 50},
        {'criteria': '>=', 'type': 'number', 'value': 35},
        {'criteria': '<', 'type': 'number', 'value': 35}
    ]
})

sheetDados.conditional_format('B8:E8', {
    'type': 'icon_set',
    'icon_style': '5_ratings',
    'icons': [
        {'criteria': '>=', 'type': 'number', 'value': 50},
        {'criteria': '>=', 'type': 'number', 'value': 35},
        {'criteria': '<', 'type': 'number', 'value': 35}
    ]
})

# Fecha o arquivo Excel para garantir que todos os dados sejam salvos
planilhaExcel.close()

# Abre o arquivo Excel gerado
os.startfile(nomeCaminhoArquivo)
