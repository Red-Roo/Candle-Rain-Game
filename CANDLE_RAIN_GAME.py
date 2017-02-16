# space_ship_game.py
# MCVAN
# Spring 16

import pygame, sys
from pygame.locals import *
from bulletClass import bullet
from meteorClass import meteor
from spaceSHIPclass import spaceSHIP
from vector2class import vector2
from dice_game_interface_class import text_display
from simpleButtonClass003 import simpleButton
from random import *

space_background = 'japanBG.jpg'
space_ship_image = 'candle.jpg'
ff1 = 'force_field.tga'



pygame.init()
pygame.mixer.init()
RAIN = pygame.mixer.music.load("DesertedScraplandEntrance.mp3")
pygame.mixer.music.play(loops= -1, start = 0.0)
FPSCLOCK = pygame.time.Clock()


BULLETSPEED = 30
meteorLIST = pygame.sprite.Group()
bulletLIST = pygame.sprite.Group()
FPS = 120
DWIDTH = 1000
DHEIGHT = 550
BGscale = 2
ssSIZE = (75, 75)

Hx = DWIDTH//2
ssPOS = vector2(Hx, DHEIGHT - ssSIZE[1] - 55)
bulletSIZE = 30

BUTTONHEIGHT = 80
BUTTONWIDTH1 = 400
BUTTONWIDTH2 = 240
Bcolor = (200, 136, 250)
Tcolor = (239, 219, 255)
Btext1 = "Play Again!"


BUTTONXPOS1 = DWIDTH//2 - BUTTONWIDTH1//2 + 20
BUTTONYPOS = int(DHEIGHT * .55)

STARTspPOS = vector2(DWIDTH//2, DHEIGHT//2)
DISPLAYSURF = pygame.display.set_mode((DWIDTH, DHEIGHT), HWSURFACE | DOUBLEBUF)
BGimage = pygame.image.load(space_background).convert()
BGwidth, BGheight = BGimage.get_size()
BGwidth = BGscale * BGwidth
BGheight = BGscale * BGheight
BGimage = pygame.transform.scale(BGimage, (BGwidth, BGheight))

B1 = simpleButton(BUTTONHEIGHT, BUTTONWIDTH1, Bcolor, Tcolor, Btext1, DISPLAYSURF, (BUTTONXPOS1, BUTTONYPOS))



startTEXT = text_display(DISPLAYSURF, "Dodge the rain!")
SCORE = 0
scoreTEXT = text_display(DISPLAYSURF, str(SCORE))
gameoverTEXT = text_display(DISPLAYSURF, "GAME OVER")

ffimage = pygame.image.load(ff1).convert_alpha()

def makeMeteors():

    
    
    meteors = 10
    global SCORE

    while meteors > 0:
        randx = randrange(0, DWIDTH)
        randy = randrange(-1000, 0)
##        print (randx)

        if  not (randx > 0 and randx < DWIDTH and randy > 0 and randy < DHEIGHT):
            v1 = vector2(randx,randy)
            v2 = vector2.fromPoints((randx, randy), (randx, 450))
            v2 = v2.normalizeV2()
            meteorLIST.add(meteor(v1, DISPLAYSURF, v2, 5.0, 40))
            meteors -= 1
##            SCORE += 1


def main():

##    pygame.mixer.music.play(loops= -1, start = 0.0)
    
    ssSIZE = (75, 75)

    GAMEOVER = False
    B1.active = False

    global SCORE
    SCORE = 0

    TEMPvector = vector2.fromPoints((STARTspPOS.vX, STARTspPOS.vY), (STARTspPOS.vX + 0, STARTspPOS.vY - 10))
    TEMPvector = TEMPvector.normalizeV2()

##    SPHpos = ssPOS

    x, y = 0, 0
    Hx = DWIDTH//2
    Hy = DHEIGHT - ssSIZE[1] - 55
    Hmove_x, Hmove_y = 0, 0

    BGIxPOS = -(BGwidth - DWIDTH)//2
    BGIyPOS = -(BGheight - DHEIGHT)//2

    RIGHT = False
    LEFT = False
    UP = False
    DOWN = False

    rotationL = 0.0
    rotationR = 0.0
    spriteROT = 0.0
    RATE = 5

    hitcount = 0
    global ssSIZE
    
    #SS1 = spaceSHIP(ssPOS, ssSIZE, space_ship_image, DISPLAYSURF)
    makeMeteors()
    

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouseXY = pygame.mouse.get_pos()
                if B1.clicked(mouseXY):
                    B1.hilighted = True
                    main()

            if event.type == KEYDOWN:

##                if event.key == K_d:
##                    rotationR = - RATE
##                elif event.key == K_a:
##                    rotationL =  RATE
                if event.key == K_LEFT:
                    print("left!")
                    Hmove_x = -RATE
                    LEFT = True
                elif event.key == K_RIGHT:
                    print("right!")
                    Hmove_x = +RATE
                    RIGHT = True
                elif event.key == K_UP:
                    UP = True
                elif event.key == K_DOWN:
                    DOWN = True
                elif event.key == K_SPACE:
                    pass

            elif event.type == KEYUP:
                if event.key == K_r:
                    rotationR = 0
                elif event.key == K_w:
                    rotationL = 0
                if event.key == K_LEFT:
                    Hmove_x = 0
                    LEFT = False
                elif event.key == K_RIGHT:
                    Hmove_x = 0
                    RIGHT = False
                elif event.key == K_UP:
                    UP = False
                elif event.key == K_DOWN:
                    DOWN = False
                elif event.key == K_SPACE:
                    bulletLIST.add(bullet(ssPOS, DISPLAYSURF, vector1, BULLETSPEED, 30))
                    
        spriteROT += rotationR + rotationL

        global Hx
        global Hmove_x

        if len(meteorLIST) < 3:
            makeMeteors()

        if RIGHT:
            Hx += Hmove_x
            print("MOVE!")
        if LEFT:
            Hx += Hmove_x
            print("MOVE!")
##        if UP:
##            Hy += Hmove_y
##        if DOWN:
##            Hy += Hmove_y

        # Constrains heart to stay on screen--if statements so checks every frame
        if Hx <= 0:
            Hx = 0
##        if Hy <= 0:
##            Hy = 0
        if Hx >= DWIDTH:
            Hx = DWIDTH
##        if Hy >= DHEIGHT:
##            Hy= DHEIGHT        
        

##        if RIGHT:
##            if BGIxPOS <= -1 * (BGwidth - DWIDTH):
##                BGIxPOS = -1 * (BGwidth - DWIDTH)
##            else:
##                BGIxPOS -= RATE
##                
##        if LEFT:
##            if BGIxPOS >= 0:
##                BGIxPOS = 0
##            else:
##                BGIxPOS += RATE
##                
##        if DOWN:
##            if BGIyPOS <= -1 * (BGheight - DHEIGHT):
##                BGIyPOS = -1 * (BGheight - DHEIGHT)
##            else:
##                BGIyPOS -= RATE
##
##        if UP:
##            if BGIyPOS >= 0:
##                BGIyPOS = 0
##            else:
##                BGIyPOS += RATE
            
        DISPLAYSURF.fill((0,0,0))
        DISPLAYSURF.blit(BGimage, (BGIxPOS, BGIyPOS))

        ssPOS = vector2(Hx, DHEIGHT - ssSIZE[1] - 55)

        SS1 = spaceSHIP(ssPOS, ssSIZE, space_ship_image, DISPLAYSURF)
    

        bulletmeteorCollisions = pygame.sprite.groupcollide(meteorLIST, bulletLIST, True, True)
        meteorSScollisions = pygame.sprite.spritecollide(SS1, meteorLIST, True)

        for meteor in meteorSScollisions:
            hitcount += 1
            if hitcount == 1:
                ssSIZE = (50, 50)
            elif hitcount == 2:
                ssSIZE = (0,0)
                GAMEOVER = True
                

        for BX in bulletLIST:
            if BX.rect.x > 0 and BX.rect.y > 0 and BX.rect.x< DWIDTH and BX.rect.y < DHEIGHT:
                pass #BX.displayBullet()
            else:
                bulletLIST.remove(BX)
                
        for MX in meteorLIST:
            if MX.rect.x < DWIDTH and MX.rect.y < DHEIGHT:
                MX.displayMeteor()
            else:
                meteorLIST.remove(MX)
                if GAMEOVER == True:
                    SCORE += 0
                else:
                    SCORE += 1
                    print (SCORE)
    
        #DISPLAYSURF.blit(ffimage, (DWIDTH//2 - 200, DHEIGHT//2 - 200))
        SS1.rotateSS(spriteROT)
        vector1 = TEMPvector.rotateV2(-spriteROT)
        SS1.displaySpaceSHIP()
        text_display.display(startTEXT, 300, 440)
        scoreTEXT = text_display(DISPLAYSURF, str(SCORE))
        text_display.display(scoreTEXT, 475, 485)

        if GAMEOVER == True:
            text_display.display(gameoverTEXT, 340, 220)
            B1.active = True
            B1.display()
            
        
        FPSCLOCK.tick(FPS)

        pygame.display.update()

if __name__ == '__main__': main()

