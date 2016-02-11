#!/usr/bin/env python

import pygame
import sys
import time

# Import Gate addresses
from addresses import db

# Load images
icon = pygame.image.load('glyphs/glyph01.gif')
icon = pygame.display.set_icon(icon)
puddle = pygame.image.load('puddle.png')

ABYDOS = [pygame.image.load('glyphs/glyph27.gif'),
          pygame.image.load('glyphs/glyph07.gif'),
          pygame.image.load('glyphs/glyph15.gif'),
          pygame.image.load('glyphs/glyph32.gif'),
          pygame.image.load('glyphs/glyph12.gif'),
          pygame.image.load('glyphs/glyph30.gif'),
          pygame.image.load('glyphs/glyph01.gif')]


pygame.init()

width = 800
height = 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Stargate Dialing Program')
font = pygame.font.SysFont(None, 72)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (64, 64, 255)
RED = (255, 64, 64)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()



def dialing_interface():
  # chevron locks
  pygame.draw.rect(screen, WHITE, [600, 50, 100, 50], 2)    # 1
  pygame.draw.rect(screen, WHITE, [600, 110, 100, 50], 2)   # 2
  pygame.draw.rect(screen, WHITE, [600, 170, 100, 50], 2)   # 3
  pygame.draw.rect(screen, WHITE, [600, 230, 100, 50], 2)   # 4
  pygame.draw.rect(screen, WHITE, [600, 290, 100, 50], 2)   # 5
  pygame.draw.rect(screen, WHITE, [600, 350, 100, 50], 2)   # 6
  pygame.draw.rect(screen, WHITE, [600, 410, 100, 50], 2)   # 7
  pygame.draw.rect(screen, WHITE, [600, 470, 100, 50], 2)   # 8



def gate_status(msg, color):
  pygame.draw.rect(screen, WHITE, [55, 570, 500, 100], 2)
  screen.fill(BLACK, (70, 580, 480, 70))
  text = font.render(msg, True, color)
  screen.blit(text, (300 - text.get_width() // 2, 620 - text.get_height() // 2))


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


def main():

  programExit = False
  encoded = 0

  dialing_interface()
  draw_stargate_inactive()
  gate_status("IDLE", WHITE)

  # List to hold the dialed symbols
  address = []

  while not programExit:

    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        programExit = True

      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a:
              # bottom left
              pygame.draw.polygon(screen, RED, [[125, 480], [140, 425], [90, 435]])
              pygame.draw.rect(screen, WHITE, [600, 50, 100, 50])
              screen.blit(ABYDOS[0], (625, 50))
              gate_status("ENGAGED", YELLOW)
              encoded += 1

          if event.key == pygame.K_y:
              # center left
              pygame.draw.polygon(screen, RED, [[50, 275], [100, 300], [50, 325]])
              pygame.draw.rect(screen, WHITE, [600, 110, 100, 50])
              screen.blit(ABYDOS[1], (625, 110))
              gate_status("ENGAGED", YELLOW)
              encoded += 1

          if event.key == pygame.K_b:
              # top left
              pygame.draw.polygon(screen, RED, [[135, 110], [150, 165], [100, 150]])
              pygame.draw.rect(screen, WHITE, [600, 170, 100, 50])
              screen.blit(ABYDOS[2], (625, 170))
              gate_status("ENGAGED", YELLOW)
              encoded += 1

          if event.key == pygame.K_x:
              # top right
              pygame.draw.polygon(screen, RED, [[465, 110], [450, 170], [500, 150]])
              pygame.draw.rect(screen, WHITE, [600, 230, 100, 50])
              screen.blit(ABYDOS[3], (625, 230))
              gate_status("ENGAGED", YELLOW)
              encoded += 1

          if event.key == pygame.K_t:
              # center right
              pygame.draw.polygon(screen, RED, [[550, 275], [500, 300], [550, 325]])
              pygame.draw.rect(screen, WHITE, [600, 290, 100, 50])
              screen.blit(ABYDOS[4], (625, 290))
              gate_status("ENGAGED", YELLOW)
              encoded += 1

          if event.key == pygame.K_u:
              # bottom right
              pygame.draw.polygon(screen, RED, [[475, 475], [455, 425], [510, 430]])
              pygame.draw.rect(screen, WHITE, [600, 350, 100, 50])
              screen.blit(ABYDOS[5], (625, 350))
              gate_status("ENGAGED", YELLOW)
              encoded += 1

          if event.key == pygame.K_h:
              # point of origin
              pygame.draw.polygon(screen, RED, [[275, 50], [300, 100], [325, 50]])
              pygame.draw.rect(screen, WHITE, [600, 410, 100, 50])
              screen.blit(ABYDOS[6], (625, 410))
              encoded += 1


    if encoded == 7:
        draw_stargate_active()
        gate_status("LOCKED", BLUE)


    pygame.display.update()
    clock.tick(60)



if __name__ == '__main__':
  main()
  pygame.quit()
  quit()
