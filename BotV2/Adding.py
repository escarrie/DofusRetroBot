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
import os


def add_process(maps):
    while True:
        mapi = input("Quel map voulez vous ajouter / modifier?\nex: 2.-23 ")
        find = False
        for this in maps:
            if this.position.to_str == mapi:
                while True:
                    find = True
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("---- MAP: {} ----".format(mapi))
                    # DOORS
                    print("\nPortes: ")
                    [print("[{}] - {}".format(i + 1, this.doors[i].to_str)) for i in range(len(this.doors))]
                    print("\nRessources:")
                    [print("[{}] - {}".format(i + 1, this.ressources[i].to_str)) for i in range(len(this.ressources))]
                    c = input("\nQue voulez vous faire?\n[A] Ajouter\n[M] Modifier\n[D] Supprimer\nex: A\t").upper()
                    if c == 'A':
                        a = input("voulez vous ajouter une porte [P] ou une ressource [R]?\t").upper()
                        if a == 'P':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Liste des portes:")
                            [print("[{}] - {}".format(i + 1, this.doors[i].to_str)) for i in range(len(this.doors))]
                            dir = int(input("\n\nQuel direction?\n[1] Haut\n[2] Bas\n[3] Gauche\n[4] Droite\n1 ou .. 4\t"))
                            flag = True
                            if dir == 1:
                                dir = "haut"
                            elif dir == 2:
                                dir = "bas"
                            elif dir == 3:
                                dir = "gauche"
                            elif dir == 4:
                                dir = "droite"
                            else:
                                flag = False
                            if flag:
                                pos = input("Quel est la position? [1684 180]\t").split()
                                pos = Position(pos[0], pos[1])
                                door = Door(dir, pos)
                                this.doors.append(door)
                                [print("[{}] - {}".format(i + 1, this.doors[i].to_str)) for i in range(len(this.doors))]
                        elif a == 'R':
                            print("Ressource")
                            [print("[{}] - {}".format(i + 1, this.ressources[i].to_str)) for i in range(len(this.ressources))]
                    elif c == 'M':
                        print('MODIFIER')
                        m = input("Voulez vous modifier une porte [P] ou une ressource [R]?\t").upper()
                        if m == 'P':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Portes:")
                            [print("[{}] - {}".format(i + 1, this.doors[i].to_str)) for i in range(len(this.doors))]
                            dir = int(input("\nQuel porte voulez vous modifier? 1 .. {}\t".format(len(this.doors))))
                            if dir in range(1, len(this.doors) + 1):
                                print("Modification de la porte: ", this.doors[dir - 1].to_str)
                                door_t = input("Quel modification? [haut/bas/gauche/droite 1000 10]\t").split()
                                this.doors[dir - 1].position = Position(int(door_t[1]), int(door_t[2]))
                                this.doors[dir - 1].direction = door_t[0]
                                [print("[{}] - {}".format(i + 1, this.doors[i].to_str)) for i in range(len(this.doors))]
                            else:
                                print("Porte non trouver")
                        elif m == 'R':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Ressources:")
                            [print("[{}] - {}".format(i + 1, this.ressources[i].to_str)) for i in range(len(this.ressources))]
                            res = int(input("Quel ressources voulez vous modifier? 1 .. {}\t".format(len(this.ressources))))
                            if res in range(1, len(this.ressources) + 1):
                                print("Modification de la ressource: ", this.ressources[res - 1].to_str)
                                res_t = input("Que voulez vous modifier? [name x.y r.g.b]\t").split()
                                r, g, b = [int(i) for i in res_t[2].split('.')]
                                pos_t = [int(i) for i in res_t[1].split('.')]
                                pos_t = Position(pos_t[0], pos_t[1])
                                temp = Ressource(res_t[0], pos_t, [r, g, b])
                                this.ressources[res] = temp
                                [print("[{}] - {}".format(i + 1, this.ressources[i].to_str)) for i in range(len(this.ressources))]
                            else:
                                print("Ressource non trouver")
                    elif c == 'D':
                        d = input("Voulez vous supppimer une porte [P] ou une ressource [R]?\t").upper()
                        if d == 'P':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("SUPPRESSION D'UNE PORTES")
                            print("\nPortes: ")
                            [print("[{}] - {}".format(i + 1, this.doors[i].to_str)) for i in range(len(this.doors))]
                            d = input("Quel portes choissisiez vous?\t")
                            temp = []
                            for i in range(len(this.doors)):
                                if i + 1 != int(d):
                                    temp.append(this.doors[i])
                            this.doors = temp
                            [print("[{}] - {}".format(i + 1, this.doors[i].to_str)) for i in range(len(this.doors))]
                        elif d == 'R':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("SUPPRESSION D'UNE RESSOURCES")
                            print("\nRessources:")
                            [print("[{}] - {}".format(i + 1, this.ressources[i].to_str)) for i in range(len(this.ressources))]
                            d = input("Quel ressources choissisiez vous?\t")
                            temp = []
                            for i in range(len(this.ressources)):
                                if i + 1 != int(d):
                                    temp.append(this.ressources[i])
                            this.ressources = temp
                            [print("[{}] - {}".format(i + 1, this.ressources[i].to_str)) for i in range(len(this.ressources))]
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if input("Continuer sur cette carte [{}]?\n[O] Oui - [N] Non\t".format(this.position.to_str)).upper() != 'O':
                        break
        if not find:
            print('-- NOT FIND --') # DOING
        os.system('cls' if os.name == 'nt' else 'clear')
        if input("Aller vers le changement de mode? [O] Oui - [N] Non\t").upper() == 'O':
            break