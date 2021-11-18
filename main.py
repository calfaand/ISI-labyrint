import random

import pygame
import os
import numpy as np

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Labyrint')
WHITE = (255, 255, 255)
GREEN = (0,255,0)
maps=[]
W=20
H=20
MARGIN=5

WALL = pygame.image.load('assets/wall.png')


def map():
    # maps = np.genfromtxt('maps/map1.txt', dtype=None)
    # print (maps)

    with open('maps/map1.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            maps.append(line.strip('\n').split(' '))# map je teraz 2d arr

    print (maps)

        # for line in map:
        #     map.append(line.strip())




FPS = 60
display_surface = pygame.display.set_mode((500, 500 ))




def map_in_gui():

    for row in range(1,10):        #ze pocet rows
        for col in range(1,10):     # pocet cols
            if maps[row][col]==0:
                break
            display_surface.blit(WALL, (row*MARGIN,col*MARGIN))

    pygame.display.flip()



def draw_window():                          #vytvori bielu plochu a bude sa updatovat
    WIN.fill(WHITE)
    #map()
    # map_in_gui()
    # display_surface.blit(WALL, (1, 1))
    # display_surface.blit(WALL, (30, 30))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    run = True
    map()
    print(maps[1][1])
    while run:
        clock.tick(FPS) #max fps 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       #ohandlovanie X - zatvori okno
                run = False

        draw_window()


    pygame.quit()

if __name__ == "__main__":
    main()

#dushan