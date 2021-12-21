import pyautogui, time
time.sleep(2)
pyautogui.moveTo('Icons and Pictures\Start Menu.png', duration=0.6)
pyautogui.click()
#pyautogui.press('winleft')
pyautogui.write('paint', interval=0.2)
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(1.5)
#pyautogui.moveTo('MS Paint.png', duration=0.8)
#pyautogui.click()
pyautogui.moveTo('Icons and Pictures\Brushes.png', duration=0.5)
pyautogui.click()
distance = 300
change = 20
pyautogui.moveTo(683, 384, duration=0.5)
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.25)
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.25)
    pyautogui.drag(-distance, 0, duration=0.25)
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.25)
try:
    pyautogui.moveTo('Icons and Pictures\edgeicon_dark.png', duration=0.4)
    pyautogui.click()
except TypeError:
    pyautogui.moveTo('Icons and Pictures\Start Menu.png', duration=0.6)
    pyautogui.click()
    pyautogui.write('edge', interval=0.2)
    pyautogui.press('enter')
time.sleep(3)
try:
    pyautogui.moveTo('Icons and Pictures\Youtube.png', duration=0.4)
except TypeError:
    pyautogui.moveTo("Icons and Pictures\\New Tab.png", duration=0.4)
    pyautogui.click()
    time.sleep(1.2)
    pyautogui.moveTo('Icons and Pictures\Youtube.png', duration=0.4)
pyautogui.click()

time.sleep(2.5)
try:
    pyautogui.moveTo('Icons and Pictures\Youtube_search.png', duration=0.4)
except TypeError:
    pyautogui.moveTo('Icons and Pictures\Youtube_search_light.png', duration=0.4)
pyautogui.click()
pyautogui.write('Never Gonna Give You Up', interval=0.15)
pyautogui.press('enter')
time.sleep(2.2)
pyautogui.moveTo('Icons and Pictures\Rick.png', duration=0.8)
pyautogui.click()