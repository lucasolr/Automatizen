import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 1

pa.press('win')
pa.write("chrome")
pa.press('ENTER')
pa.write( "https://vitoria.dealernetworkflow.com.br/LoginAux.aspx?")
pa.press('ENTER')
time.sleep(3)
pa.click(x=968, y=516)
pyperclip.copy("LUCAS.OLIMPIO")
pa.hotkey('ctrl','v')


pa.click(x=987, y=565)
pyperclip.copy("Lucas.2024")
pa.hotkey('ctrl', 'v')
pa.click(x=1177, y=640)
pa.press('ENTER')

