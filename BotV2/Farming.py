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


def getPositionStarting():
    temp = [int(i) for i in input('Entrée votre position ( ex: "0.-24" ):\t').split('.')]
    temp = Position(temp[0], temp[1])
    return temp


def checkMapExist(maps, pos: Position):
    flag = False
    to_return = False
    for temp in maps:
        if temp.position.to_str == pos.to_str:
            flag = True
            to_return = temp
            break
    if flag:
        return to_return
    return to_return


def farming_process(maps):
    current_pos_player = getPositionStarting()
    os.system('cls' if os.name == 'nt' else 'clear')
    #CHECK MAP EXIST
    if checkMapExist(maps, current_pos_player):
        current_map = checkMapExist(maps, current_pos_player)
        current_map.print_str
    else:
        c = input("Map non trouver: {}\nVoulez vous lister toutes les maps? [O] Oui - [N] Non\t".format(current_pos_player.to_str)).upper()
        if c == 'O':
                if len(maps) % 2 == 0:
                    [print("[{}] {}\t-\t[{}] {}".format(i + 1, maps[i].position.to_str, i + 2, maps[i + 1].position.to_str)) for
                     i in range(0, len(maps), 2)]
                else:
                    [print("[{}] {}\t-\t[{}] {}".format(i + 1, maps[i].position.to_str, i + 2, maps[i + 1].position.to_str)) for
                     i in range(0, len(maps) - 1, 2)]
                    print("[{}] {}".format(len(maps), maps[len(maps) - 1].position.to_str))