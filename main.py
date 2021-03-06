import pygame
from enum import Enum
from pygame.locals import *
import algos
import sys
from time import time

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Labyrint')
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (42, 30, 35)
BROWNLIGHT = (93, 84, 88)
maps = []
W = 20
H = 20
MARGIN = 24
FPS = 60
font = "Visitor TT1 BRK"
WALL = pygame.image.load('assets/wall.png')
MARIO = pygame.image.load('assets/mario.png')
SIGN = pygame.image.load('assets/nazov.png')
UP = pygame.image.load('assets/up.png')
DOWN = pygame.image.load('assets/down.png')
LVL1 = pygame.image.load('assets/level1.png')
LVL2 = pygame.image.load('assets/level2.png')
LVL3 = pygame.image.load('assets/level3.png')
LVL4 = pygame.image.load('assets/level4.png')
LVL5 = pygame.image.load('assets/level5.png')
QUIT = pygame.image.load('assets/quit.png')
X = pygame.image.load('assets/x.png')
CONGRATS = pygame.image.load('assets/congratulation.png')
DFS_BTN = pygame.image.load('assets/dfs.png')
BFS_BTN = pygame.image.load('assets/bfs.png')
GR_BTN = pygame.image.load('assets/greedy.png')
ASTAR_BTN = pygame.image.load('assets/a.png')
BACK = pygame.image.load('assets/back.png')
END = pygame.image.load('assets/end.png')
steps = 0


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.SysFont(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


def move_down(x, y, steps):
    # if dir == pygame.K_DOWN:
    if maps[x + 1][y] == '0' or maps[x + 1][y] == '3' or maps[x + 1][y] == '5':
        if maps[x + 1][y] == '3':
            x, y = move_mario(x, y, pygame.K_DOWN)
            win_game(steps)
        x, y = move_mario(x, y, pygame.K_DOWN)

    mario_moving_in_game(steps)


def move_up(x, y, steps):
    if maps[x - 1][y] == '0' or maps[x - 1][y] == '3' or maps[x - 1][y] == '5':
        if maps[x - 1][y] == '3':
            x, y = move_mario(x, y, pygame.K_UP)
            win_game(steps)
        x, y = move_mario(x, y, pygame.K_UP)

    mario_moving_in_game(steps)


def move_left(x, y, steps):
    if maps[x][y - 1] == '0' or maps[x][y - 1] == '3' or maps[x][y - 1] == '5':
        if maps[x][y - 1] == '3':
            x, y = move_mario(x, y, pygame.K_LEFT)
            win_game(steps)
        x, y = move_mario(x, y, pygame.K_LEFT)

    mario_moving_in_game(steps)


def move_right(x, y, steps):
    if maps[x][y + 1] == '0' or maps[x][y + 1] == '3' or maps[x][y + 1] == '5':
        if maps[x][y + 1] == '3':
            x, y = move_mario(x, y, pygame.K_RIGHT)
            win_game(steps)
        x, y = move_mario(x, y, pygame.K_RIGHT)

    mario_moving_in_game(steps)


def mario_moving_in_game(steps):
    # steps = 0

    for row in range(len(maps)):  # ze pocet rows
        for col in range(len(maps[0])):  # pocet cols
            if maps[row][col] == '2':
                mario_is_on_x = row
                mario_is_on_y = col
                break

    run = True
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                steps += 1
                if event.key == pygame.K_DOWN:
                    move_down(mario_is_on_x, mario_is_on_y, steps)

                if event.key == pygame.K_UP:
                    move_up(mario_is_on_x, mario_is_on_y, steps)

                if event.key == pygame.K_LEFT:
                    move_left(mario_is_on_x, mario_is_on_y, steps)

                if event.key == pygame.K_RIGHT:
                    move_right(mario_is_on_x, mario_is_on_y, steps)
        new_map()
        pygame.display.update()  # ked je o riadok hore break, mapu vypise do cons dobru, uz len refresh obrazovky, skoci to na riadok 141


def move_mario(x, y, direct):
    maps[x][y] = '5'

    if direct == pygame.K_UP:
        x -= 1
    elif direct == pygame.K_DOWN:
        x += 1
    elif direct == pygame.K_LEFT:
        y -= 1
    elif direct == pygame.K_RIGHT:
        y += 1
    else:
        print("oh nou")

    maps[x][y] = '2'
    return x, y


def win_game(steps):
    screen.fill(WHITE)
    run = True
    pressed = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ohandlovanie X - zatvori okno
                run = False
        print('winn on ', steps, 'steps')
        win_text = text_format("CONGRATULATION", font, 70, WHITE)
        win_rect = win_text.get_rect()
        steps_text2 = text_format(str(steps) + ' steps', font, 70, BROWN)
        steps_text = text_format(str(steps) + ' steps', font, 70, BROWNLIGHT)
        steps_rect = steps_text.get_rect()
        # screen.blit(win_text, (WIDTH / 2 - (win_rect[2] / 2), 80))
        screen.blit(CONGRATS, (WIDTH / 2 - 216, 30))
        screen.blit(steps_text, (WIDTH / 2 - (steps_rect[2] / 2), 160))
        screen.blit(steps_text2, ((WIDTH / 2 - (steps_rect[2] / 2) - 4), 155))
        pygame.display.flip()
        pygame.time.delay(7000)
        quit()


def new_map():
    screen.fill(WHITE)
    for row in range(len(maps)):  # ze pocet rows
        for col in range(len(maps[0])):  # pocet cols
            if maps[row][col] == '2':
                screen.blit(MARIO, (col * MARGIN + 70, row * MARGIN))
                continue
            if maps[row][col] == '0' or maps[row][col] == '3':
                continue
            if maps[row][col] == '5':
                screen.blit(X, (col * MARGIN + 70, row * MARGIN))
                continue
            screen.blit(WALL, (col * MARGIN + 70, row * MARGIN))

    screen.blit(DFS_BTN, (WIDTH / 5, HEIGHT / 2 + 120))
    screen.blit(BFS_BTN, (WIDTH / 5, HEIGHT - 80))
    screen.blit(GR_BTN, (WIDTH / 2, HEIGHT / 2 + 120))
    screen.blit(ASTAR_BTN, (WIDTH / 2, HEIGHT - 80))
    screen.blit(BACK, (0, 0))
    screen.blit(END, (WIDTH - 60, 0))

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # ohandlovanie X - zatvori okno
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= mouse[0] <= 59 and 0 <= mouse[1] <= 42:
                main()
            if WIDTH - 60 <= mouse[0] <= WIDTH and 0 <= mouse[1] <= 42:
                quit()
            elif WIDTH / 5 <= mouse[0] <= WIDTH / 5 + 100 and HEIGHT / 2 + 120 <= mouse[1] <= HEIGHT / 2 + 163:
                destination, starting_position = find_dest2()
                t0=time()
                res = algos.dfs(maps, destination, starting_position)
                t1=time()
                if res!= -1:
                    print("DFS Steps back = ", res)
                    print("Time elapsed = ", round(t1-t0,4), "seconds")
                    print()
                else:
                    print("DFS Path not found!")
                    print("Time elapsed = ", t1 - t0, "seconds")
                    print()
            elif WIDTH / 5 <= mouse[0] <= WIDTH / 5 + 100 and HEIGHT - 80 <= mouse[1] <= HEIGHT - 37:
                destination, starting_position = find_dest2()
                t0 = time()
                res1 = algos.bfs(maps, destination, starting_position)
                t1 = time()
                if res1 != -1:
                    print("BFS Steps back = ", res1)
                    print("Time elapsed = ", round(t1-t0,4), "seconds")
                    print()
                else:
                    print("BFS Path not found!")
                    print("Time elapsed = ", t1 - t0, "seconds")
                    print()
            elif WIDTH / 2 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT / 2 + 120 <= mouse[1] <= HEIGHT / 2 + 163:
                destination, starting_position = find_dest2()
                t0 = time()
                res2 = algos.greedybfs(maps, destination, starting_position)
                t1 = time()
                if res2 != -1:
                    print("GREEDY Steps back = ", res2)
                    print("Time elapsed = ", round(t1-t0,4), "seconds")
                    print()
                else:
                    print("GREEDY Path not found!")
                    print("Time elapsed = ", t1 - t0, "seconds")
                    print()
            elif WIDTH / 2 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT - 80 <= mouse[1] <= HEIGHT - 37:
                destination, starting_position = find_dest2()
                t0 = time()
                res3 = algos.A_Star(maps, destination, starting_position)
                t1 = time()
                if res3 != -1:
                    print("A* Steps back = ", res3)
                    print("Time elapsed = ", round(t1-t0,4), "seconds")
                    print()
                else:
                    print("A* Path not found!")
                    print("Time elapsed = ", t1 - t0, "seconds")
                    print()


def map(self):
    with open('maps/map' + str(self) + '.txt', 'r') as f:
        lines = 0
        lines = f.readlines()
        for line in lines:
            maps.append(line.strip('\n').split(' '))  # map je teraz 2d arr

        map_in_gui()


def map_in_gui():  # tuto sa vykresli mapa
    for row in range(len(maps)):  # ze pocet rows
        for col in range(len(maps[0])):  # pocet cols
            if maps[row][col] == '2':
                screen.blit(MARIO, (col * MARGIN + 70, row * MARGIN))
                continue
            if maps[row][col] == '0' or maps[row][col] == '3':
                continue

            screen.blit(WALL, (col * MARGIN + 70, row * MARGIN))

    pygame.display.flip()
    mario_moving_in_game(steps)


def draw_window(self):  # vytvori bielu plochu a bude sa updatovat
    screen.fill(WHITE)
    map(self)
    # only_get_map(self)


def game_window(self):
    clock = pygame.time.Clock()  # iba pre fps
    t = 1
    run = True
    while run:
        clock.tick(FPS)  # max fps 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ohandlovanie X - zatvori okno
                run = False
        if t == 1:
            maps.clear()
            draw_window(self)  # presne tuto sa to zacykluje
            t += 1


def main():
    screen.fill(WHITE)
    clock = pygame.time.Clock()  # iba pre fps
    run = True
    pressed = 0
    while run:

        clock.tick(FPS)  # max fps 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ohandlovanie X - zatvori okno
                run = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:

                    if pressed < 0:
                        pressed += 1

                elif event.key == pygame.K_DOWN:
                    if pressed > -5:
                        pressed -= 1

                if event.key == pygame.K_RETURN:  # ked sa stlaci enter
                    if pressed == 0:
                        return game_window(1)
                    elif pressed == -1:
                        return game_window(2)
                    elif pressed == -2:
                        return game_window(3)
                    elif pressed == -3:
                        return game_window(4)
                    elif pressed == -4:
                        return game_window(5)
                    elif pressed == -5:
                        quit()

        screen.fill(WHITE)  # priprava na vypisanie na uvodnu obrazovku
        title = text_format("Labyrint", font, 90, WHITE)
        if pressed == 0:
            screen.blit(LVL1, (WIDTH / 2 - 90, 260))
        elif pressed == -1:
            screen.blit(LVL2, (WIDTH / 2 - 90, 260))
        elif pressed == -2:
            screen.blit(LVL3, (WIDTH / 2 - 90, 260))
        elif pressed == -3:
            screen.blit(LVL4, (WIDTH / 2 - 90, 260))
        elif pressed == -4:
            screen.blit(LVL5, (WIDTH / 2 - 90, 260))
        elif pressed == -5:
            text_level = screen.blit(QUIT, (WIDTH / 2 - 65, 260))

        screen.blit(SIGN, (WIDTH / 2 - 162.5, 30))
        screen.blit(UP, (WIDTH / 2 - 20, 210))
        screen.blit(DOWN, (WIDTH / 2 - 16, 320))
        pygame.display.update()
        # pygame.quit()


def find_dest(self):
    with open('maps/map' + str(self) + '.txt', 'r') as f:
        lines2 = f.readlines()
        for line in lines2:
            maps.append(line.strip('\n').split(' '))  # map je teraz 2d arr

        for row in range(len(maps)):  # ze pocet rows
            for col in range(len(maps[0])):  # pocet cols
                if maps[row][col] == '3':
                    destination = algos.GridPosition(row, col)

                if maps[row][col] == '2':
                    starting_position = algos.GridPosition(row, col)

        return destination, starting_position


def find_dest2():
    for row in range(len(maps)):  # ze pocet rows
        for col in range(len(maps[0])):  # pocet cols
            if maps[row][col] == '3':
                destination = algos.GridPosition(row, col)

            if maps[row][col] == '2':
                starting_position = algos.GridPosition(row, col)

    return destination, starting_position


if __name__ == "__main__":
    global a
    a = main()

# dushandsa andreiiii boiiii
