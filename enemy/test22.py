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
import pytmx

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
enemie_animation = [ceena, ceena1, ceena2]

##button
E_button = pygame.image.load('texture/PSD/button_E.png')

####----------------------------------------------------------------------------------------------------------------------------####


clock = pygame.time.Clock() 

from pygame.locals import * 
pygame.init()
display.set_caption('WhatTheFrog') 
WINDOW_SIZE = (720, 480) 
screen = display.set_mode(WINDOW_SIZE,0,32)
mouse.set_visible(False)


#crosshair 
crosshair_rect = crosshair_image.get_rect()
###

#image size
TILE_SIZE = 32
sign_pos = [(32, 11), (3, 31), (22, 50)]
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
        screen.blit(enemie_animation[int(self.animation)], (self.rect.x - smscroll[0], self.rect.y - smscroll[1]))
###

#Bullet and shoot
class Bullet():
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.lifetime = 90
        self.speed = 18
        self.angle = math.atan2(mouse_y - 240 + middle_y - TILE_SIZE/2, mouse_x - 360 + middle_x - TILE_SIZE/2 + 16)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.radius = 6
        self.rect = Rect(self.x - 5, self.y - 5, 10, 10)

    def draw(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        draw.circle(screen, (0, 204, 102), (self.x - scroll[0], self.y - scroll[1]), self.radius)
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

    def draw(self):
        draw.rect(screen, (0, 0, 0), self.rect)
        if player_rect.colliderect(self.rect):
            checkpoint_pos[0] = self.rect.x
            checkpoint_pos[1] = self.rect.y
        #screen.blit(checkpoint_image, (self.rect.x - smscroll[0], self.rect.y - smscroll[1]))

checkpoint_rect = []
for rect in sign_rect:
    checkpoint_rect.append(checkpoint(rect.x/TILE_SIZE, rect.y/TILE_SIZE))

checkpoint_pos = [0 * TILE_SIZE, 9 * TILE_SIZE]
###

#load map
gameMap = pytmx.load_pygame('tilemap/test11.tmx')
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
enemies_pos = [(23, 8), (14, 19), (11, 32)]
y = 0
tile_rects = []
for layer in gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = gameMap.get_tile_image_by_gid(gid) 
                if(tile != None):
                    tile_rects.append(Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
for pos in enemies_pos:
    enemies_rects.append(Enemies(pos))
###
sm_x = 9
sm_y = 9
test = None
while True: 
    #print(player_rect.x, player_rect.y)

    ###fps
    clock.tick(60)

    #mouse input
    mouse_x, mouse_y = mouse.get_pos()
    ###

    #set bool
    onclick = False
    shoot = False
    ###

    #key
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == MOUSEBUTTONDOWN:
            onclick = True
            shoot = True
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
    if mouse_x < 360 + TILE_SIZE:
        middle_x = -55
    else:
        middle_x = 55
    if mouse_y < 240 + TILE_SIZE :
        middle_y = -40
    else:
        middle_y = 40
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

    #draw tile
    for layer in gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = gameMap.get_tile_image_by_gid(gid)
                if(tile != None):
                    screen.blit(tile, (x * gameMap.tilewidth - smscroll[0], y * gameMap.tileheight - smscroll[1]))
        
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
            screen.blit(show_sign, (450, 240))
    elif player_rect.colliderect(sign_rect[1]):
        if Reaction:
            screen.blit(show_sign, (450, 240))
    elif player_rect.colliderect(npc_rect):
        screen.blit(E_button, (npc_rect.x + (1 * TILE_SIZE) - smscroll[0], npc_rect.y - (1 * TILE_SIZE) +(TILE_SIZE - E_button.get_height()) - smscroll[1]))
        if Reaction:
            screen.blit(npc1_text, (npc_rect.x+npc1.get_width() - smscroll[0], npc_rect.y-npc1.get_height()-8 - smscroll[1]))
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
        check.draw()

    #draw enemies
    for enemy in enemies_rects:
        for bullet in Bullets:
            if bullet.rect.colliderect(enemy.rect):
                enemy.life -= 1
        enemy.rect, enemy_collisions = move(enemy.rect, enemy.movement, tile_rects)
        if enemy.life == 0:
            enemies_rects.remove(enemy)
        enemy.draw()
    ###

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
    if shoot:
        Bullets.append(Bullet(player_rect.x + player_image.get_width()/2, player_rect.y + player_image.get_height()/2, mouse_x, mouse_y))

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

    ###

    #draw crosshair
    screen.blit(crosshair_image, (mouse_x - crosshair_image.get_width()/2, mouse_y - crosshair_image.get_height()/2 ))
    ###

    display.flip()
