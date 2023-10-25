import pygame
from pygame import transform

#start castle 
castle_image = pygame.image.load('texture/castletest.png')

#background
background_image = pygame.transform.scale(pygame.image.load('texture/2 Background/Background.png'), (400, 200))
background2_image = pygame.image.load('texture/2 Background/Layers/3.png')
background3_image = pygame.transform.scale(pygame.image.load('texture/2 Background/Layers/4.png'), (400, 200))

#tiles
grass2_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_02.png'), (20, 20))
grass3_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_03.png'), (20, 20))
grass4_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_04.png'), (20, 20))
grass5_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_05.png'), (20, 20))
grass6_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_06.png'), (20, 20))
grass7_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_07.png'), (20, 20))
grass8_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_08.png'), (20, 20))
grass9_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_09.png'), (20, 20))
grass10_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_10.png'), (20, 20))
grass11_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_11.png'), (20, 20))
dirt_image = pygame.transform.scale(pygame.image.load('texture/1 Tiles/Tile_01.png'), (20, 20))

#player
player_image = pygame.image.load('player/animations/0.png')
player_jump_image = pygame.image.load('frogjump.png')

#crsoohiar
crosshair_image = pygame.transform.scale(pygame.image.load('crosshair.png'), (20, 20))

player_animations = [pygame.image.load('player/animations/0.png'),
                    pygame.image.load('player/animations/1.png'),
                    pygame.image.load('player/animations/2.png'),
                    pygame.image.load('player/animations/3.png'),
                    pygame.image.load('player/animations/4.png'),
                    pygame.image.load('player/animations/5.png'),
                    pygame.image.load('player/animations/6.png')]

ceena = pygame.transform.scale(pygame.image.load('enemy.jpg'), (20, 20))
ceena1 = pygame.transform.scale(pygame.image.load('enemy1.jpg'), (20, 20))
ceena2 = pygame.transform.scale(pygame.image.load('enemy2.jpg'), (20, 20))
enemie_animation = [ceena, ceena1, ceena2]