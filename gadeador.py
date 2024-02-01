import pyautogui
import time
link= 'www.instagram.com/jandersoncunegundes/'
pyautogui.PAUSE= 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(10)
pyautogui.click(x=511, y=470)
time.sleep(1.5)
pyautogui.click(x=827, y=679)
time.sleep(1)
pyautogui.write('Oi lindo amei tuas fotos!, te vi no tinder. adoraria te conhecer <3')
pyautogui.press('enter')
