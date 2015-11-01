import pygame
import sys

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Stargate Dialing Program')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (64, 64, 255)
RED = (255, 64, 64)

clock = pygame.time.Clock()

# load images
puddle = pygame.image.load('puddle.png')

# Load images
ABYDOS = [pygame.image.load('glyphs/glyph27.gif'),
          pygame.image.load('glyphs/glyph07.gif'),
          pygame.image.load('glyphs/glyph15.gif'),
          pygame.image.load('glyphs/glyph32.gif'),
          pygame.image.load('glyphs/glyph12.gif'),
          pygame.image.load('glyphs/glyph30.gif'),
          pygame.image.load('glyphs/glyph01.gif')]

# GATE ADDRESSES
ADDRESSES = ['ABYDOS', ['A', 'Y', 'B', 'L', 'X', 'T', 'U']]


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
              encoded += 1

          if event.key == pygame.K_y:
              # center left
              pygame.draw.polygon(screen, RED, [[50, 275], [100, 300], [50, 325]])
              pygame.draw.rect(screen, WHITE, [600, 110, 100, 50])
              screen.blit(ABYDOS[1], (625, 110))
              encoded += 1

          if event.key == pygame.K_b:
              # top left
              pygame.draw.polygon(screen, RED, [[135, 110], [150, 165], [100, 150]])
              pygame.draw.rect(screen, WHITE, [600, 170, 100, 50])
              screen.blit(ABYDOS[2], (625, 170))
              encoded += 1

          if event.key == pygame.K_x:
              # top right
              pygame.draw.polygon(screen, RED, [[465, 110], [450, 170], [500, 150]])
              pygame.draw.rect(screen, WHITE, [600, 230, 100, 50])
              screen.blit(ABYDOS[3], (625, 230))
              encoded += 1

          if event.key == pygame.K_t:
              # center right
              pygame.draw.polygon(screen, RED, [[550, 275], [500, 300], [550, 325]])
              pygame.draw.rect(screen, WHITE, [600, 290, 100, 50])
              screen.blit(ABYDOS[4], (625, 290))
              encoded += 1

          if event.key == pygame.K_u:
              # bottom right
              pygame.draw.polygon(screen, RED, [[475, 475], [455, 425], [510, 430]])
              pygame.draw.rect(screen, WHITE, [600, 350, 100, 50])
              screen.blit(ABYDOS[5], (625, 350))
              encoded += 1

          if event.key == pygame.K_h:
              # point of origin
              pygame.draw.polygon(screen, RED, [[275, 50], [300, 100], [325, 50]])
              pygame.draw.rect(screen, WHITE, [600, 410, 100, 50])
              screen.blit(ABYDOS[6], (625, 410))
              encoded += 1


    dialing_interface()
    draw_stargate_inactive()

    if encoded == 7:
        draw_stargate_active()

    pygame.display.update()
    clock.tick(60)



if __name__ == '__main__':
  main()
  pygame.quit()
  quit()
