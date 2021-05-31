from threading import Thread
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
import winsound
import _thread
import os


def getPicture(screen: Screen):
    pic = pyautogui.screenshot(region=(screen.x_start, screen.y_start, screen.x_append, screen.y_append))
    return pic


def sleep(t):
    time.sleep(t)


def click(pos: Position):
    t = random.random()
    if t > 0.5:
        t -= 0.5
    if t < 0.2:
        t += 0.2
    pyautogui.moveTo(pos.get_x, pos.get_y)
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


def verifPods(screen: Screen):
    pic = getPicture(screen)
    r, g, b = pic.getpixel((screen.x_pods - screen.x_start, screen.y_pods - screen.y_start))
    if not (r in range(75, 85) or g in range(70, 80) or b in range(55, 65)):
        # VERIF LEVEL
        pic = getPicture(screen)
        r, g, b = pic.getpixel((screen.x_level - screen.x_start, screen.y_level - screen.y_start))
        if r == 255 and g == 97 and b == 0:
            pyautogui.press('enter')
            print("****************************")
            print("\tLEVELUP")
            print("****************************")
        else:
            print("********************************")
            print("\tINVENTAIRE PLEIN")
            print("********************************")
            frequency = 500  # Set Frequency To 1500 Hertz
            duration = 500  # Set Duration To 1000 ms == 1 second
            for i in range(1, 5):
                winsound.Beep(frequency, duration)
                sleep(random.random())
            os._exit(1)


def checkChangeMap(screen: Screen):
    pic = getPicture(screen)
    br, bg, bb = pic.getpixel((screen.x_center, screen.y_center))
    while True and not keyboard.is_pressed('right'):
        pic = getPicture(screen)
        nr, ng, nb = pic.getpixel((screen.x_center, screen.y_center))
        if br != nr or bg != ng or bb != nb:
            break
    br = bg = bb = 0
    print('Chargement de map en cours')
    while True and not keyboard.is_pressed('right'):
        pic = getPicture(screen)
        nr, ng, nb = pic.getpixel((screen.x_center, screen.y_center))
        if br != nr or bg != ng or bb != nb:
            break
    print('Chargement de map fini')


def rechargeMap(current_map: Map, maps):
    for c_map in maps:
        if c_map.position.to_str == current_map.position.to_str:
            current_map = c_map
            break
    return current_map


def checkRessourceCollected(res: Ressource, screen: Screen):
    while True and not keyboard.is_pressed('right'):
        if not checkRessources(res, screen):
            break


def checkRessources(res: Ressource, screen: Screen):
    pic = getPicture(screen)
    r, g, b = pic.getpixel(((res.position.x - screen.x_start), (res.position.y - screen.y_start)))
    if not (r in range(res.r - 2, res.r + 2) and g in range(res.g - 2, res.g + 2) and b in range(res.b - 2, res.b + 2)):
        return True
    else:
        return False


def collectRessrouces(current_map: Map, screen: Screen):
    i = 0
    while i < len(current_map.ressources):
        if checkRessources(current_map.ressources[i], screen):
            # COLLECT
            click(current_map.ressources[i].position)
            secPosition = Position(current_map.ressources[i].position.x + 50, current_map.ressources[i].position.y + 60)
            click(secPosition)
            # CHECK COLLECTED
            checkRessourceCollected(current_map.ressources[i], screen)
            # CHECK PODS
            verifPods(screen)
            i = 0
        i += 1


def changeMap(current_map: Map, come_from, screen: Screen):
    # GET DOOR
    t_door = current_map.get_random_door(come_from, current_map.doors)
    # CLICK ON DOOR
    click(t_door.position)
    # CHECK MAP CHANGE
    checkChangeMap(screen)
    # NEW POS
    new_pos = Position(current_map.position.x, current_map.position.y)
    if t_door.direction == 'haut':
        new_pos.up
    elif t_door.direction == 'bas':
        new_pos.down
    elif t_door.direction == 'droite':
        new_pos.right
    elif t_door.direction == 'gauche':
        new_pos.left
    return t_door.direction, new_pos


def collectMaps(current_map: Map, screen: Screen):
    collectRessrouces(current_map, screen)


def farming_process(maps):
    current_pos_player = getPositionStarting()
    screen = Screen([0, 364], [1917, 1817], [1022, 1544], [1006,  993])
    os.system('cls' if os.name == 'nt' else 'clear')
    #CHECK MAP EXIST
    if checkMapExist(maps, current_pos_player):
        current_map = checkMapExist(maps, current_pos_player)
        current_map.print_str
        # FARMING
        come_from = 'none'
        while True:
            verifPods(screen)
            collectMaps(current_map, screen)
            come_from, new_pos = changeMap(current_map, come_from, screen)
            # FIND NEW MAP
            m_temp = checkMapExist(maps, new_pos)
            if not m_temp:
                print("La map n'existe pas")
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                m_temp.print_str
                current_map = m_temp
    else:
        c = input("Map non trouver: {}\nVoulez vous lister toutes les maps? [O] Oui - [N] Non\t".format(current_pos_player.to_str)).upper()
        if c == 'O':
                if len(maps) % 2 == 0:
                    [print("[{}] {}\t-\t[{}] {}".format(i + 1, maps[i].position.to_str, i + 2, maps[i + 1].position.to_str)) for i in range(0, len(maps), 2)]
                else:
                    [print("[{}] {}\t-\t[{}] {}".format(i + 1, maps[i].position.to_str, i + 2, maps[i + 1].position.to_str)) for
                     i in range(0, len(maps) - 1, 2)]
                    print("[{}] {}".format(len(maps), maps[len(maps) - 1].position.to_str))