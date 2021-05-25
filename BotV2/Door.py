from Position import *


class Door:
    def __init__(self, direction: str, position: Position):
        self.direction = direction
        self.position = position

    @property
    def get_direction(self):
        return self.direction

    @property
    def get_door(self):
        return self.position

    @property
    def to_str(self):
        return self.direction + "\t-\t" + self.position.to_str