import pygame
from pygame import event
from math import floor
from random import randint
from playersandgame import *

colordict = {'y': (255, 222, 21), 'g': (4, 150, 69),
             'b': (18, 149, 231), 'r': (232, 21, 30)}


def getplayersdata(type=0):
    if type == 0:
        return list(map(lambda x: x.getpar(), players))
    elif type == 1:
        return {(i[0], i[1]): i[2] for i in list(map(lambda x: x.getpar(), players))}


def checkwincondition():
    allplayers = getplayersdata(type=1)
    if (8, 13) in allplayers and (8, 12) in allplayers and (8, 11) in allplayers and (8, 10) in allplayers:
        wintext = pygame.font.SysFont('Arial', 72).render('Синие победили!', True, 'Blue')
        while True:
            screen.fill((255, 255, 255))
            screen.blit(wintext, (300, 300))
        pass
    if (8, 6) in allplayers and (8, 5) in allplayers and (8, 4) in allplayers and (8, 3) in allplayers:
        wintext = pygame.font.SysFont('Arial', 72).render('Зеленые победили!', True, 'Blue')
        while True:
            screen.fill((255, 255, 255))
            screen.blit(wintext, (300, 300))
        pass
        # green win
    if (6, 8) in allplayers and (5, 8) in allplayers and (4, 8) in allplayers and (3, 8) in allplayers:
        wintext = pygame.font.SysFont('Arial', 72).render('Желтые победили!', True, 'Blue')
        while True:
            screen.fill((255, 255, 255))
            screen.blit(wintext, (300, 300))
        pass
    if (13, 8) in allplayers and (12, 8) in allplayers and (11, 8) in allplayers and (10, 8) in allplayers:
        wintext = pygame.font.SysFont('Arial', 72).render('Красные победили!', True, 'Blue')
        while True:
            screen.fill((255, 255, 255))
            screen.blit(wintext, (300, 300))
        pass


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
                          'b': (18, 149, 231), 'r': (232, 21, 30)}

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

    def on_click(self, cell_coords, movement):
        if (cell_coords[0] + 1, cell_coords[1] + 1) in list(map(lambda x: (x[0], x[1]), getplayersdata())):
            conplayer = 0
            for i in range(16):
                if (cell_coords[0] + 1, cell_coords[1] + 1) == players[i].getcoords():
                    conplayer = i
                    break
            if (order[whoseturn]
                    == players[conplayer].getcolor()):
                if movement == 6 and players[conplayer].getactstate() is False:
                    players[conplayer].activate()
                else:
                    actpl = players[conplayer]
                    for i in range(movement):
                        actpl.move()
                        self.render(screen)
                        pygame.display.flip()
                        pygame.time.delay(50)
                    if len(set(filter(lambda x: actpl.getcoords() == (x[0], x[1]),
                                      [i.getpar() for i in players]))) >= 2:
                        setofmultpieces = set(filter(lambda x:
                                                     actpl.getcoords() == x.getcoords(),
                                                     players))
                        for i in list(setofmultpieces):
                            if actpl.getpar() != i.getpar():
                                i.caught()

                return True
            return False

    def get_click(self, mouse_pos, movement):
        return self.on_click(self.get_cell(mouse_pos), movement)

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
        for i in getplayersdata():
            pygame.draw.circle(scr, 'black',
                               ((i[0] - 0.5) * self.cell_size + self.left, (i[1] - 0.5) * self.cell_size + self.top),
                               (self.cell_size) // 2, 1)
            pygame.draw.circle(scr, self.colordict[i[2]],
                               ((i[0] - 0.5) * self.cell_size + self.left, (i[1] - 0.5) * self.cell_size + self.top),
                               (self.cell_size - 1) // 2)


board = Board()
screen = pygame.display.set_mode((600, 600))
running = True
pygame.display.set_caption("Ludo")
rolling = True
dices = pygame.image.load('dice.png')
got_rolled = False
result = 0
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("snap.mp3")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and got_rolled is False:
                rolling = False
                got_rolled = True
                result = randint(1, 6)
                whoseturn = (whoseturn + 1) % 4
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE and got_rolled is True:
                rolling = True
                got_rolled = False
        if event.type == pygame.MOUSEBUTTONDOWN and got_rolled is True:
            is_correct = board.get_click(event.pos, result)
            if is_correct:
                rolling = True
                got_rolled = False
    screen.fill((255, 255, 255))
    board.render(screen)
    if rolling:
        result = randint(1, 6)
        screen.blit(dices, (275, 500), ((result - 1) * 54, 0, 54, 55))
    else:
        pygame.draw.rect(screen, colordict[order[whoseturn]], (0, 575, 600, 600))
        screen.blit(dices, (275, 500), ((result - 1) * 54, 0, 54, 55))
    text = pygame.font.SysFont('Corbel', 24).render("Сейчас ходит", True, 'black')
    screen.blit(text, (240, 575))
    pygame.display.flip()
    checkwincondition()
