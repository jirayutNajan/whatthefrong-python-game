import pygame, sys

from pygame import mouse
from pygame import draw
from pygame import transform
from pygame import image
from pygame import display
import texture
import math
import random
import pytmx

clock = pygame.time.Clock() 

from texture import *
from pygame.locals import * 
pygame.init()
display.set_caption('WhatTheFrog') 
WINDOW_SIZE = (800, 400) 
screen = display.set_mode(WINDOW_SIZE,0,32)
Display = pygame.Surface((400, 200))
mouse.set_visible(False)


#crosshair 
crosshair_rect = crosshair_image.get_rect()
###

#image size
TILE_SIZE = dirt_image.get_width()
###

##enemies
class Enemies():
    def __init__(self, pos):
        self.pos = pos
        self.life = 10
        self.pos = pos
        self.rect = Rect(self.pos[0] * TILE_SIZE, self.pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.animation = 0
        self.speed = 2
        self.movement = [0, 0]
        
    def draw(self):
        self.movement = [0, 0]
        self.animation += 0.02
        self.player_x = player_rect.x
        self.player_y = player_rect.y
        if self.animation > 3:
            self.animation = 0
        if (self.rect.x - self.player_x) < 200:
            self.angle = math.atan2(self.player_y - self.rect.y, self.player_x - self.rect.x)
            self.x_vel = math.cos(self.angle) * self.speed
            self.y_vel = math.sin(self.angle) * self.speed
            self.movement[0] += self.x_vel
            self.movement[1] += self.y_vel
        draw.rect(Display, (255, 0 ,0), (self.rect.x - smscroll[0] + 2.5, self.rect.y - smscroll[1] - 5,15 ,2))
        draw.rect(Display, (0, 255 ,0), (self.rect.x - smscroll[0] + 2.5, self.rect.y - smscroll[1] - 5,self.life/0.6 ,2))
        Display.blit(enemie_animation[int(self.animation)], (self.rect.x - smscroll[0], self.rect.y - smscroll[1]))
###

#Bullet and shoot
class Bullet():
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.lifetime = 90
        self.speed = 7
        self.angle = math.atan2(mouse_y - 105 + middle_y, mouse_x - 200 + middle_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.radius = 3
        self.rect = Rect(self.x - 5, self.y - 5, 10, 10)

    def draw(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        draw.circle(Display, (0, 204, 102), (self.x - scroll[0], self.y - scroll[1]), self.radius)
        self.lifetime -= 1        

Bullets = []
###

#load map
def loadmap(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map
game_map = loadmap('map')
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

player_rect = Rect(0, 100, player_image.get_width(), player_image.get_height())

#scroll map
scroll = [0, 0]
bgsc = 0 #bg scrolling
sm = 10 #scroll look good
middle_x = 0
middle_y = 0

enemies_rects = []    #enemies rect
#adds enemies
enemies_pos = []
y = 0
tile_rects = []
for row in game_map:
        x = 0
        for tile in row:
            if tile == 'E':
                enemies_pos.append((x, y))
            if tile != '0' and tile != 'E':
                tile_rects.append(Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
for pos in enemies_pos:
    enemies_rects.append(Enemies(pos))
###

while True: 

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
                if air_timer < 6:
                    player_y_momentum = -5
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False
            if event.key == K_q:
                shoot = True
    ###

    #scroll
    if mouse_x/2 < 185:
        middle_x = -20
    else:
        middle_x = 20
    if mouse_y/2 < 108 :
        middle_y = -20
    elif mouse_y/2 > 118 :
        middle_y = 20
    scroll[0] += (player_rect.x+middle_x-scroll[0] - 187)/sm 
    scroll[1] += (player_rect.y+middle_y-scroll[1] - 100)/sm
    smscroll = scroll.copy()
    smscroll[0] = int(scroll[0])
    smscroll[1] = int(scroll[1])
    ###

    #backgroud
    Display.blit(texture.background_image, (0, 0))
    Display.blit(texture.background3_image, (0, 0))
    Display.blit(texture.background2_image, (-bgsc, 0))
    Display.blit(texture.background2_image, (400-bgsc, 0))
    if bgsc >= 400:
        Display.blit(texture.background2_image, (400-bgsc, 0))
        bgsc = 0
    Display.blit(texture.background2_image, (-400-bgsc, 0))
    if bgsc <= -400:
        Display.blit(texture.background2_image, (-400-bgsc, 0))
        bgsc = 0
    ###

    y = 0
    #draw tile
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                Display.blit(dirt_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == '2':
                Display.blit(grass2_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == '3':
                Display.blit(grass3_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == '4':
                Display.blit(grass4_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == '5':
                Display.blit(grass5_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == '6':
                Display.blit(grass6_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == '7':
                Display.blit(grass7_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == '8':
                Display.blit(grass8_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == '9':
                Display.blit(grass9_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == 'A':
                Display.blit(grass10_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            if tile == 'B':
                Display.blit(grass11_image, (x * TILE_SIZE - smscroll[0], y * TILE_SIZE - smscroll[1]))
            x += 1
        y += 1
    ###

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

    #draw castle 
    castle_rect = Rect(-200, -100, 200, 500)
    Display.blit(castle_image, (castle_rect.x - smscroll[0], castle_rect.y - smscroll[1]))
    tile_rects.append(castle_rect) 
    ###

    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
        bgsc += 0.2
        step += 0.3
        right = True
    elif moving_left:
        player_movement[0] -= 2
        bgsc -= 0.2
        step += 0.3
        right = False 
    else:
        step = 0
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum > 3:
        player_y_momentum = 3
    
    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['top']:
        player_y_momentum += 5
    if collisions['bottom']:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1

    #draw Bullet
    if shoot:
        Bullets.append(Bullet(player_rect.x + texture.player_image.get_width()/2, player_rect.y + texture.player_image.get_height()/2, mouse_x/2, mouse_y/2))

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
    if step > 5:
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
    Display.blit(player_image, (player_rect.x - smscroll[0], player_rect.y - smscroll[1]))
    
    for enemy in enemies_rects:
        if player_rect.colliderect(enemy):
            enemies_rects.remove(enemy)
            life = 0
    ###if player die
    if player_rect.y >= 450 or life == 0: #if fall out
        player_rect.y = 100
        player_rect.x = 0
        life = 1
        enemies_rects = []
        for pos in enemies_pos:
            enemies_rects.append(Enemies(pos))

    ###

    #draw crosshair
    Display.blit(crosshair_image, (mouse_x/2 - crosshair_image.get_width()/2 - 5, mouse_y/2 - crosshair_image.get_height()/2 ))
    ###

    surf = transform.scale(Display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    display.flip()
    clock.tick(70)
