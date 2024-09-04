import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 1

pa.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")

#Inicio Login
pa.press('win')
pa.write("chrome")
pa.press('ENTER')
pa.write( "https://vitoria.dealernetworkflow.com.br/LoginAux.aspx?")
pa.press('ENTER')
time.sleep(5)
pa.click(x=968, y=516)
pyperclip.copy("LUCAS.OLIMPIO")
pa.hotkey('ctrl','v')


pa.click(x=987, y=565)
pyperclip.copy("Lucas.2024")
pa.hotkey('ctrl', 'v')
pa.click(x=1177, y=640)
pa.press('ENTER')

pa.click(x=256, y=135, duration=2)
pa.moveTo(x=253, y=314)
pa.moveTo(x=370, y=688)
pa.press('ENTER')
pa.click(x=1068, y=357)