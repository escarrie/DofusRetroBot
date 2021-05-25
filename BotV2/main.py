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


def init():
    return json.load(open("data.json"))


def starting():
    return input("Voulez vous farmer ou ajouter des ressources?\n[1] - Farmer\n[2] - Ajouter des ressources\n1 ou 2: ")


def verif_stop():
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
            break


def main(void):
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
            add_process(maps)
        elif s == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---- FARMING ----")
        os.system('cls' if os.name == 'nt' else 'clear')
        if input("Quitter le programme? [O] Oui - [N] Non\t") == 'O':
            break


_thread.start_new_thread(main, ('',))
verif_stop()
