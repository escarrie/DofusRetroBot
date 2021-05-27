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
        if mapi:
            for this in maps:
                if this.position.to_str == mapi:
                    while True:
                        find = True
                        delete = False
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
                            d = input("Voulez vous suppprimer une porte [P], une ressource [R] ou la map [M]?\t").upper()
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
                            elif d == 'M':
                                temp = []
                                for t_map in maps:
                                    if t_map.position.to_str != this.position.to_str:
                                        temp.append(t_map)
                                maps = temp
                                if len(maps) % 2 == 0:
                                    [print("[{}] {}\t-\t[{}] {}".format(i + 1, maps[i].position.to_str, i + 2, maps[i + 1].position.to_str)) for i in range(0, len(maps), 2)]
                                else:
                                    [print("[{}] {}\t-\t[{}] {}".format(i + 1, maps[i].position.to_str, i + 2, maps[i + 1].position.to_str)) for i in range(0, len(maps) - 1, 2)]
                                    print("[{}] {}".format(len(maps), maps[len(maps) - 1].position.to_str))
                                for i in range(10):
                                    sys.stdout.write("\rContinue dans {} seconde(s) ".format(10 - i))
                                    time.sleep(1)
                                sys.stdout.write("\rContinue dans 0 seconde(s) ")
                                time.sleep(1)
                                delete = True
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if delete or input("Continuer sur cette carte [{}]?\n[O] Oui - [N] Non\t".format(this.position.to_str)).upper() != 'O':
                            break
            if not find:
                c = input("---- Map non trouver ----\nVoulez vous l'ajouter [A] ou Lister les maps [L]\t").upper()
                if c == 'L':
                    print("Liste des maps:")
                    if len(maps) % 2 == 0:
                        [print("[{}] {}\t-\t[{}] {}".format(i + 1, maps[i].position.to_str, i + 2, maps[i + 1].position.to_str)) for i in range(0, len(maps), 2)]
                    else:
                        [print("[{}] {}\t-\t[{}] {}".format(i + 1, maps[i].position.to_str, i + 2, maps[i + 1].position.to_str)) for i in range(0, len(maps) - 1, 2)]
                        print("[{}] {}".format(len(maps), maps[len(maps) - 1].position.to_str))
                    p = input("Voulez vous ajouter '{}' ? [O] Oui - [N] Non\t".format(mapi)).upper()
                    if p == 'O':
                        c = 'A'
                    else:
                        c = ''
                if c == 'A':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Création d'une carte:\n[1] Saisir la position\n[2] Ajouts des portes\n[3] Ajouts des ressources")
                    print("La position actuel est: [{}]".format(mapi))
                    c = input("Voulez vous continuer avec cette position? [O] Oui - [N] Non\t").upper()
                    if c == 'N':
                        break
                    pos = [int(i) for i in mapi.split('.')]
                    pos = Position(pos[0], pos[1])
                    print("Position = [{}]".format(pos.to_str))
                    flag_process = True
                    # PORTES
                    doors = []
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        dir, pos_p = 0, 0
                        try:
                            dir, pos_p = input("Direction et coordonnées de la porte? ex: droite/gauche/haut/bas xxx.xxx\t").split()
                        except:
                            print("Vous devevez rentrer des information")
                        # VERIFY
                        if dir and pos_p:
                            if not (dir == 'droite' or dir == 'gauche' or dir == 'haut' or dir == 'bas'):
                                print("Erreur lors de la direction - Arrêts du process")
                                flag_process = False
                                break
                            pos_p = [int(i) for i in pos_p.split('.')]
                            pos_p = Position(pos_p[0], pos_p[1])
                            os.system('cls' if os.name == 'nt' else 'clear')
                            door = Door(dir, pos_p)
                            t_flag = True
                            for t_door in doors:
                                if t_door.direction == door.direction:
                                    t_flag = False
                                    break
                            if t_flag:
                                doors.append(door)
                            else:
                                print("Erreur la porte existe déjà - Arrêt process")
                                break
                            [print(temp.to_str) for temp in doors]
                        if input("Continuer d'ajouter des portes? [O] Oui - [N] Non\t").upper() == 'N':
                            break
                    # RESSOURCES
                    ressources = []
                    while True and flag_process:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        t_res = []
                        try:
                            t_res = input("Ajout d'une ressource!\nex: Frene 1500.200 255.255.255\n").split()
                        except:
                            print("Vous devevez rentrer des information")
                        if t_res:
                            x, y = (int(i) for i in t_res[1].split('.'))
                            rgb = (int(i) for i in t_res[2].split('.'))
                            t_rgb = []
                            [t_rgb.append(i) for i in rgb]
                            t_pos = Position(x, y)
                            t_res = Ressource(t_res[0], t_pos, t_rgb)
                            ressources.append(t_res)
                            [print(i.to_str) for i in ressources]
                        if input("Continuer d'ajouter des ressources? [O] Oui - [N] Non\t").upper() == 'N':
                            break
                    if not doors and ressources:
                        flag_process = False
                    if flag_process:
                        maps.append(Map(pos, ressources, doors))
                    for i in range(10):
                        sys.stdout.write("\rContinue dans {} seconde(s) ".format(10 - i))
                        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        var = [t.print_str for t in maps]
        var = '0'
        int(var)
        if input("Aller vers le changement de mode? [O] Oui - [N] Non\t").upper() == 'O':
            break