#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# [IMPORTS] #   

import pygame
from tiles import Tile
from level import Level

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# [SETTINGS] #

pygame.init()
clock = pygame.time.Clock()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# [SCREEN] #

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# [INSTÂNCIAS] #

myrect = Level()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# [EVENTS] #

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    myrect.run(screen)

    pygame.display.flip()
    clock.tick(60)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
