# Importa a biblioteca xlsxwriter com um alias
import xlsxwriter as opcoesDoXlsxWriter  
# Importa a biblioteca os para operações de sistema
import os 

# Define o nome do arquivo Excel a ser criado
nomeCaminhoArquivo = 'PintaFundoEFonte.xlsx'  
# Cria um objeto Workbook
minhaPlanilha = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)  
# Adiciona uma nova worksheet chamada "Dados"
sheetDados = minhaPlanilha.add_worksheet("Dados")  

# Mapeamento de cores em inglês
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

# Define a formatação para alterar a cor de fundo da célula
corFundo = minhaPlanilha.add_format({'fg_color': 'yellow'})  # Formato com fundo amarelo

# Define a formatação para alterar a cor da fonte
corFonte = minhaPlanilha.add_format()  # Cria um formato vazio
corFonte.set_font_color('pink')  # Define a cor da fonte como rosa

# Adicionando dados na worksheet com as formatações definidas
sheetDados.write("A1", "Nome", corFundo)  # Escreve "Nome" na célula A1 com fundo amarelo
sheetDados.write("B1", "Idade", corFundo)  # Escreve "Idade" na célula B1 com fundo amarelo
sheetDados.write("A2", "Amanda", corFonte)  # Escreve "Amanda" na célula A2 com fonte rosa
sheetDados.write("B2", 21, corFonte)  # Escreve 21 na célula B2 com fonte rosa
sheetDados.write("A3", "Allan", corFonte)  # Escreve "Allan" na célula A3 com fonte rosa
sheetDados.write("B3", 28, corFonte)  # Escreve 28 na célula B3 com fonte rosa

# Fechando o arquivo para salvar as alterações
minhaPlanilha.close()

# Abrindo o arquivo Excel gerado utilizando o aplicativo padrão do sistema operacional
os.startfile(nomeCaminhoArquivo)
