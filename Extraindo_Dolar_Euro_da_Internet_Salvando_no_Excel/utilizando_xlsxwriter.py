import xlsxwriter
import os

nomeCaminhoArquivo = 'C:\\Valor_do_Dolar_e_Euro\\Dolar e Euro Google.xlsx'

planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)

planilha1 = planilhaCriada.add_worksheet()

planilha1.write('A1', 'Nome')
planilha1.write('B1', 'Idade')
planilha1.write('A2', 'Jessica')
planilha1.write('B2', '30')
planilha1.write('A3', 'Paulo')
planilha1.write('B3', '52')

planilhaCriada.close()

os.startfile(nomeCaminhoArquivo)