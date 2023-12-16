#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [IMPORTS] #

import pygame 
from tiles import Tile 
from settings import *

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Level(pygame.sprite.Sprite):
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [OBJECTS] #
    
    def __init__(self, surface, layout):
        super().__init__()

        self.tiles = Tile(300, 500, (255, 255, 255), 0, surface)
        self.myrect4 = pygame.Rect(350, 550, tile_size, tile_size)
        self.map = layout
        self.list_tiles_solo = []
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 001] #
                                                                        
    def printmap(self):

        for row_index, row in enumerate(self.map):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    solo = pygame.Rect(x, y, tile_size, tile_size)
                    pygame.draw.rect(self.tiles.display, self.tiles.color, solo)
                    self.list_tiles_solo.append(solo)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 002] #

    def collision_solo(self):
        
        pygame.draw.rect(self.tiles.display, (0, 0, 0), self.tiles.myrect)

        for solo in self.list_tiles_solo:

            pygame.draw.rect(self.tiles.display, (0, 0, 0), solo)
            pygame.draw.rect(self.tiles.display, (255, 0, 0), solo, 2)

            if self.tiles.myrect.colliderect(solo):
                if self.tiles.pos == 'right':
                    self.tiles.myrect.x -= 1
                elif self.tiles.pos == 'left':
                    self.tiles.myrect.x += 1
                elif self.tiles.pos == 'down':
                    self.tiles.myrect.y -= 1
                elif self.tiles.pos == 'up':
                    self.tiles.myrect.y += 1

            pygame.draw.rect(self.tiles.display, (0, 0, 0), solo)
            pygame.draw.rect(self.tiles.display, (255, 0, 0), solo, 2)

        pygame.draw.rect(self.tiles.display, self.tiles.color, self.tiles.myrect)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 003] #

    def run(self):

        self.tiles.update()
        self.printmap()
        self.collision_solo()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
