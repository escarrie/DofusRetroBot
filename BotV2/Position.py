class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def get_x(self):
        return int(self.x)

    @property
    def get_y(self):
        return int(self.y)

    @property
    def right(self):
        self.x += 1

    @property
    def left(self):
        self.x -= 1

    @property
    def up(self):
        self.y -= 1

    @property
    def down(self):
        self.y += 1

    @property
    def to_str(self):
        return str(self.x) + '.' + str(self.y)

    @classmethod
    def to_int(cls, s):
        return [int(i) for i in s.split('.')]