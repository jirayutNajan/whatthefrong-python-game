import pygame, sys

from pygame import mouse
from pygame import draw
from pygame import transform
from pygame import image
from pygame import display
import texture
import math

clock = pygame.time.Clock() 



from texture import *
from pygame.locals import * 
pygame.init()
display.set_caption('WhatTheFrog') 
WINDOW_SIZE = (800, 400) 
screen = display.set_mode(WINDOW_SIZE,0,32)
Display = pygame.Surface((400, 200))

class bullet(object):
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.lifetime = 90
        self.speed = 10
        self.anglex = (mouse_x - self.x)/10
        self.angley = (mouse_y - self.y)/10
        self.radius = 3
        self.rect = Rect(self.x - 5, self.y - 5, 10, 10)

    def draw(self):
        self.x += self.anglex
        self.y += self.angley
        draw.circle(Display, (0, 204, 102), (self.x , self.y ), self.radius)
        self.lifetime -= 1        
bullets = []
onclick = False
while True:
    Display.fill((0, 0, 0))
    draw.rect(Display, (0, 255, 0), (10, 10, 10 ,10))
    mouses = mouse.get_pos()
    #draw bullet
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == MOUSEBUTTONDOWN:
            onclick = True
    if onclick:
        bullets.append(bullet(200, 100, mouses[0]/2, mouses[1]/2))

    for Bullet in bullets:
        if Bullet.lifetime <= 0:
            bullets.remove(Bullet)
        Bullet.draw()
    ###

    surf = transform.scale(Display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    display.flip()
    display.flip()
