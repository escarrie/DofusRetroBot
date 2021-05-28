from Adding import *
from pyautogui import *
from Map import *
from Position import *
from Ressource import *
from Screen import *
from Door import *
import pyautogui
import random
import time
import keyboard
import random
import _thread
import json


def getPicture(screen: Screen):
    pic = pyautogui;screenshot(region=(screen.x_start, screen.y_start, screen.x_append, screen.y_append))
    return pic


def sleep(t):
    time.sleep(t)


def click(pos: Position):
    t = random.random()
    if t > 0.5:
        t -= 0.5
    if t < 0.2:
        t += 0.2
    pyautogui.moveTo(pos.x, pos.y)
    pyautogui.click()
    sleep(t)
