import pyautogui as posicaoAbreArquivos

# Aguardar alguns segundos para dar tempo ao computador de processar
posicaoAbreArquivos.sleep(4)

# Abrir o Executar do Windows (pressionar Win + R)
posicaoAbreArquivos.hotkey('win', 'r')

# Aguardar um momento para o Executar abrir
posicaoAbreArquivos.sleep(2)

# Digitar 'notepad' no Executar para abrir o Bloco de Notas
posicaoAbreArquivos.typewrite('notepad')

# Aguardar um momento para o Bloco de Notas abrir
posicaoAbreArquivos.sleep(2)

# Pressionar Enter para confirmar e abrir o Bloco de Notas
posicaoAbreArquivos.press('enter')

# Aguardar um momento para o Bloco de Notas carregar
posicaoAbreArquivos.sleep(3)

# Digitar texto dentro do Bloco de Notas
posicaoAbreArquivos.typewrite('Abrimos o Notepad com um robô ou Script')

# Aguardar um momento para o texto ser digitado
posicaoAbreArquivos.sleep(4)

# Mover o cursor do mouse para uma posição específica dentro do Bloco de Notas
posicaoAbreArquivos.moveTo(x=1060, y=102)

# Clicar no Bloco de Notas para ativar a janela e exibir o texto digitado
posicaoAbreArquivos.click(x=1060, y=102)

# Aguardar um momento para o Bloco de Notas responder
posicaoAbreArquivos.sleep(5)

# Mover o cursor do mouse para outra posição dentro do Bloco de Notas
posicaoAbreArquivos.moveTo(x=1855, y=102)

# Clicar novamente no Bloco de Notas para garantir que ele esteja ativo
posicaoAbreArquivos.click(x=1060, y=102)

# Aguardar um momento para o Bloco de Notas responder
posicaoAbreArquivos.sleep(2)

# Fechar o Bloco de Notas (pressionar Ctrl + W)
posicaoAbreArquivos.hotkey('ctrl', 'w')

# Pressionar a tecla TAB para selecionar a próxima opção
posicaoAbreArquivos.press('tab')

# Aguardar um momento para o sistema processar
posicaoAbreArquivos.sleep(2)

# Pressionar Enter para confirmar a seleção
posicaoAbreArquivos.press('enter')
