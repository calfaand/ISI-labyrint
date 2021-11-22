import pygame
from enum import Enum
from pygame.locals import *

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
maps = []
W = 20
H = 20
MARGIN = 15
FPS = 60
font = "ariel"
WALL = pygame.image.load('assets/wall.png')
MARIO = pygame.image.load('assets/mario.png')
LEN_MAP_ROW = 0  # dlzka vykreslenej mapy         preto zeby som vedel az kam max sa da ist mariom ,moozno nebude ani treba
LEN_MAP_COL = 0  # sirka vykreslenej mapy
MX = 0
MY = 0
steps=0



# https://www.youtube.com/watch?v=bmRFi7-gy5Y&t=446s

class Type(Enum):
    FREE = 0
    WALL = 1


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.SysFont(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

def move_down(x,y,steps, dir):
    # if dir == pygame.K_DOWN:
    if maps[x + 1][y] == '0' or maps[x + 1][y] == '3':
        if maps[x + 1][y] == '3':
            x, y = move_mario(x, y, pygame.K_DOWN)
            win_game(steps)
        x, y = move_mario(x, y, pygame.K_DOWN)
    mario_moving_in_game(steps)
    
def move_up(x,y,steps,dir):
    if maps[x - 1][y] == '0' or maps[x - 1][y] == '3':
        if maps[x - 1][y] == '3':
            x, y = move_mario(x, y, pygame.K_UP)
            win_game(steps)
        x, y = move_mario(x, y, pygame.K_UP)
    mario_moving_in_game(steps)

def move_left(x,y,steps, dir):
    if maps[x][y - 1] == '0' or maps[x][y- 1] == '3':
        if maps[x][y - 1] == '3':
            x, y = move_mario(x, y, pygame.K_LEFT)
            win_game(steps)
        x, y = move_mario(x, y, pygame.K_LEFT)
    mario_moving_in_game(steps)


def move_right(x,y,steps,dir):
    if maps[x][y + 1] == '0' or maps[x][y+ 1] == '3':
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
    #print('mario', mario_is_on_x, mario_is_on_y)        # dobre pozicie
    run = True
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                steps+=1
                if event.key == pygame.K_DOWN:
                    move_down(mario_is_on_x, mario_is_on_y, steps, pygame.K_DOWN)

                if event.key == pygame.K_UP:
                    move_up(mario_is_on_x, mario_is_on_y, steps, pygame.K_UP)

                if event.key == pygame.K_LEFT:
                    move_left(mario_is_on_x, mario_is_on_y, steps, pygame.K_LEFT)

                if event.key == pygame.K_RIGHT:
                    move_right(mario_is_on_x, mario_is_on_y, steps, pygame.K_RIGHT)

        new_map()
        pygame.display.update()     #ked je o riadok hore break, mapu vypise do cons dobru, uz len refresh obrazovky, skoci to na riadok 141


def move_mario(x, y, direct):
    maps[x][y] = '0'
    print(x, y)

    if direct == pygame.K_UP:
        x -= 1
    elif direct == pygame.K_DOWN:
        x += 1
    elif direct == pygame.K_LEFT:
        y -= 1
    elif direct == pygame.K_RIGHT:
        y += 1
    else:
        print("Fuck this shit")

    maps[x][y] = '2'
    # print(x, y)
    return x,y

def win_game(steps):

    screen.fill(BLACK)
    run = True
    pressed = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ohandlovanie X - zatvori okno
                run = False
        print('winn on ', steps, 'steps')
        win_text = text_format("CONGRATULATION", font, 70, WHITE)
        win_rect = win_text.get_rect()
        steps_text= text_format(str(steps) + ' steps', font, 70, WHITE)
        steps_rect = steps_text.get_rect()
        screen.blit(win_text, (WIDTH / 2 - (win_rect[2] / 2), 80))
        screen.blit(steps_text, (WIDTH / 2 - (steps_rect[2] / 2), 160))
        pygame.display.flip()
        pygame.time.delay(1000)
        quit()


def new_map():

    screen.fill(WHITE)
    for row in range(len(maps)):  # ze pocet rows
        for col in range(len(maps[0])):  # pocet cols
            if maps[row][col] == '2':
                screen.blit(MARIO, (col * MARGIN, row * MARGIN))

                continue
            if maps[row][col] == '0' or maps[row][col] == '3':
                continue

            screen.blit(WALL, (col * MARGIN, row * MARGIN))


    pygame.display.flip()

def map(self):
    # print(' som v map')
    with open('maps/map' + str(self) + '.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            maps.append(line.strip('\n').split(' '))  # map je teraz 2d arr
    map_in_gui()


def map_in_gui():
    # pygame.display.update()
    # print('map in gui')

    for row in range(len(maps)):  # ze pocet rows
        for col in range(len(maps[0])):  # pocet cols
            if maps[row][col] == '2':
                screen.blit(MARIO, (col * MARGIN, row * MARGIN))

                continue
            if maps[row][col] == '0' or maps[row][col] == '3':
                continue

            screen.blit(WALL, (col * MARGIN, row * MARGIN))

    pygame.display.flip()
    mario_moving_in_game(steps)


def draw_window(self):  # vytvori bielu plochu a bude sa updatovat
    # pygame.display.update()
    #print('draw_window')

    screen.fill(WHITE)
    map(self)

    # map_in_gui()


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
            draw_window(self)  # presne tuto sa to zacykluje
            print(maps)

            t += 1


def main():
    clock = pygame.time.Clock()  # iba pre fps
    run = True
    pressed = 0
    while run:
        clock.tick(FPS)  # max fps 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ohandlovanie X - zatvori okno
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:

                    if pressed < 0:
                        pressed += 1

                elif event.key == pygame.K_DOWN:
                    if pressed > -5:
                        pressed -= 1

                if event.key == pygame.K_RETURN:  # ked sa stlaci enter
                    if pressed == 0:
                        print('level 1')
                        return 1
                    elif pressed == -1:
                        print('level 2')
                        return 2
                    elif pressed == -2:
                        print('level 3')
                        return 3
                    elif pressed == -3:
                        print('level 4')
                        return 4
                    elif pressed == -4:
                        print('level 5')
                        return 5
                    elif pressed == -5:
                        print('quit')
                        pygame.quit()
                        quit()

        screen.fill(BLUE)  # priprava na vypisanie na uvodnu obrazovku
        title = text_format("Labyrint", font, 90, WHITE)
        if pressed == 0:
            text_level = text_format('LEVEL 1', font, 75, WHITE)
        elif pressed == -1:
            text_level = text_format('LEVEL 2', font, 75, WHITE)
        elif pressed == -2:
            text_level = text_format('LEVEL 3', font, 75, WHITE)
        elif pressed == -3:
            text_level = text_format('LEVEL 4', font, 75, WHITE)
        elif pressed == -4:
            text_level = text_format('LEVEL 5', font, 75, WHITE)
        elif pressed == -5:
            text_level = text_format('QUIT', font, 75, WHITE)

        text_up = text_format('^', font, 75, WHITE)
        text_down = text_format('v', font, 75, WHITE)

        title_rect = title.get_rect()
        start_rect = text_level.get_rect()
        down_rect = text_up.get_rect()
        up_rect = text_down.get_rect()

        # menu text
        screen.blit(title, (WIDTH / 2 - (title_rect[2] / 2), 80))  # toto je nazov hry
        screen.blit(text_up, (WIDTH / 2 - (up_rect[2] / 2), 200))  # toto bude ^
        screen.blit(text_level, (WIDTH / 2 - (start_rect[2] / 2), 260))  # toto sa bude menit, vypis daneho lvl
        screen.blit(text_down, (WIDTH / 2 - (down_rect[2] / 2), 320))  # toto bude znazornenie ze sa da ist dole

        pygame.display.update()

    # pygame.quit()


if __name__ == "__main__":
    a = main()
    print(a)
    print('vonku z main')
    game_window(a)

# dushan
