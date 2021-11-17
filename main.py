import random

import pygame
import os

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Labyrint')
WHITE = (255, 255, 255)

# class MAP:
#     def __init__(self, map, tiles):
#         self.tiles = pygame.image.load(tiles)
#
#         l = [line.strip() for line in open(map).readlines()]
#         self.map = [[None]*len(l[0]) for j in range(len(l))]
#         for i in range(len(l[0])):
#             for j in range(len(l)):
#                 print('l')

def map():
    with open('maps/map1.txt', 'r') as f:
        for line in f:
            print (line)    #iba vypisuje do konzoly
                    
                

FPS = 60
def draw_window():                          #vytvori bielu plochu a bude sa updatovat
    WIN.fill(WHITE)
    map()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #max fps 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       #ohandlovanie X - zatvori okno
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()