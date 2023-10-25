import os
import pygame, sys

from pygame import mouse
from pygame import draw
from pygame import transform
from pygame import image
from pygame import display
from pygame import font
import math
import random

import pygame
from pygame import transform

####-------------------------------------------------------------image-----------------------------------------------------------------####
#castle 
castle_image = pygame.image.load('texture/castletest.png')

#background
background_image = pygame.image.load('texture/2 Background/back.png')
background2_image = pygame.transform.scale(pygame.image.load('texture/2 Background/Layers/3.png'), (180, 120))
background3_image = pygame.transform.scale(pygame.image.load('texture/2 Background/Layers/4.png'), (180, 120))

#Tree
tree1 = pygame.image.load('texture/3 Objects/Willows/1.png')
tree2 = pygame.image.load('texture/3 Objects/Willows/2.png')
tree3 = pygame.image.load('texture/3 Objects/Willows/3.png')

show_sign = pygame.image.load('texture/PSD/sign.png')
sign = pygame.transform.scale(pygame.image.load('texture/PSD/sign.png'), (32, 32))

npc1 = pygame.transform.scale(pygame.image.load('texture/PSD/npc1.png'), (28, 40))
npc1.set_colorkey((255, 255, 255))
npc1 = pygame.transform.flip(npc1, True, False)
npc1_text = pygame.transform.scale(pygame.image.load('texture/PSD/npc1_text.png'), (320, 60))

#player
player_image = pygame.transform.scale(pygame.image.load('player/animations/0.png'), (32, 32))
player_jump_image = pygame.transform.scale(pygame.image.load('player/animations/frogjump.png'), (32, 32))

#crsoohiar
crosshair_image = pygame.transform.scale(pygame.image.load('texture/PSD/crosshair.png'), (32, 32))

player_animations = [pygame.transform.scale(pygame.image.load('player/animations/0.png'), (32, 32)),
                    pygame.transform.scale(pygame.image.load('player/animations/1.png'), (32, 32)),
                    pygame.transform.scale(pygame.image.load('player/animations/2.png'), (32, 32)),
                    pygame.transform.scale(pygame.image.load('player/animations/3.png'), (32, 32)),
                    pygame.transform.scale(pygame.image.load('player/animations/4.png'), (32, 32)),
                    pygame.transform.scale(pygame.image.load('player/animations/5.png'), (32, 32)),
                    pygame.transform.scale(pygame.image.load('player/animations/6.png'), (32, 32))]

ceena = pygame.transform.scale(pygame.image.load('enemy/enemy.jpg'), (32, 32))
ceena1 = pygame.transform.scale(pygame.image.load('enemy/enemy1.jpg'), (32, 32))
ceena2 = pygame.transform.scale(pygame.image.load('enemy/enemy2.jpg'), (32, 32))
enemy_animation = [ceena, ceena1, ceena2]
boss_image = pygame.image.load('enemy/boss1.png')

tile_img = []
for num in range(56):
    num += 1
    tile_img.append(pygame.image.load('texture/1 Tiles/Tile_'+str(num)+'.png'))

##button
E_button = pygame.image.load('texture/PSD/button_E.png')

###menu
menu_background_img = pygame.image.load('menu/menu_background.png')

##ICON
ICON = pygame.image.load('ICON.ico')

####---------------------------------------------------------------image-------------------------------------------------------------####


clock = pygame.time.Clock() 

from pygame.locals import * 
pygame.init()
pygame.font.init()
display.set_caption('WhatTheFrog') 
WINDOW_SIZE = (720, 480) 
screen = display.set_mode(WINDOW_SIZE,0,32)
display.set_icon(ICON)

###fonts
fonts = font.Font('font/8514oem.fon', 24)
fonts_2 = font.Font('font/8514oem.fon', 150)
#end font
End_font = font.SysFont('Arial', 100)
end_text = End_font.render('The End', 'arial', (0, 0, 0))

#load map
game_Map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,9,0,0,0,0,0,0,0,0,0,7,8,8,9,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,7,8,8,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,9],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,3],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,4,23,0,0,0,0,0,1,26,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,4,22,22,23,0,0,0,0,0,0,11,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,13,0,0,0,0,0,0,0,0,0,11,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,13,0,0,0,0,0,0,0,0,0,11,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,12,12,4,22,23,0,0,0,0,0,0,0,0,1,26,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,12,4,23,0,0,0,0,0,0,0,0,0,1,26,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,4,23,0,0,0,0,0,0,0,0,0,1,26,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,13,0,0,0,0,0,0,0,0,0,0,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,13,8,9,9,9,9,9,0,0,0,0,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,13,0,0,0,0,0,0,0,0,0,0,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,4,23,0,0,0,0,0,0,0,0,0,1,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,4,23,0,0,0,0,0,0,0,0,0,1,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,13,0,0,0,0,0,0,0,0,1,2,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,4,23,0,0,0,0,0,0,1,2,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,4,22,22,22,23,0,0,0,0,0,0,1,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,21,6,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,21,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,6,12,12,12,12,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,21,6,12,12,12,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,12,12,12,13],
            [11,24,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,21,6,12,12,13],
            [11,12,12,12,12,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,21,22,6,13],
            [11,12,12,12,12,24,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,24,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,24,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,24,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,24,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,24,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,24,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,24,3,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,24,2,2,3,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,4,53,33,33,34,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,4,22,22,22,22,22,23,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,4,22,22,22,22,22,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,12,12,12,12,12,12,12,12,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,11,13],
            [11,12,12,12,12,12,12,12,12,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,4,22,22,22,22,22,22,22,23,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [11,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,11,13],
            [38,23,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,31,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,13],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,21,44],
            [55,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,31,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55],
            [36,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,46],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13],
            [21,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,23]]
###

def game():
    global castle_image, background3_image, background2_image, background_image, tree1, tree2, tree3, show_sign, sign, npc1
    global npc1_text, player_image, player_jump_image, crosshair_image, player_animations, enemy_animation, boss_image, E_button

    #image size
    TILE_SIZE = 32
    sign_pos = [(32, 11), (3, 31), (22, 50), (16, 74), (12, 83), (31, 90)]
    #sign
    sign_rect = []
    for pos in sign_pos:
        sign_rect.append(Rect(pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    npc_rect = Rect(2 * TILE_SIZE + (TILE_SIZE - npc1.get_width()), 11 * TILE_SIZE + (TILE_SIZE - npc1.get_height() + 1), 28, 40)
    ###

    ##enemies
    class Enemies():
        def __init__(self, pos):
            self.pos = pos
            self.life = 5
            self.pos = pos
            self.rect = Rect(self.pos[0] * TILE_SIZE, self.pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            self.animation = 0
            self.speed = 6
            self.movement = [0, 0]
            self.place = Rect(self.pos[0] * TILE_SIZE - 340, self.pos[1] * TILE_SIZE - 180, TILE_SIZE + 680, TILE_SIZE + 360)
        
        def draw(self):
            self.movement = [0, 0]
            self.animation += 0.02
            self.player_x = player_rect.x
            self.player_y = player_rect.y
            if self.animation > 3:
                self.animation = 0
            if player_rect.colliderect(self.place):
                self.angle = math.atan2(self.player_y - self.rect.y, self.player_x - self.rect.x)
                self.x_vel = math.cos(self.angle) * self.speed
                self.y_vel = math.sin(self.angle) * self.speed
                self.movement[0] += self.x_vel
                self.movement[1] += self.y_vel
                self.place.x = self.rect.x - 340
                self.place.y = self.rect.y - 180
            draw.rect(screen, (255, 0 ,0), (self.rect.x - smscroll[0] + 2.5, self.rect.y - smscroll[1] - 5, 30 ,2))
            draw.rect(screen, (0, 255 ,0), (self.rect.x - smscroll[0] + 2.5, self.rect.y - smscroll[1] - 5, self.life*6, 2))
            screen.blit(enemy_animation[int(self.animation)], (self.rect.x - smscroll[0], self.rect.y - smscroll[1]))
    ###

    ##boss
    class boss():
        def __init__(self, pos):
            super(boss, self).__init__()
            self.x = pos[0]
            self.y = pos[1]
            self.rect = Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE * 3, TILE_SIZE * 3)
            self.speed = 2.5
            self.ball_speed = 10
            self.life = 20
            self.place = Rect(self.x * TILE_SIZE - 640 +48, self.y * TILE_SIZE - 400 +48, TILE_SIZE + 1280, TILE_SIZE + 800)
            self.ball_x = self.rect.x - 48
            self.ball_y = self.rect.y - 48
            self.time = 0

        def draw(self):
            if player_rect.colliderect(self.place):
                self.angle = math.atan2(player_rect.y - self.rect.y, player_rect.x - self.rect.x)
                self.x_vel = math.cos(self.angle) * self.speed
                self.y_vel = math.sin(self.angle) * self.speed
                self.rect.x += self.x_vel
                self.rect.y += self.y_vel
                self.place.x = self.rect.x - 640 + 48
                self.place.y = self.rect.y - 400 + 48
                self.time += 1
                if self.time >= 100:
                    self.time = 0
                test = self.time % 50
                if test == 0:
                    boss_Bullets.append(Bullet(self.rect.x + 48, self.rect.y + 48, player_rect.x + 16 - self.rect.x -48, 
                        player_rect.y + 16 - self.rect.y -48, 10, (255, 0, 0)))
            draw.rect(screen, (255, 0 ,0), (self.rect.x - smscroll[0], self.rect.y - smscroll[1] - 7, 96 ,4)) #hp
            draw.rect(screen, (0, 255 ,0), (self.rect.x - smscroll[0], self.rect.y - smscroll[1] - 7, self.life*4.8, 4)) #hp
            screen.blit(boss_image, (self.rect.x - smscroll[0], self.rect.y - smscroll[1]))

    boss_pos = [(25, 107)]
    boss_rect = []
    for pos in boss_pos:
        boss_rect.append(boss(pos))
    ###

    boss_Bullets = [] ##boss bullet

    #Bullet and shoot
    class Bullet():
        def __init__(self, x, y, input_x, input_y, size, color):
            self.x = x
            self.y = y
            self.color = color
            self.lifetime = 90
            self.speed = 18
            self.angle = math.atan2(input_y, input_x)
            self.x_vel = math.cos(self.angle) * self.speed
            self.y_vel = math.sin(self.angle) * self.speed
            self.radius = size
            self.rect = Rect(self.x - 5, self.y - 5, 10, 10)

        def draw(self):
            self.x += self.x_vel
            self.y += self.y_vel
            self.rect.x += self.x_vel
            self.rect.y += self.y_vel
            draw.circle(screen, (self.color), (self.x - scroll[0], self.y - scroll[1]), self.radius)
            self.lifetime -= 1        

    Bullets = []
    ###

    ##chekpoint
    class checkpoint():
        def __init__(self, x, y):
            super(checkpoint, self).__init__()
            self.x = x
            self.y = y
            self.rect = Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

        def update(self):
            if player_rect.colliderect(self.rect):
                checkpoint_pos[0] = self.rect.x
                checkpoint_pos[1] = self.rect.y
            #screen.blit(checkpoint_image, (self.rect.x - smscroll[0], self.rect.y - smscroll[1]))

    checkpoint_rect = []
    for rect in sign_rect:
        checkpoint_rect.append(checkpoint(rect.x/TILE_SIZE, rect.y/TILE_SIZE))

    checkpoint_pos = [0 * TILE_SIZE, 9 * TILE_SIZE]
    ###


    #การชนและการขยับกล้อง
    def collision_test(rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types
    ###

    #setplayer
    moving_right = False
    moving_left = False
    #set gravity and jump
    player_y_momentum = 0
    air_timer = 0
    life = 1

    step = 0 #set player animation
    right = True

    player_rect = Rect(checkpoint_pos[0], checkpoint_pos[1], player_image.get_width(), player_image.get_height())

    #scroll map
    scroll = [0, 0]
    bgsc = 0 #bg scrolling
    middle_x = 0
    middle_y = 0

    enemies_rects = []
    enemies_pos = [(23, 8), (14, 19), (11, 32), (25, 38), (18, 59), (29, 38)]
    for pos in enemies_pos:
        enemies_rects.append(Enemies(pos))

    y = 0
    tile_rects = []
    for row in game_Map:
        x = 0
        for tile in row:
            if tile != 0:
                tile_rects.append(Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    ###
    sm_x = 9
    sm_y = 9
    End = False

    mouse.set_visible(False)
    while True: 
        #print(player_rect.x/TILE_SIZE, player_rect.y/TILE_SIZE)
    
        ###fps
        clock.tick(60)

        #mouse input
        mouse_x, mouse_y = mouse.get_pos()
        ###

        #set bool
        onclick = False
        ###

        #key
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit() 
            if event.type == MOUSEBUTTONDOWN:
                onclick = True
            if event.type == KEYDOWN:
                if event.key == K_d:
                    moving_right = True
                if event.key == K_a:
                    moving_left = True
                if event.key == K_SPACE:
                    if air_timer < 8 :
                        player_y_momentum = -12
                if event.key == K_e:
                    Reaction = True
            if event.type == KEYUP:
                if event.key == K_d:
                    moving_right = False
                if event.key == K_a:
                    moving_left = False
                if event.key == K_q:
                    shoot = True

        ###
        #scroll
        angle = math.atan2(mouse_y - 240 +middle_y - TILE_SIZE/2, mouse_x - 360 +middle_x - TILE_SIZE/2 + 16)
        x_vel = math.cos(angle) * 80
        y_vel = math.sin(angle) * 80
        middle_x = x_vel
        middle_y = y_vel
        scroll[0] += (player_rect.x+middle_x-scroll[0]+18 - 360)/sm_x
        scroll[1] += (player_rect.y+middle_y-scroll[1] - 240)/sm_y
        smscroll = scroll.copy()
        smscroll[0] = int(scroll[0])
        smscroll[1] = int(scroll[1])
        ###
    
        #backgroud
        screen.fill((83, 146, 131))
        screen.blit(transform.scale(background2_image, (720, 480)), (0, 0))
        screen.blit(transform.scale(background3_image, (720, 480)), (0, 0))
        ###

        ####game map
        y = 0
        for row in game_Map:
            x = 0
            for tile in row:
                if tile != 0:
                    screen.blit(tile_img[tile-1], (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
                x += 1
            y += 1
        ###

        #draw another object

        #draw castle 
        castle_rect = Rect(-200, 160, 200, 500)
        screen.blit(castle_image, (castle_rect.x - smscroll[0], castle_rect.y - smscroll[1]))
        tile_rects.append(castle_rect)
        Right_edge_rect =  Rect(1120, 120, 200, 800)
        tile_rects.append(Right_edge_rect)
        ###

        #draw tree
        screen.blit(tree1, (4 * TILE_SIZE + (TILE_SIZE - tree1.get_width()) - smscroll[0], 11 * TILE_SIZE + (TILE_SIZE - tree1.get_height()) - smscroll[1]))

        #collide another objects
        for rect in sign_rect:
            if player_rect.colliderect(rect):
                screen.blit(E_button, (rect.x +(TILE_SIZE) - smscroll[0], rect.y -(TILE_SIZE) +(TILE_SIZE - E_button.get_height()) - smscroll[1]))

        if player_rect.colliderect(sign_rect[0]):
            if Reaction:
                sign_str = fonts.render('contruction zone pls turn back', True, (255, 0, 0))
                sign_str2 = fonts.render('Remember!!!!', True, (255, 0, 0))
                sign_str3 = fonts.render('Sign = checkpoint', True, (255, 0, 0))
                screen.blit(show_sign, (450, 240))
                screen.blit(sign_str, (452, 250))
                screen.blit(sign_str2, (452, 280))
                screen.blit(sign_str3, (452, 310))
        elif player_rect.colliderect(sign_rect[1]):
            if Reaction:
                sign_str = fonts.render('GO RIGHT DOWN', True, (255, 0, 0))
                screen.blit(show_sign, (450, 240))
                screen.blit(sign_str, (505, 250))
        elif player_rect.colliderect(npc_rect):
            screen.blit(E_button, (npc_rect.x + (1 * TILE_SIZE) - smscroll[0], npc_rect.y - (1 * TILE_SIZE) +(TILE_SIZE - E_button.get_height()) - smscroll[1]))
            if Reaction:
                font_npc_text = font.Font('font/8514oem.fon', 30)
                text = font_npc_text.render('Left click for shoot john4na', True, (0, 0, 0))
                screen.blit(npc1_text, (npc_rect.x+npc1.get_width() - smscroll[0], npc_rect.y-npc1.get_height()-8 - smscroll[1]))
                screen.blit(text, (npc_rect.x+npc1.get_width()+25 - smscroll[0], npc_rect.y-npc1.get_height()+10 - smscroll[1]))
        else:
            Reaction = False

        #draw sign
        for pos in sign_pos:
            screen.blit(sign, (pos[0]*TILE_SIZE - smscroll[0], pos[1]*TILE_SIZE - smscroll[1]))
        #draw npc
        screen.blit(npc1, (2 * TILE_SIZE + (TILE_SIZE - npc1.get_width()) - smscroll[0], 11 * TILE_SIZE + (TILE_SIZE - npc1.get_height() + 1) - smscroll[1]))
        ###

        ##checkpoint = sign
        for check in checkpoint_rect:
            check.update()

        #draw enemies
        for enemy in enemies_rects:
            if enemy.rect.y < checkpoint_pos[1] - 3 * TILE_SIZE:
                enemies_rects.remove(enemy)        
            for bullet in Bullets:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.life -= 1
            enemy.rect, enemy_collisions = move(enemy.rect, enemy.movement, tile_rects)
            if enemy.life <= 0:
                enemies_rects.remove(enemy)
            enemy.draw()
        ###

        ##draw boss
        for Boss in boss_rect:
            for bullet in Bullets:
                if bullet.rect.colliderect(Boss.rect):
                    Boss.life -= 1
                    bullet.lifetime = 0
            if Boss.rect.colliderect(player_rect):
                life = 0
            if Boss.life <= 0:
                End = True
                boss_rect = []
            Boss.draw()
        if End:
            end_screen()
        ####

        player_movement = [0, 0]
        if moving_right:
            player_movement[0] += 5
            bgsc += 0.2
            step += 0.3
            right = True
        elif moving_left:
            player_movement[0] -= 5
            bgsc -= 0.2
            step += 0.3
            right = False 
        else:
            step = 0
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.6
        if player_y_momentum > 6:
            player_y_momentum = 6
    
        player_rect, collisions = move(player_rect, player_movement, tile_rects)

        if collisions['top']:
            player_y_momentum += 10
        if collisions['bottom']:
            player_y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1

        #draw Bullet
        if onclick:
            Bullets.append(Bullet(player_rect.x + player_image.get_width()/2, player_rect.y + player_image.get_height()/2, 
                mouse_x - 360 + middle_x - TILE_SIZE/2 + 16, mouse_y - 240 + middle_y - TILE_SIZE/2, 6, (0, 204, 102)))

        for bullet in Bullets:
            for tile in tile_rects:
                if bullet.rect.colliderect(tile):
                    bullet.lifetime = 0
            for enemy in enemies_rects:
                if bullet.rect.colliderect(enemy.rect):
                    bullet.lifetime = 1
            if bullet.lifetime <= 0:
                Bullets.remove(bullet)
            bullet.draw()
        ###

        ##draw boss bullet
        for bullet in boss_Bullets:
            for rect in tile_rects:
                if bullet.rect.colliderect(rect):
                    bullet.lifetime = 0
            if bullet.lifetime <= 0:
                boss_Bullets.remove(bullet)
            if bullet.rect.colliderect(player_rect):
                boss_Bullets = []
                life = 0
            bullet.draw()
        ### 

        #draw player 
        player_image = player_animations[int(step)]
        if mouse_x/2 < 185 :
            right = False
        else:
            right = True
        if right == False:
            player_image = transform.flip(player_image, True, False)
        if step > 6:
            step = 0
        #jump animation
        if air_timer > 5 and air_timer <= 60 or air_timer > 60:
            if right == False:
                player_image = transform.flip(player_jump_image, True, False)
            else:
                player_image = player_jump_image
        else:
            player_image = player_image

        ###
        screen.blit(player_image, (player_rect.x - smscroll[0], player_rect.y - smscroll[1]))
    
        for enemy in enemies_rects:
            if player_rect.colliderect(enemy):
                enemies_rects.remove(enemy)
                life = 0
                enemies_rects = []
                for pos in enemies_pos:
                    enemies_rects.append(Enemies(pos))
        ###if player die
        if life == 0: #if fall out
            player_rect.y = checkpoint_pos[1]
            player_rect.x = checkpoint_pos[0]
            life = 1
            enemies_rects = []
            for pos in enemies_pos:
                enemies_rects.append(Enemies(pos))
            boss_rect = []
            for pos in boss_pos:
                boss_rect.append(boss(pos))

        ###
        #draw crosshair
        screen.blit(crosshair_image, (mouse_x - crosshair_image.get_width()/2, mouse_y - crosshair_image.get_height()/2 ))
        ###

        display.update()

def end_screen():
    mouse.set_visible(True)

    #button color
    play_color = (23, 71, 56)
    quit_clolor = (45, 120, 75)

    while True:
        onclick = False
        mouse_x, mouse_y = mouse.get_pos()
        
        ##event
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                onclick = True
        ###

        ###play button
        play = Rect(210, 250, 300, 80)
        draw.rect(screen, (play_color), play)
        ###

        ##quit button
        quit_ = Rect(260, 350, 200, 50)
        draw.rect(screen, (quit_clolor), quit_)
        ###

        ###text
        txt = End_font.render('The End', True, (0, 0, 0))
        txt_play = fonts_2.render('Play again', True, (0, 0, 0))
        txt_quit = fonts_2.render('Quit', True, (0, 35, 23))
        screen.blit(txt, (200, 100))
        screen.blit(txt_play, (310, 280))
        screen.blit(txt_quit, (340, 365))
        ###


        if play.collidepoint(mouse_x, mouse_y):
            play_color = (30, 75, 60)
            if onclick:
                game()
        else:
            play_color = (23, 71, 56)
        if quit_.collidepoint(mouse_x, mouse_y):
            quit_clolor = (55, 130, 85)
            if onclick:
                pygame.quit()
                sys.exit()
        else:
            quit_clolor = (45, 120, 75)
        ####
        
        display.flip()

def menu():
    mouse.set_visible(True)

    #button color
    play_color = (23, 71, 56)
    quit_clolor = (45, 120, 75)

    while True:
        screen.blit(menu_background_img, (0, 0))
        onclick = False
        mouse_x, mouse_y = mouse.get_pos()
        
        ##event
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                onclick = True
        ###

        ###play button
        play = Rect(210, 250, 300, 80)
        draw.rect(screen, (play_color), play)
        ###

        ##quit button
        quit_ = Rect(260, 350, 200, 50)
        draw.rect(screen, (quit_clolor), quit_)
        ###

        ###text
        txt = End_font.render('WhatTheFrog', True, (0, 0, 0))
        txt_play = fonts_2.render('Play', True, (0, 0, 0))
        txt_quit = fonts_2.render('Quit', True, (0, 35, 23))
        screen.blit(txt, (100, 100))
        screen.blit(txt_play, (340, 280))
        screen.blit(txt_quit, (340, 365))
        ###


        if play.collidepoint(mouse_x, mouse_y):
            play_color = (30, 75, 60)
            if onclick:
                game()
        else:
            play_color = (23, 71, 56)
        if quit_.collidepoint(mouse_x, mouse_y):
            quit_clolor = (55, 130, 85)
            if onclick:
                pygame.quit()
                sys.exit()
        else:
            quit_clolor = (45, 120, 75)
        ####
        
        display.update()

menu()