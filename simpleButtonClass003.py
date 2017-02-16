# simpleButtonClass003.py

import pygame
from pygame.locals import *

class simpleButton:

    # class that creates button objects

    def __init__(self, height, width, color, textColor, label, surf, position):

        # define some values

        self.__SURF = surf
        self.POS = position
        self.BUTCOLOR  = color
        self.HIGHLIGHTCOLOR = (color[0] + ((255 - color[0])//3),
                               color[1] + ((255 - color[1])//3),
                               color[2] + ((255 - color[2])//3))
                               
        self.TEXTCOLOR = textColor

        self.HEIGHT   = height
        self.WIDTH  = width
        self.__RADIUS   = self.HEIGHT//2
        THEIGHT  = int(self.HEIGHT * .72)

        self.active = True
        self.hilighted = False

        BUTFONT = pygame.font.Font("ScriptinaPro.ttf", THEIGHT)
        # Render a Text Surface
        self.TEXT__SURF = BUTFONT.render(label, True, textColor, None)

        w, h   = self.TEXT__SURF.get_size()
        
        self.XPOS   = (self.WIDTH - w)//2
        self.YPOS   = int((self.HEIGHT - h)//2)

        self.__BUTTON__SURF = pygame.Surface((self.WIDTH, self.HEIGHT), flags=SRCALPHA, depth=32)
        self.__BUTTON__SURF.fill((0, 0, 0, 0))


    def __buttonBG(self, color):

        # create square with rounded corners
       
        pygame.draw.circle(self.__BUTTON__SURF, color, (self.__RADIUS, self.__RADIUS),
                           self.__RADIUS)
        pygame.draw.circle(self.__BUTTON__SURF, color,
                           (self.WIDTH - self.__RADIUS, self.__RADIUS), self.__RADIUS)

        pygame.draw.rect(self.__BUTTON__SURF, color,  Rect((self.__RADIUS, 0), (self.WIDTH - 2 * self.__RADIUS, self.HEIGHT)))


    def __buttonText(self):

        # Draw Text
        self.__BUTTON__SURF.blit(self.TEXT__SURF, (self.XPOS, self.YPOS))


    def clicked(self, MOUSEXY):
        
        yesORno = False
        P1 = self.POS
        P2 = (P1[0] + self.WIDTH, P1[1] + self.HEIGHT)
        yesORno = (self.active and P1[0] <= MOUSEXY[0] <= P2[0] and
                   P1[1] <= MOUSEXY[1] <= P2[1])

        return yesORno


    def display(self):
        
        if self.active:
            if self.hilighted:
                self.__buttonBG(self.HIGHLIGHTCOLOR)
                self.__buttonText()
                self.__SURF.blit(self.__BUTTON__SURF, self.POS)
            else:
                self.__buttonBG(self.BUTCOLOR)
                self.__buttonText()
                self.__SURF.blit(self.__BUTTON__SURF, self.POS)

        

       
