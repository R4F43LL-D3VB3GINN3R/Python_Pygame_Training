#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# [IMPORTS] #

import pygame

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Tile(pygame.sprite.Sprite):
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [OBJECTS] #
    
    def __init__(self, pos_width, pos_height, width, height, color, breath):
        super().__init__()

        self.rect = pygame.Rect(pos_width, pos_height, width, height)
        self.rect2 = pygame.Rect(pos_width + 100, pos_height + 100, width, height)
        self.color = color 
        self.breath = breath
        self.breathing = True 
        self.direction = 'stop'

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 001] #

    def breathrect(self, surface):

        pygame.draw.rect(surface, (0, 0, 0), self.rect)

        if self.breathing:
            self.breath += 1
            self.rect.width += 1
            self.rect.height += 1
            pygame.draw.rect(surface, self.color, self.rect)
            if self.breath == 30:
                self.breathing = False 
        else: 
            self.breath -= 1
            self.rect.width -= 1
            self.rect.height -= 1
            pygame.draw.rect(surface, self.color, self.rect)
            if self.breath == 0:
                self.breathing = True 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 002] #

    def moverect(self, surface):

        pygame.draw.rect(surface, (0, 0, 0), self.rect)

        key = pygame.key.get_pressed()

        if key[pygame.K_d]:
            self.rect.x += 1
            self.direction = 'right'
        elif key[pygame.K_a]:
            self.rect.x -= 1
            self.direction = 'left'
        elif key[pygame.K_s]:
            self.rect.y += 1
            self.direction = 'down'
        elif key[pygame.K_w]:
            self.rect.y -= 1
            self.direction = 'up'
        else:
            self.direction = 'stop'

        pygame.draw.rect(surface, self.color, self.rect)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 003] #

    def colliderect(self, surface):

        pygame.draw.rect(surface, (0, 0, 0), self.rect2)

        if self.rect.colliderect(self.rect2):
            if self.direction == 'right':
                self.rect2.x += 1
            elif self.direction == 'left':
                self.rect2.x -= 1
            elif self.direction == 'up':
                self.rect2.y -= 1
            elif self.direction == 'down':
                self.rect2.y += 1

        pygame.draw.rect(surface, self.color, self.rect2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 004] #

    def run(self, surface):

        self.moverect(surface)
        self.colliderect(surface)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
