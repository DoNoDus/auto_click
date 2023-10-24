import pyautogui
import time



def mouse_position():
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)

# orders = {'Nut': [[1403 ,22],[1775 ,457], [1680 ,457], [1376 ,327], [1488 ,453], [1757 ,370]],
#          'Note': [[1390 ,535],[1785 ,971],[1675, 983],[1381 ,845], [1491, 964],[1752, 888]]}

# def auto_click(lis):
#     for i in lis:
#         pyautogui.moveTo(i[0] , i[1]) 
#         pyautogui.sleep(1)
#         pyautogui.click(i[0] , i[1]) 
#         pyautogui.sleep(1)

# pyautogui.moveTo(orders['Note'][0][0] , orders['Note'][0][1]) 
# pyautogui.sleep(1)
# pyautogui.moveTo(orders['Note'][5][0] , orders['Note'][5][1]) 
# pyautogui.sleep(1)
# pyautogui.click(orders['Note'][5][0] , orders['Note'][5][1]) 
# pyautogui.sleep(1)
# pyautogui.moveTo(orders['Nut'][0][0] , orders['Nut'][0][1]) 
# pyautogui.sleep(1)
# pyautogui.moveTo(orders['Nut'][5][0] , orders['Nut'][5][1]) 
# pyautogui.sleep(1)
# pyautogui.click(orders['Nut'][5][0] , orders['Nut'][5][1]) 
# pyautogui.sleep(1)
# start_time = time.time()

# while True :
#     timer = int(time.time() - start_time)
#     print('Time running'+' ' , timer)
#     pyautogui.sleep(1)

#     if type(timer/141) == type(int()):
#         auto_click(orders['Nut'])
#         auto_click(orders['Note'])

# pyautogui.hotkey('alt', 'tab')
# pyautogui.sleep(1)
# pyautogui.click(1069 , 1061) 
# pyautogui.sleep(1)
# pyautogui.click(1012 , 972) 
# pyautogui.sleep(1)
# pyautogui.click(1069 , 1061) 
# pyautogui.sleep(1)
# pyautogui.click(1180 , 957) 
# pyautogui.sleep(1)
# pyautogui.click(1632, 917) 

# pyautogui.click(1632, 917) 
# pyautogui.sleep(1)

while True :

    # mouse_position()
    # pyautogui.sleep(1)
    pyautogui.moveTo(1546 , 765) 
    pyautogui.doubleClick() 
    pyautogui.sleep(1)
    pyautogui.moveTo(1500 , 137) 
    pyautogui.doubleClick()
    pyautogui.sleep(1)

