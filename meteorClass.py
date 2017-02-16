## meteorClass.py
## MCVAN
## Fall 15

import pygame, sys
from pygame.locals import *
from vector2class import vector2
from math import *


class meteor(pygame.sprite.Sprite):


    def __init__(self, pos, surf, vector, speed, size):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.SURF = surf
        self.SIZE = size
        self.POS = pos
        self.VECTOR = vector
        self.SPEED = speed

        self.image = pygame.Surface((self.SIZE,self.SIZE), flags=SRCALPHA, depth=32)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos.vX
        self.rect.y = pos.vY

        self.HSIZE = self.SIZE//2

        self.met = pygame.image.load("raindrop.gif-c200").convert_alpha()
        self.met = pygame.transform.scale(self.met, (self.SIZE, self.SIZE))
        self.image.blit(self.met, (0, 0))


    def resizeSQ(self, x, y, xPOS, yPOS):
        # Resizes a Square on x-width and y-height sides
        self.image = pygame.transform.scale(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = xPOS
        self.rect.y = yPOS


    def __moveMeteor(self, pos, vec, speed):

        pos += vec * speed

        return pos


    def __changePOS(self, pos):

        self.POS = vector2(pos.vX, pos.vY)
        self.rect.x = pos.vX
        self.rect.y = pos.vY


    def displayMeteor(self):
        
        self.__changePOS(self.__moveMeteor(self.POS, self.VECTOR, self.SPEED))
        self.SURF.blit(self.image, (self.POS.vX - self.HSIZE, self.POS.vY - self.HSIZE))
