import pyautogui
import time

def action():
    pyautogui.hotkey('ctrlleft', 'v')
    pyautogui.hotkey('ctrlleft', 'enter')

times = int(input('How many times?: '))

time.sleep(5)

if times == 0:
    while True:
        action()
elif times > 0:
    for i in range(times):
        action()
    
