imboard = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', ' ', '*', '*', ' ', '*', ' ', '_', ' ', '*', ' ', '*', '*', ' ', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', ' ', '*', '*', ' ', '*', ' ', '_', ' ', '*', ' ', '*', '*', ' ', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
           ['*', ' ', '_', '_', '_', '_', '_', '*', '*', '*', '_', '_', '_', '_', '_', ' ', '*'],
           ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', ' ', '*', '*', ' ', '*', ' ', '_', ' ', '*', '*', ' ', '*', ' ', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', ' ', '*', '*', ' ', '*', ' ', '_', ' ', '*', '*', ' ', '*', ' ', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]


class Piece:
    def __init__(self, coords, color):
        self.y, self.x = coords
        self.color = color
        self.active = False

    def activate(self):
        self.active = True

    def move(self, tiles):
        if imboard[self.y][self.x]





players = {'b1': (11, 2), 'b2': (11, 5), 'b3': (14, 2), 'b4': (14, 5),
          'y1': (2, 2), 'y2': (2, 5), 'y3': (5, 2), 'y4': (5, 5),
          'g1': (2, 11), 'g2': (2, 14), 'g3': (5, 11), 'g4': (5, 14),
          'r1': (11, 11), 'r2': (11, 14), 'r3': (14, 11), 'r4': (11, 11)}