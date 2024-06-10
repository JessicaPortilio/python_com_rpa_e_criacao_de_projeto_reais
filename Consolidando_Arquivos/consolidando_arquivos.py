import pandas as pd  # Importa a biblioteca pandas e a renomeia como pd, que é usada para manipulação de dados
import os  # Importa a biblioteca os, que fornece funções para interagir com o sistema operacional

# Caminho onde estão os arquivos de Excel
caminhoArquivos = r"C:\\python_com_rpa_e_criacao_de_projeto_reais\\Excel"

# Obtém uma lista com todos os nomes de arquivos no diretório especificado
listaArquivos = os.listdir(caminhoArquivos)

# Imprime a lista de arquivos encontrados no diretório
print(listaArquivos)

# Cria uma lista contendo o caminho completo para cada arquivo Excel (.xlsx) encontrado
listaCaminhoEArquivoExcel = [os.path.join(caminhoArquivos, arquivo) for arquivo in listaArquivos if arquivo.endswith('.xlsx')]

# Imprime separadores e a lista de caminhos completos dos arquivos Excel
print("----- #### -------- ###### ---------")
print("----- #### -------- ###### ---------")
print(listaCaminhoEArquivoExcel)

# Cria uma lista para armazenar os DataFrames (estruturas de dados do pandas) de cada arquivo Excel
listaDataFrames = []

# Para cada arquivo Excel na lista de caminhos completos:
for arquivo in listaCaminhoEArquivoExcel:
    # Lê os dados do arquivo Excel e os armazena em um DataFrame
    dados = pd.read_excel(arquivo)
    # Adiciona o DataFrame à lista de DataFrames
    listaDataFrames.append(dados)

# Concatena todos os DataFrames da lista em um único DataFrame, ignorando os índices antigos e criando novos índices sequenciais
dadosArquivo = pd.concat(listaDataFrames, ignore_index=True)

# Salva o DataFrame consolidado em um novo arquivo Excel, sem incluir os índices na planilha
dadosArquivo.to_excel(r"C:\\python_com_rpa_e_criacao_de_projeto_reais\\Arquivo Consolidado.xlsx", index=False)
