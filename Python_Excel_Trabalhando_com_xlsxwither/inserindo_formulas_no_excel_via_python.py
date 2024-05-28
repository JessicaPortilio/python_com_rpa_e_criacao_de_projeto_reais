# Importação das bibliotecas necessárias

# Importa a biblioteca xlsxwriter com um alias
import xlsxwriter as opcoesDoXlsxWriter  
# Importa a biblioteca os para operações de sistema
import os  

# Definição do nome do arquivo Excel
nomeCaminhoArquivo = 'Formulas.xlsx'
# Cria um objeto Workbook
minhaPlanilha = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo) 
# Adiciona uma nova worksheet chamada "Dados"
sheetDados = minhaPlanilha.add_worksheet("Dados")

# Adicionando títulos nas colunas
sheetDados.write("A1", "Número 1")  # Título da coluna A
sheetDados.write("B1", "Número 2")  # Título da coluna B
sheetDados.write("C1", "Fórmula")  # Título da coluna C

# Adicionando valores na coluna A
sheetDados.write("A2", 10)
sheetDados.write("A3", 6)
sheetDados.write("A4", 8)
sheetDados.write("A5", 6)
sheetDados.write("A8", "Ana")

# Adicionando valores na coluna B
sheetDados.write("B2", 7)
sheetDados.write("B3", 5)
sheetDados.write("B4", 3)
sheetDados.write("B5", 1)
sheetDados.write("B8", "Paula")

# Adicionando fórmulas na coluna C
sheetDados.write_formula("C2", "=A2+B2")  # Soma os valores das células A2 e B2
sheetDados.write_formula("C3", "=A3-B3")  # Subtrai o valor da célula B3 do valor da célula A3
sheetDados.write_formula("C4", "=A4*B4")  # Multiplica os valores das células A4 e B4
sheetDados.write_formula("C5", "=A5/B5")  # Divide o valor da célula A5 pelo valor da célula B5
sheetDados.write_formula("C8", '=CONCATENATE(A8," ",B8)')  # Concatena os valores das células A8 e B8 com um espaço entre eles

# Ajusta a largura das colunas de A a C para 15 caracteres
sheetDados.set_column('A:C', 15)

# Fecha o arquivo para salvar as alterações
minhaPlanilha.close()

# Abre o arquivo Excel gerado utilizando o aplicativo padrão do sistema operacional
os.startfile(nomeCaminhoArquivo)
