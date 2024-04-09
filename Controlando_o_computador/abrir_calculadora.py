import pyautogui as posicaoMouse

# Tempo de espera para o computador pensar
posicaoMouse.sleep(4)
# print(posicaoMouse.position())

# Mover o mouse
posicaoMouse.moveTo(x=3476, y=1324)
# Clicamos no botão Start ou seja no botão do Windows
posicaoMouse.click(x=3476, y=1324)

# Tempo de espera para o computador pensar
posicaoMouse.sleep(2)
# Digitando calculadora
posicaoMouse.typewrite('calculadora')

# posicaoMouse.sleep(4)
# print(posicaoMouse.position())
# Tempo de espera para o computador pensar
posicaoMouse.sleep(4)

# Mover o mouse
posicaoMouse.moveTo(x=3629, y=619)
# Clicamos no botão Start ou seja no botão da Calculadora
posicaoMouse.click(x=3629, y=619)