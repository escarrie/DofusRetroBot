from Ressource import *
from Position import *
from Door import *


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

    @property
    def print_str(self):
        print("-------- MAP: {} --------".format(self.position.to_str))
        print("\n", self.position.to_str, "Porte:")
        [print(d.to_str) for d in self.doors]
        print("\n", self.position.to_str, "Ressources: {}".format(len(self.ressources)))
        [print(r.to_str) for r in self.ressources]
        print('\n\n\n')