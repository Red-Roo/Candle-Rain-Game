##dice_game_interface_class.py
##JacqulynMacHardy
##10-25-16

import pygame
from pygame.locals import *

class text_display(object):

    def __init__ (self, surf, text):

        self.__SURF = surf
##        INFO = pygame.display.Info()
##        dh = INFO.current_h
##        dw = INFO.current_w
##
##        print ('blech')

        self.display_text = text

        color1 = (164, 167, 255)

        TITLE_FONT_1 = pygame.font.Font("Quicksand-BoldItalic.otf", 60)
        self.__TITLE_1 = TITLE_FONT_1.render(self.display_text, True, color1, None)

    def display(self, X, Y):

        self.X = X
        self.Y = Y

        self.__SURF.blit(self.__TITLE_1, (self.X, self.Y))

##        print('bam')

