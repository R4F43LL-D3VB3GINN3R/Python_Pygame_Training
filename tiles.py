#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [IMPORTS] #

import pygame 
import random
from settings import *

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Tile(pygame.sprite.Sprite):
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [OBJECTS] #

    def __init__(self, x, y, color, breath, surface):
        super().__init__()

        self.random_width = random.randint(0, screen_width)
        self.random_height = random.randint(0, screen_height)
        self.myrect = pygame.Rect(x, y, tile_size, tile_size)
        self.myrect2 = pygame.Rect(0, 0, tile_size, tile_size)
        self.myrect3 = pygame.Rect(self.random_width, y, tile_size, tile_size)
        self.myrect4 = pygame.Rect(x, self.random_height, tile_size, tile_size)
        self.direction = pygame.math.Vector2(0,0)
        self.direction.y = -1
        self.color = color 
        self.breath = breath 
        self.breathing = True 
        self.pos = 'falling'
        self.display = surface
        self.jump_force = 30
        self.jumping = True
        self.speed = 5

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 001] #

    def breathrect(self):

        pygame.draw.rect(self.display, (0, 0, 0), self.myrect)

        if self.breathing:
            self.breath += 1
            self.myrect.width += 1
            self.myrect.height += 1
            if self.breath == 30:
                self.breathing = False 
        else: 
            self.breath -= 1
            self.myrect.width -= 1
            self.myrect.height -= 1
            if self.breath == 0:
                self.breathing = True

        pygame.draw.rect(self.display, self.color, self.myrect)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 002] #

    def moverect(self):

        pygame.draw.rect(self.display, (0, 0, 0), self.myrect)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.myrect.x += self.speed
            self.direction.x = 1
            self.pos = 'right'
        elif keys[pygame.K_a]:
            self.myrect.x -= self.speed
            self.direction.x = -1
            self.pos = 'left'

        if keys[pygame.K_s]:
            self.pos = 'down'

        pygame.draw.rect(self.display, self.color, self.myrect)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 003] #

    def jump_rect(self):

        keys = pygame.key.get_pressed()

        pygame.draw.rect(self.display, (0, 0, 0), self.myrect)

        if keys[pygame.K_w] and self.jumping == True:
            self.myrect.y -= self.jump_force
            self.direction.y = -1
            self.pos = 'up'
        if not keys[pygame.K_w] and self.direction.y == -1:
            self.pos = 'falling'
            self.jumping == False
    
        pygame.draw.rect(self.display, self.color, self.myrect)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 004] #

    def colliderect(self):

        pygame.draw.rect(self.display, (0, 0, 0), self.myrect2)

        if self.myrect.colliderect(self.myrect2):
            if self.pos == 'right':
                self.myrect2.x += 1
            elif self.pos == 'left':
                self.myrect2.x -= 1
            elif self.pos == 'down':
                self.myrect2.y += 1
            elif self.pos == 'up':
                self.myrect2.y -= 1

        pygame.draw.rect(self.display, self.color, self.myrect2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 005] #

    def rainingrects(self):

        pygame.draw.rect(self.display, (0, 0, 0), self.myrect3)

        self.myrect3.y += 10

        if self.myrect3.y > 700:
            self.myrect3.y = 0
            self.random_width = random.randint(0, screen_width)
            self.myrect3.x = self.random_width 

        pygame.draw.rect(self.display, self.color, self.myrect3)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 006] #

    def blastrects(self):

        pygame.draw.rect(self.display, (0, 0, 0,), self.myrect4)

        self.myrect4.x += 10

        print(self.myrect4.x)

        if self.myrect4.x > 600:
            print(self.myrect4.x)
            self.myrect4.x = 0
            self.random_height = random.randint(0, screen_height)
            self.myrect4.y = self.random_height

        pygame.draw.rect(self.display, self.color, self.myrect4)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# [METHOD: 007] #

    def update(self):

        self.moverect()
        self.jump_rect()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
