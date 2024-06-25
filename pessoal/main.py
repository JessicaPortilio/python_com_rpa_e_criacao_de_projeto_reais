import pyautogui
import time
import keyboard

# time.sleep(4)
# print(pyautogui.position())

def image_game():
    while True:
        #pyautogui.moveTo(x=425, y=526)
        pyautogui.doubleClick(x=425, y=526)


keyboard.add_hotkey('i', image_game)

print(f"Pressione 'i' para inicializar a busca pelas imagens ou pressione 's' para sair.")

while True:
    if keyboard.is_pressed('s'):
        print('Saindo...')
        break
    time.sleep(0.1)
