import pyautogui
import cv2 as cv
import numpy as np
import keyboard

'''
LINK DO JOGO:
- https://mouseaccuracy.com/

AVISO:
- Caso ocorra algum problema, segure a tecla ESC,
ou então mova o mouse rapidamente para um dos cantos
da tela para finalizar o programa!
- Lembre-se de finalizar o bot após o jogo.
'''

# salvando informacoes do alvo
alvo = cv.imread('./imagens/alvo.png')
largura_alvo, comprimento_alvo = alvo.shape[:2]

# iniciando o looping principal
print('INICIANDO O BOT...\n')

while True:
    # verificando se a tecla ESC foi pressionada
    if keyboard.is_pressed('esc'):
        break

    # tirando print da tela
    print_tela = cv.cvtColor(np.array(pyautogui.screenshot()), cv.COLOR_RGB2BGR)

    # encontrando todos os alvos possiveis
    resultados_possiveis = cv.matchTemplate(print_tela, alvo, cv.TM_CCOEFF_NORMED)

    # filtrando os alvos
    threshold = 0.8
    resultados_filtrados = np.where(resultados_possiveis >= threshold)

    # agrupando todos os resultados duplicados
    retangulos = []
    for x, y in zip(resultados_filtrados[1], resultados_filtrados[0]):
        retangulos.append([int(x), int(y), comprimento_alvo, largura_alvo])
    retangulos, _ = cv.groupRectangles(retangulos, 1, 0.5)

    # clicando em todos os alvos detectados
    for x, y, comprimento, largura in retangulos:
        print(f'Alvo Encontrado! -> ({x}, {y})')
        centro_x = x + (comprimento//2)
        centro_y = y + (largura//2)
        pyautogui.click(centro_x, centro_y)
        
print('\nFINALIZANDO O BOT...')
