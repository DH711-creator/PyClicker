from pyautogui import typewrite


try:    
    import pyautogui
    import time
    import random


    mincps = int(input("Enter Minimum CPS: ")) / 1000
    maxcps = int(input("Enter Maximum CPS: ")) / 1000

    for i in range(1,70):
        time.sleep(random.randint(mincps, maxcps))
        pyautogui.leftClick
        i = i+1
except TypeError:
    print('bad')