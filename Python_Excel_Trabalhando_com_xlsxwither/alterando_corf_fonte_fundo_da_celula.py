import xlsxwriter as opcoesDoXlsxWriter  # Importa a biblioteca xlsxwriter com um alias
import os  # Importa a biblioteca os para operações de sistema

nomeCaminhoArquivo = 'PintaFundoEFonteExemplo.xlsx'  # Define o nome do arquivo Excel a ser criado
minhaPlanilha = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)  # Cria um objeto Workbook

sheetDados = minhaPlanilha.add_worksheet("Dados")  # Adiciona uma nova worksheet chamada "Dados"

# Mapeamento de cores em inglês para referência
# Preto = black
# Branco = white
# Amarelo = yellow
# Laranja = orange
# Vermelho = red
# Azul = blue
# Verde = green
# Cinza = gray
# Rosa = pink
# Roxo = purple
# Marinho = navy
# Prata = silver

# Define a formatação para alterar a cor da fonte
corFonte = minhaPlanilha.add_format()  # Cria um formato vazio
corFonte.set_font_color('blue')  # Define a cor da fonte como azul

# Define a formatação para alterar tanto a cor da fonte quanto a cor de fundo, centralizando o texto e colocando em negrito
corFonteFundo = minhaPlanilha.add_format({'align': 'center',  # Centraliza o texto
                                          'font_color': 'white',  # Define a cor da fonte como branca
                                          'bold': True,  # Define a fonte como negrito
                                          'bg_color': 'gray'})  # Define a cor de fundo como cinza

# Adicionando dados na worksheet com as formatações definidas
sheetDados.write("A1", "Nome", corFonteFundo)  # Escreve "Nome" na célula A1 com a formatação de fundo cinza e fonte branca centralizada
sheetDados.write("B1", "Idade", corFonteFundo)  # Escreve "Idade" na célula B1 com a mesma formatação
sheetDados.write("A2", "Amanda", corFonte)  # Escreve "Amanda" na célula A2 com fonte azul
sheetDados.write("B2", 21, corFonte)  # Escreve 21 na célula B2 com fonte azul
sheetDados.write("A3", "Allan", corFonte)  # Escreve "Allan" na célula A3 com fonte azul
sheetDados.write("B3", 28, corFonte)  # Escreve 28 na célula B3 com fonte azul

# Fechando o arquivo para salvar as alterações
minhaPlanilha.close()

# Abrindo o arquivo Excel gerado utilizando o aplicativo padrão do sistema operacional
os.startfile(nomeCaminhoArquivo)
