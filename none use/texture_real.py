import pygame
from pygame import transform

#start castle 
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
crosshair_image = pygame.transform.scale(pygame.image.load('crosshair.png'), (32, 32))

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