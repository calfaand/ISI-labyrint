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
MARGIN=15


FPS = 60
display_surface = pygame.display.set_mode((500, 500 ))
WALL = pygame.image.load('assets/wall.png')


def map():

    with open('maps/map1.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            maps.append(line.strip('\n').split(' '))# map je teraz 2d arr


def map_in_gui():

    for row in range(len(maps)):        #ze pocet rows
        for col in range(len(maps[0])):     # pocet cols
            if maps[row][col] == '0':
                continue
            display_surface.blit(WALL, (row*MARGIN, col*MARGIN))


    pygame.display.flip()



def draw_window():                          #vytvori bielu plochu a bude sa updatovat
    WIN.fill(WHITE)
    #map()
    map_in_gui()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    map()
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