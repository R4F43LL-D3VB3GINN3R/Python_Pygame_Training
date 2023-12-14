#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [IMPORTS] #

import pygame

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Tile(pygame.sprite.Sprite):
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [OBJECTS] #

    def __init__(self, pos_width, pos_height, width, height, color, breath, surface):
        super().__init__()

        self.rect = pygame.Rect(pos_width, pos_height, width, height)
        self.rect2 = pygame.Rect(pos_width + 50, pos_height + 50, width, height)
        self.color = color 
        self.breath = breath
        self.breathing = True 
        self.position = 'stop'
        self.display = surface

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 001] #

    def breathrect(self):

        pygame.draw.rect(self.display, (0, 0, 0), self.rect)

        if self.breathing:
            self.breath += 1
            self.rect.width += 1
            self.rect.height += 1
            if self.breath == 30:
                self.breathing = False 
        else: 
            self.breath -= 1
            self.rect.width -= 1
            self.rect.height -= 1
            if self.breath == 0:
                self.breathing = True 

        pygame.draw.rect(self.display, self.color, self.rect)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 002] #

    def moverect(self):

        pygame.draw.rect(self.display, (0, 0, 0), self.rect)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += 1
            self.position = 'right'
        elif keys[pygame.K_a]:
            self.rect.x -= 1
            self.position = 'left'
        elif keys[pygame.K_s]:
            self.rect.y += 1
            self.position = 'down'
        elif keys[pygame.K_w]:
            self.rect.y -= 1
            self.position = 'up'
        else: 
            self.position = 'stop'

        pygame.draw.rect(self.display, self.color, self.rect)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 003] #

    def colliderect(self):

        pygame.draw.rect(self.display, (0, 0, 0), self.rect2)

        if self.rect.colliderect(self.rect2):
            if self.position == 'right':
                self.rect2.x += 1
            elif self.position == 'left':
                self.rect2.x -= 1
            elif self.position == 'down':
                self.rect2.y += 1
            elif self.position == 'up':
                self.rect2.y -= 1

        pygame.draw.rect(self.display, self.color, self.rect2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 004] #

    def update(self):

        self.moverect()
        self.colliderect()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
