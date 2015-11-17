#!/usr/bin/env python
import pygame
import sys
import time

# Import Gate addresses
from addresses import db

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (64, 64, 255)
RED = (255, 64, 64)
YELLOW = (255, 255, 0)


class Stargate():
    def __init__(self):

        # set up the Pygame environment
        pygame.init()

        width = 1280
        height = 768

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Stargate Dialing Program')
        self.font = pygame.font.SysFont(None, 72)
        self.clock = pygame.time.Clock()

        # status of the Stargate
        self.gate_active = False


    def load_graphics(self):
        self.puddle = pygame.image.load('puddle.png')
        self.stargate = pygame.image.load('stargate.jpg')
        self.glyphs = []


    def update(self):
        self.clock.tick(60)
        self.screen.fill(0)

        self.load_graphics()
        self.gate_status("IDLE", WHITE)
        self.dialing_interface()

        if self.gate_active:
            self.draw_stargate_active()
            self.gate_status("LOCKED", BLUE)
        else:
            self.draw_stargate_inactive()
            self.gate_status("IDLE", WHITE)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.gate_active == True:
                        self.gate_active = False
                    else:
                        self.gate_active = True

        pygame.display.update()


    def draw_stargate_inactive(self):
        self.screen.blit(self.stargate, (400, 30))


    def draw_stargate_active(self):
        self.screen.blit(self.stargate, (400, 30))
        self.screen.blit(self.puddle, (473, 89))


    def gate_status(self, msg, color):
        pygame.draw.rect(self.screen, WHITE, [435, 600, 500, 100], 2)
        self.screen.fill(BLACK, (437, 605, 490, 90))
        self.text = self.font.render(msg, True, color)
        self.screen.blit(self.text, (690 - self.text.get_width() / 2, 650 - self.text.get_height() / 2))


    def dialing_interface(self):
        # chevron locks
        pygame.draw.rect(self.screen, WHITE, [1100, 50, 100, 50], 2)    # 1
        pygame.draw.rect(self.screen, WHITE, [1100, 110, 100, 50], 2)   # 2
        pygame.draw.rect(self.screen, WHITE, [1100, 170, 100, 50], 2)   # 3
        pygame.draw.rect(self.screen, WHITE, [1100, 230, 100, 50], 2)   # 4
        pygame.draw.rect(self.screen, WHITE, [1100, 290, 100, 50], 2)   # 5
        pygame.draw.rect(self.screen, WHITE, [1100, 350, 100, 50], 2)   # 6
        pygame.draw.rect(self.screen, WHITE, [1100, 410, 100, 50], 2)   # 7
        pygame.draw.rect(self.screen, WHITE, [1100, 470, 100, 50], 2)   # 8
        pygame.draw.rect(self.screen, WHITE, [1100, 530, 100, 50], 2)   # 9


if __name__ == '__main__':

    sg = Stargate()

    while True:
        sg.update()
