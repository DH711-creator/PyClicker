import pyautogui
import pynput
import time
import random


try:
    def runclicker():

        mincps = 0.0
        maxcps = 0.0

        def askcps():
            global mincps, maxcps, amount
            mincps = (1000 / float(input("Enter minimum CPS: ")))*0.001
            maxcps = (1000 / float(input("Enter maximum CPS: ")))*0.001
            #Converting CPS into MS delay
            amount = int(input("How many times would you like to click? "))

        askcps()

        for i in range(1, amount):
            delay = random.uniform(mincps, maxcps)
            time.sleep(delay)
            pyautogui.click()
            i = i+1
    runclicker()
except TypeError:
    print("Please enter an integer or float value for CPS, and an integer value for amount.")
    runclicker()
