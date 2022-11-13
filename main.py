import random
import time
import pyautogui as pya

while True:
    X = random.randint(600,800)
    Y = random.randint(200,600)
    pya.moveTo(X,Y,0.6)
    time.sleep(2)