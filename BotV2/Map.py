from Ressource import *
from Position import *
from Door import *
import random


class Map:
    def __init__(self, position: Position, ressources: [], doors: []):
        self.position = position
        self.ressources = ressources
        self.doors = doors

    @property
    def get_position(self):
        return self.position

    @property
    def get_ressources(self):
        return self.ressources

    @property
    def get_doors(self):
        return self.doors

    @property
    def add_ressources(self, ressource: Ressource):
        self.ressources.append(ressource)

    @property
    def add_door(self, door: Door):
        self.doors.append(door)

    @classmethod
    def get_random_door(cls, come_from, doors):
        if len(doors) == 1:
            return doors[0]
        elif len(doors) == 0:
            return 0
        else:
            while True:
                flag = True
                i = random.randint(0, len(doors) - 1)
                door_return = doors[i]
                # bas - haut
                if door_return.direction == 'bas' and come_from == 'haut':
                    flag = False
                # haut - bas
                if door_return.direction == 'haut' and come_from == 'bas':
                    flag = False
                # droite - gauche
                if door_return.direction == 'droite' and come_from == 'gauche':
                    flag = False
                # gauche - droite
                if door_return.direction == 'gauche' and come_from == 'droite':
                    flag = False
                if flag:
                    return door_return

    @property
    def print_str(self):
        print("-------- MAP: {} --------".format(self.position.to_str))
        print("\n", self.position.to_str, "Porte:")
        [print(d.to_str) for d in self.doors]
        print("\n", self.position.to_str, "Ressources: {}".format(len(self.ressources)))
        [print(r.to_str) for r in self.ressources]
        print('\n\n\n')