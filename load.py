import pygame
from script import load_image

player_image = load_image('image/player')
enemy_1_image = load_image('image/enemy/1')
portal_image = load_image('image/portal')
bullet_image = load_image('image/fireball')
earth_image = pygame.image.load('image/blocks/earth.png').convert_alpha()
center_image = pygame.image.load('image/blocks/center.png').convert_alpha()
water_image = pygame.image.load('image/blocks/water.png').convert_alpha()
box_image = pygame.image.load('image/blocks/box.png').convert_alpha()
stop_image = pygame.image.load('image/blocks/stop.png').convert_alpha()
enemy_2_image = pygame.image.load('image/enemy/2/1.png').convert_alpha()
enemy_3_image = pygame.image.load('image/enemy/3/1.png').convert_alpha()
enemy_4_image = pygame.image.load('image/enemy/4/1.png').convert_alpha()
monetka_image = pygame.image.load('image/item/monetka.png').convert_alpha()