from Adding import *
from pyautogui import *
from Map import *
from Position import *
from Ressource import *
from Door import *
import pyautogui
import time
import keyboard
import random
import _thread
import json

g_stopped = False


def init():
    f = open("maps.json", "r")
    s = json.load(f)
    f.close()
    return s


def starting():
    return input("Voulez vous farmer ou ajouter des ressources?\n[1] - Farmer\n[2] - Ajouter des ressources\n1 ou 2: ")


def verif_stop():
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
            break
        if g_stopped:
            break


def save_maps(maps):
    t_maps  = {}
    # CREATION ACTUAL MAP
    for c_map in maps:
        t_map       = {"porte": {"disponible": []}, "ressources": []}
        # CREATION ACTUAL DOORS
        for c_door in c_map.doors:
            t_map["porte"]["disponible"].append(c_door.direction)
            t_map["porte"][c_door.direction] = [c_door.position.x, c_door.position.y]
        # CREATION ACTUAL RESOURCES
        t_res_d = ["Nombre de ressources", 0]
        t_map["ressources"].append(t_res_d)
        i = 0
        for c_res in c_map.ressources:
            i += 1
            t_map["ressources"].append([c_res.name, c_res.position.x, c_res.position.y, [c_res.r, c_res.g, c_res.b]])
        # SAVE MAP INTO MAPS
        t_map["ressources"][0][1] = i
        t_maps[c_map.position.to_str] = t_map
    f = open("maps.json", "w")
    f.write(json.dumps(t_maps, indent=4))
    f.close()


def main(g_stopped):
    maps = init()
    temp = []
    for mapi in maps:
        ressource = []
        doors = []
        pos = Position.to_int(mapi)
        for this in maps[mapi]['ressources'][1:]:
            ressource.append(Ressource(this[0], Position(this[1], this[2]), this[3]))
        doors_dispo = maps[mapi]['porte']['disponible']
        for this in doors_dispo:
            doors.append(Door(this, Position(maps[mapi]['porte'][this][0], maps[mapi]['porte'][this][1])))
        temp.append(Map(Position(pos[0], pos[1]), ressource, doors))
    maps = temp
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        s = starting()
        if s == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---- AJOUT DE RESSOURCES ----")
            maps = add_process(maps)
            save_maps(maps)
        elif s == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---- FARMING ----")
        os.system('cls' if os.name == 'nt' else 'clear')
        if input("Quitter le programme? [O] Oui - [N] Non\t").upper() == 'O':
            g_stopped = True
            break


_thread.start_new_thread(main, (g_stopped,))
verif_stop()
