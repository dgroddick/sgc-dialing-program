#!/usr/bin/env python3

import pygame
import sys
import time

# Import Gate addresses
from addresses import db

# setup
pygame.init()

width = 800
height = 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Stargate Dialing Program')
font = pygame.font.SysFont(None, 72)

# Load images
icon = pygame.image.load('glyphs/glyph1.gif')
icon = pygame.display.set_icon(icon)
puddle = pygame.image.load('puddle.png')

# array to store gate symbols
SYMBOLS = []

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (64, 64, 255)
RED = (255, 64, 64)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()


def load_symbols():
    global SYMBOLS
    for i in range(1, 42):
        SYMBOLS.append(pygame.image.load('glyphs/glyph' + str(i) + '.gif'))


def dialing_interface():
    # chevrons
    pygame.draw.rect(screen, WHITE, [600, 50, 100, 50], 2)    # 1
    pygame.draw.rect(screen, WHITE, [600, 110, 100, 50], 2)   # 2
    pygame.draw.rect(screen, WHITE, [600, 170, 100, 50], 2)   # 3
    pygame.draw.rect(screen, WHITE, [600, 230, 100, 50], 2)   # 4
    pygame.draw.rect(screen, WHITE, [600, 290, 100, 50], 2)   # 5
    pygame.draw.rect(screen, WHITE, [600, 350, 100, 50], 2)   # 6
    pygame.draw.rect(screen, WHITE, [600, 410, 100, 50], 2)   # 7

    # chevron 8 is hidden FOR NOW!!
    #pygame.draw.rect(screen, WHITE, [600, 470, 100, 50], 2)   # 8



def gate_status(msg, color):
    pygame.draw.rect(screen, WHITE, [55, 570, 500, 100], 2)
    screen.fill(BLACK, (70, 580, 480, 70))
    text = font.render(msg, True, color)
    screen.blit(text, (300 - text.get_width() / 2, 620 - text.get_height() / 2))


def draw_stargate_inactive():

    # stargate
    pygame.draw.circle(screen, WHITE, (300, 300), 250, 1)
    pygame.draw.circle(screen, WHITE, (300, 300), 200, 1)

    # chevrons
    # top-center
    pygame.draw.polygon(screen, WHITE, [[275, 50], [300, 100], [325, 50]], 5)
    # top-left
    pygame.draw.polygon(screen, WHITE, [[135, 110], [150, 165], [100, 150]], 5)
    # top-right
    pygame.draw.polygon(screen, WHITE, [[465, 110], [450, 170], [500, 150]], 5)
    # mid-left
    pygame.draw.polygon(screen, WHITE, [[50, 275], [100, 300], [50, 325]], 5)
    # mid-right
    pygame.draw.polygon(screen, WHITE, [[550, 275], [500, 300], [550, 325]], 5)
    # bottom-left
    pygame.draw.polygon(screen, WHITE, [[125, 480], [140, 425], [90, 435]], 5)
    # bottom-right
    pygame.draw.polygon(screen, WHITE, [[475, 475], [455, 425], [510, 430]], 5)


def draw_stargate_active():
    draw_stargate_inactive()
    screen.blit(puddle, (95, 97))



def lock_chevron(position):
    global SYMBOLS

    if position == 1:
        pygame.draw.polygon(screen, RED, [[125, 480], [140, 425], [90, 435]])
        pygame.draw.rect(screen, WHITE, [600, 50, 100, 50])
        screen.blit(SYMBOLS[0], (625, 50))
    elif position == 2:
        pygame.draw.polygon(screen, RED, [[50, 275], [100, 300], [50, 325]])
        pygame.draw.rect(screen, WHITE, [600, 110, 100, 50])
        screen.blit(SYMBOLS[1], (625, 110))
    elif position == 3:
        pygame.draw.polygon(screen, RED, [[135, 110], [150, 165], [100, 150]])
        pygame.draw.rect(screen, WHITE, [600, 170, 100, 50])
        screen.blit(SYMBOLS[2], (625, 170))
    elif position == 4:
        pygame.draw.polygon(screen, RED, [[465, 110], [450, 170], [500, 150]])
        pygame.draw.rect(screen, WHITE, [600, 230, 100, 50])
        screen.blit(SYMBOLS[3], (625, 230))
    elif position == 5:
        pygame.draw.polygon(screen, RED, [[550, 275], [500, 300], [550, 325]])
        pygame.draw.rect(screen, WHITE, [600, 290, 100, 50])
        screen.blit(SYMBOLS[4], (625, 290))
    elif position == 6:
        pygame.draw.polygon(screen, RED, [[475, 475], [455, 425], [510, 430]])
        pygame.draw.rect(screen, WHITE, [600, 350, 100, 50])
        screen.blit(SYMBOLS[5], (625, 350))
    else:
        pygame.draw.polygon(screen, RED, [[275, 50], [300, 100], [325, 50]])
        pygame.draw.rect(screen, WHITE, [600, 410, 100, 50])
        screen.blit(SYMBOLS[6], (625, 410))


def main():

    programExit = False
    encoded = 0

    load_symbols()
    dialing_interface()
    draw_stargate_inactive()
    gate_status("IDLE", WHITE)

    # List to hold the dialed symbols
    address = []

    # main loop
    while not programExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                programExit = True

            # capture gate address keypress
            if event.type == pygame.KEYDOWN:
                address.append(event.unicode)
                lock_chevron(len(address))
                gate_status("ENGAGED", YELLOW)

        # 7 Symbol gate address
        if len(address) == 7:
            draw_stargate_active()
            gate_status("LOCKED", BLUE)

        pygame.display.update()
        clock.tick(60)



if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
