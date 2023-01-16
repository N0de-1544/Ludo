import pygame
from pygame import event
from math import floor
import playersandgame


def getplayers():
    return list(map(lambda x: x.getpiecestate(), playersandgame.players))




class Board:
    def __init__(self):
        self.width = 15
        self.height = 15
        self.board = [['1y', '1y', '1y', '1y', '1y', '1y', '', '', '', '1g', '1g', '1g', '1g', '1g', '1g'],
                      ['1y', '', '1y', '1y', '', '1y', '', 'hg', 'sg', '1g', '', '1g', '1g', '', '1g'],
                      ['1y', '1y', '1y', '1y', '1y', '1y', '', 'hg', '', '1g', '1g', '1g', '1g', '1g', '1g'],
                      ['1y', '1y', '1y', '1y', '1y', '1y', '', 'hg', '', '1g', '1g', '1g', '1g', '1g', '1g'],
                      ['1y', '', '1y', '1y', '', '1y', '', 'hg', '', '1g', '', '1g', '1g', '', '1g'],
                      ['1y', '1y', '1y', '1y', '1y', '1y', '', 'hg', '', '1g', '1g', '1g', '1g', '1g', '1g'],
                      ['', 'sy', '', '', '', '', '', 'u', '', '', '', '', '', '', ''],
                      ['', 'hy', 'hy', 'hy', 'hy', 'hy', 'u', 'u', 'u', 'hr', 'hr', 'hr', 'hr', 'hr', ''],
                      ['', '', '', '', '', '', '', 'u', '', '', '', '', '', 'sr', ''],
                      ['1b', '1b', '1b', '1b', '1b', '1b', '', 'hb', '', '1r', '1r', '1r', '1r', '1r', '1r'],
                      ['1b', '', '1b', '1b', '', '1b', '', 'hb', '', '1r', '', '1r', '1r', '', '1r'],
                      ['1b', '1b', '1b', '1b', '1b', '1b', '', 'hb', '', '1r', '1r', '1r', '1r', '1r', '1r'],
                      ['1b', '1b', '1b', '1b', '1b', '1b', '', 'hb', '', '1r', '1r', '1r', '1r', '1r', '1r'],
                      ['1b', '', '1b', '1b', '', '1b', 'sb', 'hb', '', '1r', '', '1r', '1r', '', '1r'],
                      ['1b', '1b', '1b', '1b', '1b', '1b', '', '', '', '1r', '1r', '1r', '1r', '1r', '1r']]
        self.left = 75
        self.top = 25
        self.cell_size = 30
        self.colordict = {'y': (255, 222, 21), 'g': (4, 150, 69),
                          'b':  (18, 149, 231), 'r': (232, 21, 30)}


    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        if ((mouse_pos[0] - self.left) / self.cell_size < self.width
                and (mouse_pos[1] - self.top) / self.cell_size < self.height):
            return floor((mouse_pos[0] - self.left) / self.cell_size), floor((mouse_pos[1] - self.top) / self.cell_size)
        else:
            return None

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def render(self, scr):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(scr, 'black', (self.left + (j * self.cell_size),
                                 self.top + (i * self.cell_size),
                                 self.cell_size,
                                 self.cell_size), 1)
                pygame.draw.rect(scr, 'white',
                                 (self.left + (j * self.cell_size) + 1,
                                  self.top + (i * self.cell_size) + 1,
                                  (self.cell_size - 2),
                                  (self.cell_size - 2)))
                if self.board[i][j] != '':
                    if self.board[i][j][0] == '1':
                        pygame.draw.rect(scr, self.colordict[self.board[i][j][1]],
                                         (self.left + (j * self.cell_size),
                                                        self.top + (i * self.cell_size),
                                                        self.cell_size,
                                                        self.cell_size))
                    elif self.board[i][j][0] == 'h':
                        pygame.draw.rect(scr, self.colordict[self.board[i][j][1]],
                                         (self.left + (j * self.cell_size) + 1,
                                          self.top + (i * self.cell_size) + 1,
                                          (self.cell_size - 2),
                                          (self.cell_size - 2)))
                    elif self.board[i][j][0] == 's':
                        pygame.draw.rect(scr, self.colordict[self.board[i][j][1]],
                                         (self.left + (j * self.cell_size) + 1,
                                          self.top + (i * self.cell_size) + 1,
                                          (self.cell_size - 2),
                                          (self.cell_size - 2)))
                    elif self.board[i][j] == 'u':
                        pygame.draw.rect(scr, 'white', (self.left + (j * self.cell_size),
                                                        self.top + (i * self.cell_size),
                                                        self.cell_size,
                                                        self.cell_size))
        for par in getplayers():
            pygame.draw.circle(scr, self.colordict[par[2]],
                               (((par[0] - 0.5) * self.cell_size) + self.left,
                                ((par[1] - 0.5) * self.cell_size) + self.top),
                               (self.cell_size - 1) // 2)




if __name__ == '__main__':
    board = Board()
    screen = pygame.display.set_mode((600, 600))
    running = True
    fps = 50
    v = 10
    clock = pygame.time.Clock()
    pygame.display.set_caption("Ludo")
    rolling = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(board.get_click(event.pos))
                rolling = False
        if rolling:
            pass
        screen.fill((255, 255, 255))
        board.render(screen)
        pygame.display.flip()
