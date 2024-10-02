import pyautogui
import time
import os
import sys

pyautogui.FAILSAFE = True

def resource_path(relative_path):
    """Obtém o caminho absoluto do arquivo, seja no script ou no executável."""
    try:
        base_path = sys._MEIPASS 
    except AttributeError:
        base_path = os.path.abspath(".") 

    return os.path.join(base_path, relative_path)

def wait_for_image(image_path, confidence=0.8, timeout=1000):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                return location
        except pyautogui.ImageNotFoundException:
            print(f"Imagem '{image_path}' não encontrada. Aguardando...")
            time.sleep(2)

    raise TimeoutError(f"Imagem '{image_path}' não encontrada após {timeout} segundos.")

def main():
    try:
        btn_location = wait_for_image(resource_path('aceitar-btn.png'))
        pyautogui.click(btn_location)
        print("Partida aceita!")
    except TimeoutError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    while True:
        main()
