import pyautogui as posicaoAbrirEdge

# Tempo de espera para o computador pensar
posicaoAbrirEdge.sleep(4)
# Pegando a posição do mouse
# print(posicaoAbrirEdge.position())

# Mover o mouse
posicaoAbrirEdge.moveTo(x=3476, y=1324)
# Clicamos no botão Start ou seja no botão do Windows
posicaoAbrirEdge.click(x=3476, y=1324)

# Tempo de espera para o computador pensar
posicaoAbrirEdge.sleep(2)
# Digitando Edge
posicaoAbrirEdge.typewrite('Edge')

# Tempo de espera para o computador pensar
posicaoAbrirEdge.sleep(3)
# Pegando a posição do mouse
# print(posicaoAbrirEdge.position())

# # # # Mover o mouse
posicaoAbrirEdge.moveTo(x=3680, y=610)
# # # # Clicamos duas vezes no botãoo do navegador Edge
posicaoAbrirEdge.doubleClick(x=3680, y=610)

# Tempo de espera para o computador pensar
posicaoAbrirEdge.sleep(3)
# Pegando a posição do mouse
# print(posicaoAbrirEdge.position())


# Movendo o mouse para barra de pesquisa
posicaoAbrirEdge.moveTo(x=444, y=217)
# Clicando duas vezes na barra de pesquisa
posicaoAbrirEdge.doubleClick(x=444, y=217)

# Digitando a url de pesquisa do google
posicaoAbrirEdge.typewrite('https://www.google.com/')

#Tempo de espera para o computador pensar
posicaoAbrirEdge.sleep(3)

#Apertamos a tecla enter
posicaoAbrirEdge.press('enter')

#Tempo de espera para o computador pensar
posicaoAbrirEdge.sleep(3)
# Pegando a posição do mouse
# print(posicaoAbrirEdge.position())

# Movimentando o mouse para o google
posicaoAbrirEdge.moveTo(x=302, y=561)
# Clicando duas vezes no link do google
posicaoAbrirEdge.doubleClick(x=302, y=561)

#Tempo de espera para o computador pensar
posicaoAbrirEdge.sleep(3)
# Digitando o que desejamos pesquisar
posicaoAbrirEdge.typewrite('Dolar hoje')

#Apertamos a tecla enter
posicaoAbrirEdge.press('enter')
