import pygame
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


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.SysFont(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


# def menu():
#     screen.fill(BLUE)
#     title = text_format("Labyrint", font, 90, WHITE)
#     if selected == 'start':
#         text_start = text_format('START', font, 75, WHITE)
#     else:
#         text_start = text_format('START', font, 75, BLACK)
#     if selected == 'quit':
#         text_quit = text_format('QUIT', font, 75, WHITE)
#     else:
#         text_quit = text_format('QUIT', font, 75, BLACK)
#
#     title_rect = title.get_rect()
#     start_rect = text_start.get_rect()
#     quit_rect = text_quit.get_rect()
#
#     # menu text
#     screen.blit(title, (WIDTH / 2 - (title_rect[2] / 2), 80))
#     screen.blit(text_start, (WIDTH / 2 - (start_rect[2] / 2), 300))
#     screen.blit(text_quit, (WIDTH / 2 - (quit_rect[2] / 2), 360))
#
#     pygame.display.update()


def map():
    with open('maps/map2.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            maps.append(line.strip('\n').split(' '))  # map je teraz 2d arr


def map_in_gui():
    for row in range(len(maps)):  # ze pocet rows
        for col in range(len(maps[0])):  # pocet cols
            if maps[row][col] == '0':
                continue
            screen.blit(WALL, (row * MARGIN, col * MARGIN))

    pygame.display.flip()


def draw_window():  # vytvori bielu plochu a bude sa updatovat
    pygame.display.update()
    screen.fill(WHITE)
    # map()
    map_in_gui()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    selected= 'start'

    # map()
    while run:
        clock.tick(FPS)  # max fps 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ohandlovanie X - zatvori okno
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = 'start'
                elif event.key == pygame.K_DOWN:
                    selected = 'quit'
                if event.key == pygame.K_RETURN:
                    if selected == 'start':
                        print('start')


                    if selected == 'quit':
                        print('quit')
                        pygame.quit()
                        quit()

        screen.fill(BLUE)
        title = text_format("Labyrint", font, 90, WHITE)
        if selected == 'start':
            text_start = text_format('START', font, 75, WHITE)
        else:
            text_start = text_format('START', font, 75, BLACK)
        if selected == 'quit':
            text_quit = text_format('QUIT', font, 75, WHITE)
        else:
            text_quit = text_format('QUIT', font, 75, BLACK)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # menu text
        screen.blit(title, (WIDTH / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (WIDTH / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_quit, (WIDTH / 2 - (quit_rect[2] / 2), 360))

        pygame.display.update()
        # draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()

# dushan
