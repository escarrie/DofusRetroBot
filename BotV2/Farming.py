from Adding import *
from pyautogui import *
from Map import *
from Position import *
from Ressource import *
from Door import *
import pyautogui
import random
import time
import keyboard
import random
import _thread
import json


def click(pos: Position):
    t = random.random()
    if t > 0.5:
        t -= 0.5
    if t < 0.2:
        t += 0.2
    pyautogui.moveTo(pos.x, pos.y)
    pyautogui.click()
    sleep(t)
