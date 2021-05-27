from Position import *


class Ressource:
    def __init__(self, name, position: Position, rgb):
        self.name = name
        self.position = position
        self.rgb = rgb

    @property
    def get_rgb(self):
        return self.rgb

    @property
    def r(self):
        return self.rgb[0]

    @property
    def g(self):
        return self.rgb[1]

    @property
    def b(self):
        return self.rgb[2]

    @property
    def get_position(self):
        return self.position

    @property
    def to_str(self):
        return self.name + "\t-\t" + self.position.to_str + '\t' + 'RGB: {},{},{}'.format(self.rgb[0], self.rgb[1], self.rgb[2])