import pyautogui as escolha_opcao
# https://docs.python.org/pt-br/3/library/tkinter.html
# Importação da Biblioteca tkinter
# É uma biblioteca Python usada para criar interface gráficas de usuários (GUI)
import tkinter as tk

# Essa função é chamada quando o botão é clicado na janela de diálogo.
# Ela interrompe o programa usando root.quit() (o root é a janela principal)
# e imprime no console a opção selecionada
def escolher_opcao(opcao):
    if opcao == 'Sair':
        root.quit()
    if opcao == "Excel":
        
        #O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
        #Nesse caso é a mesma coisa que precionar Windows + R
        escolha_opcao.hotkey('win', 'r')
        
        #Tempo de espera para o computador pensar
        escolha_opcao.sleep(2)
        
        #Digitamos a palavra Excel
        escolha_opcao.typewrite('Excel')
        
        #Tempo de espera para o computador pensar
        escolha_opcao.sleep(2)
        
        #Precionamos a tecla Enter
        escolha_opcao.press('Enter')
        
        #Tempo de espera para o computador pensar
        escolha_opcao.sleep(4)
        
        #print(escolha_opcao.position())
        
        #Mover o mouse
        escolha_opcao.moveTo(x=2982, y=259, duration=0.5)
        
        #CLiquei na opção para abrir um excel em branco
        escolha_opcao.click(x=2982, y=259, duration=0.5)
        
        #Tempo de espera para o computador pensar
        escolha_opcao.sleep(3)
        
        # Digitando
        escolha_opcao.typewrite('Opcao desejada foi: Excel')
        
        #print(escolha_opcao.position())
    elif opcao == "Word":
        #O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
        #Nesse caso é a mesma coisa que precionar Windows + R
        escolha_opcao.hotkey('win', 'r')
        
        #Tempo de espera para o computador pensar
        escolha_opcao.sleep(5)
        
        #Digitamos a palavra Excel
        escolha_opcao.typewrite('winword')
        
        #Tempo de espera para o computador pensar
        escolha_opcao.sleep(2)
        
        #Precionamos a tecla Enter
        escolha_opcao.press('Enter')
        
        #Tempo de espera para o computador pensar
        escolha_opcao.sleep(4)
        
        #print(escolha_opcao.position())
        
        #Mover o mouse
        escolha_opcao.moveTo(x=2982, y=259, duration=0.5)
        
        # CLiquei na opção para abrir um excel em branco
        escolha_opcao.click(x=2982, y=259, duration=0.5)
        
        # Tempo de espera para o computador pensar
        escolha_opcao.sleep(3)
        
        # Digitando
        escolha_opcao.typewrite('Opcao desejada foi: Word')
    elif opcao == "Notepad":
        # Abrir o Executar do Windows (pressionar Win + R)
        escolha_opcao.hotkey('win', 'r')

        # Aguardar um momento para o Executar abrir
        escolha_opcao.sleep(2)

        # Digitar 'notepad' no Executar para abrir o Bloco de Notas
        escolha_opcao.typewrite('notepad')

        # Aguardar um momento para o Bloco de Notas abrir
        escolha_opcao.sleep(2)

        # Pressionar Enter para confirmar e abrir o Bloco de Notas
        escolha_opcao.press('enter')

        # Aguardar um momento para o Bloco de Notas carregar
        escolha_opcao.sleep(3)

        # Digitar texto dentro do Bloco de Notas
        escolha_opcao.typewrite('Abrimos o Notepad com um robô ou Script')

        # Aguardar um momento para o texto ser digitado
        escolha_opcao.sleep(4)

        # Mover o cursor do mouse para uma posição específica dentro do Bloco de Notas
        escolha_opcao.moveTo(x=1060, y=102)

        # Clicar no Bloco de Notas para ativar a janela e exibir o texto digitado
        escolha_opcao.click(x=1060, y=102)

        # Aguardar um momento para o Bloco de Notas responder
        escolha_opcao.sleep(5)

        # Mover o cursor do mouse para outra posição dentro do Bloco de Notas
        escolha_opcao.moveTo(x=1855, y=102)

        # Clicar novamente no Bloco de Notas para garantir que ele esteja ativo
        escolha_opcao.click(x=1060, y=102)

        # Aguardar um momento para o Bloco de Notas responder
        escolha_opcao.sleep(2)

        # Fechar o Bloco de Notas (pressionar Ctrl + W)
        escolha_opcao.hotkey('ctrl', 'w')

        # Pressionar a tecla TAB para selecionar a próxima opção
        escolha_opcao.press('tab')

        # Aguardar um momento para o sistema processar
        escolha_opcao.sleep(2)

        # Pressionar Enter para confirmar a seleção
        escolha_opcao.press('enter')
        
        #print(escolha_opcao.position())
# Está função é usada para criar botões na janela de diálogo.
# Ela recebe como argumento o root(a janela onde o botão será criado), o texto
# a ser exibido no botão, a cor de fundo do botão e a opção associada a esse botão
def criar_botao(root, text, color, opcao):
    button = tk.Button(root, text=text, bg=color, fg='white', width=10,
                       command=lambda: escolher_opcao(opcao))
    button.pack(side=tk.LEFT, pady=5, padx=5)

# Função para criar o botão "Sair"
def criar_botao_sair(root):
    button = tk.Button(root, text='Sair', bg='gray', fg='white', width=10,
                       command=lambda: escolher_opcao('Sair'))
    button.pack(side=tk.LEFT, padx=5, pady=5)

# Definindo as cores dos botões
# As cores para os botões Excel, Word e Notepad são definidas aqui.
# Essas cores serão usadas para diferenciar visualmente os botões na janela de diálogo.
excel_color = "#4CAF50"  # verde
word_color = "#2196F3"   # azul
notepad_color = "#FF5722"  # laranja

# Criar a janela principal e escondendo-a
# A função tk.Tk() cria uma janela principal, que será usada como o 
# container para todos os elementos da interface gráfica. O método root.withdraw() esconde
# essa janela principal, já que não precisamos mostrá-la diretamente ao usuário.
root = tk.Tk()
root.withdraw() # Esconder a janela principal

# Crie uma nova janela de diálogo personalizada
# Usando o tk.Toplevel(root) para criar uma nova janela de diálogo.
# Está será a janela onde os botôes serão exibidos para que o usuário possa escolher uma opção.
dialog = tk.Toplevel(root)
# Usamos dialog.title() para difinir o título da janela de diálogo
dialog.title('Escolha uma opção')
# E dialog.geometry() para definir suas dimensões como 300X150 pixels
dialog.geometry('400x150') 

# Adicionando botões personalizados com cores específicas
# a função criar_botao() três vezes para adicionar os botões do Excel,
# Word e Noteppad na janela de diálogo. Cada botão é associado à função
# escolher_opcao(opcao) com a opção correspondente
criar_botao(dialog, 'Excel', excel_color, 'Excel')
criar_botao(dialog, 'Word', word_color, 'Word')
criar_botao(dialog, 'Notepad', notepad_color, 'Notepad')

criar_botao_sair(dialog)

# Mantendo a janela aberta
# para iniciar o loop principal da interface gráfica. 
# Isso mantém a janela de diálogo aberta e permite que o usuário interaja
# com ele até que feche a janela
root.mainloop()

