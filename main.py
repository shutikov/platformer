import pygame
import os
import sys
import random

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
monetka = 0
svitok = 0
lvl_game = 1
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 30)
from load import *


def drawMaps(nameFile):
    maps = []
    source = 'game_lvl/' + str(nameFile)
    with open(source, 'r') as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])
    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == "1":
                box = Box(box_image, pos)
                box_group.add(box)
                camera_group.add(box)
            elif maps[i][j] == "2":
                center = Center(center_image, pos)
                center_group.add(center)
                camera_group.add(center)
            elif maps[i][j] == "3":
                earth = Earth(earth_image, pos)
                earth_group.add(earth)
                camera_group.add(earth)
            elif maps[i][j] == "4":
                water = Water(water_image, pos)
                water_group.add(water)
                camera_group.add(water)
            elif maps[i][j] == "5":
                stopenemy = StopEnemy(stop_image, pos)
                stopenemy_group.add(stopenemy)
                camera_group.add(stopenemy)
            elif maps[i][j] == "6":
                enemy = Enemy(enemy_1_image, pos)
                enemy_group.add(enemy)
                camera_group.add(enemy)
            elif maps[i][j] == "7":
                monetka = Monetka(monetka_image, pos)
                monetka_group.add(monetka)
                camera_group.add(monetka)
            elif maps[i][j] == "8":
                portal = Portal(portal_image, pos)
                portal_group.add(portal)
                camera_group.add(portal)
            elif maps[i][j] == "9":
                hpelik = Hpelik(hp_image, pos)
                hpelik_group.add(hpelik)
                camera_group.add(hpelik)
            elif maps[i][j] == "10":
                mpelik = Mpelik(mp_image, pos)
                hpelik_group.add(mpelik)
                camera_group.add(mpelik)
            elif maps[i][j] == "11":
                npc = NPC(npc_image, pos)
                npc_group.add(npc)
                camera_group.add(npc)
            elif maps[i][j] == "12":
                svitok = Svitok(svitok_image, pos)
                svitok_group.add(svitok)
                camera_group.add(svitok)
            elif maps[i][j] == "13":
                fire = Fire(fire_image, pos)
                fire_group.add(fire)
                camera_group.add(fire)


def restart():
    global player_group, earth_group, water_group, box_group, center_group, camera_group, player, stopenemy_group, monetka_group, enemy_group, portal_group, fireball_group, hpelik_group, mpelik_group, npc_group, svitok_group, fire_group
    player_group = pygame.sprite.Group()
    fireball_group = pygame.sprite.Group()
    earth_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    npc_group = pygame.sprite.Group()
    center_group = pygame.sprite.Group()
    camera_group = pygame.sprite.Group()
    stopenemy_group = pygame.sprite.Group()
    monetka_group = pygame.sprite.Group()
    hpelik_group = pygame.sprite.Group()
    mpelik_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    svitok_group = pygame.sprite.Group()
    fire_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    player = Player(player_image, (300, 300))
    player_group.add(player)


def gamelvl():
    sc.fill('black')
    player_group.update()
    player_group.draw(sc)
    hpelik_group.update(0)
    hpelik_group.draw(sc)
    mpelik_group.update(0)
    mpelik_group.draw(sc)
    fire_group.update(0)
    fire_group.draw(sc)
    fireball_group.update(0)
    fireball_group.draw(sc)
    earth_group.update(0)
    earth_group.draw(sc)
    water_group.update(0)
    water_group.draw(sc)
    box_group.update(0)
    box_group.draw(sc)
    center_group.update(0)
    center_group.draw(sc)
    monetka_group.update(0)
    monetka_group.draw(sc)
    svitok_group.update(0)
    svitok_group.draw(sc)
    npc_group.update(0)
    npc_group.draw(sc)
    enemy_group.update(0)
    enemy_group.draw(sc)
    portal_group.update(0)
    portal_group.draw(sc)
    text_font = font.render(f"Монеток: {monetka}", True, 'white')
    sc.blit(text_font, (1000, 50))
    pygame.display.update()


class NPC(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True

    def update(self, step):
        self.animation()
        self.rect.x += step
        self.image = npc_image[self.frame]

        if pygame.sprite.spritecollide(self, player_group, False):
            if lvl_game == 1:
                sc.blit(qwest_1_image, (self.rect.x - 30, self.rect.y - 100))
            elif lvl_game == 2:
                sc.blit(qwest_2_image, (self.rect.x - 30, self.rect.y - 100))

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(npc_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


class Svitok(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        global svitok
        self.rect.x += step

        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()
            svitok += 1


class Earth(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left

            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step

        if pygame.sprite.spritecollide(self, player_group, False):
            pygame.quit()
            sys.exit()


class Box(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left

            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Center(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left

            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Fire(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.timer_attack = 0
        self.anime = True

    def update(self, step):
        global lvl_game
        self.animation()
        self.rect.x += step
        self.image = fire_image[self.frame]

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(fire_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


class Monetka(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        global monetka
        self.rect.x += step

        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()
            monetka += 1


class StopEnemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Hpelik(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step

        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()
            player.hp += 50


class Mpelik(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step

        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()
            player.mp += 30


class Portal(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True

    def update(self, step):
        global lvl_game
        self.animation()
        self.rect.x += step
        self.image = portal_image[self.frame]

        if lvl_game == 1:
            if svitok == 2:
                sc.blit(flag_image, (self.rect.center[0] - 10, self.rect.y - 60))
            if pygame.sprite.spritecollide(self, player_group, False) and svitok == 2:
                lvl_game = 2
                restart()
                drawMaps('2.txt')

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(portal_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 3
        self.dir = 1
        self.frame = 0
        self.hp = 100
        self.timer_attack = 0
        self.timer_anime = 0
        self.anime = True

    def update(self, step):
        self.draw_stats()
        self.rect.x += step
        if self.dir == 1:
            self.rect.x += self.speed
            self.image = enemy_1_image[self.frame]
        elif self.dir == -1:
            self.rect.x -= self.speed

        if pygame.sprite.spritecollide(self, fireball_group, False):
            if self.timer_attack / FPS > 0.2:
                self.hp -= 10
                self.timer_attack = 0

            self.image = pygame.transform.flip(enemy_1_image[self.frame], True, False)
        if pygame.sprite.spritecollide(self, stopenemy_group, False):
            self.dir *= -1

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.01:
                if self.frame == len(enemy_1_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def draw_stats(self):
        width_hp = 96 * (self.hp / 100)
        pygame.draw.rect(sc, 'black', (self.rect.x - 30, self.rect.y - 52, 100, 20), 2)
        pygame.draw.rect(sc, 'red', (self.rect.x - 27, self.rect.y - 50, width_hp, 15))


'''        if pygame.sprite.collide(self, player_group, False):
            pygame.quit()
            sys.exit()
'''


class Fireball(pygame.sprite.Sprite):
    def __init__(self, pos, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = fireball_image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.anime = True
        self.timer_anime = 0
        if dir == "left":
            self.speed = -5
        else:
            self.speed = 5

    def update(self, step):
        self.animation()
        self.rect.x += step + self.speed
        if self.speed > 0:
            self.image = fireball_image[self.frame]
        else:
            self.image = pygame.transform.flip(fireball_image[self.frame], True, False)


    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(fireball_image) - 1:
                    self.kill()
                else:
                    self.frame += 1
                    self.timer_anime = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.timer_shot = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 10
        self.velocity_y = 0
        self.on_ground = True
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
        self.key = pygame.key.get_pressed()
        self.dir = 'right'
        self.timer_attack = 0
        self.hp = 100
        self.mp = 70

    def move(self):
        self.animation()
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.dir = 'right'
            self.anime = True
            self.image = player_image[self.frame]
            self.rect.x += self.speed
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.update(-self.speed)

        elif key[pygame.K_a]:
            self.image = pygame.transform.flip(player_image[self.frame], True, False)
            self.anime = True
            self.dir = 'left'
            self.rect.x -= self.speed
            if self.rect.left < 200:
                self.rect.left = 200
                camera_group.update(self.speed)
        else:
            self.anime = False

        if pygame.sprite.spritecollide(self, fire_group, False):
            if self.timer_attack / FPS > 0.2:
                self.hp -= 10
                self.timer_attack = 0


    def jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def attack(self):
        self.timer_attack += 1
        if self.key[pygame.K_RETURN] and self.timer_attack / FPS > 1:
            fireball = Fireball(self.rect.center, self.dir)
            fireball_group.add(fireball)
            camera_group.add(fireball)
            self.timer_attack = 0

    def draw_stats(self):
        width_hp = 96 * (self.hp / 100)
        width_mp = 96 * (self.mp / 100)
        pygame.draw.rect(sc, 'black', (self.rect.x - 30, self.rect.y - 52, 100, 20), 2)
        pygame.draw.rect(sc, 'green', (self.rect.x - 27, self.rect.y - 50, width_hp, 15))

        pygame.draw.rect(sc, 'black', (self.rect.x - 30, self.rect.y - 30, 100, 10), 2)
        pygame.draw.rect(sc, 'blue', (self.rect.x - 27, self.rect.y - 27, width_mp, 6))

    def update(self):
        self.animation()
        self.attack()
        self.move()
        self.jump()
        self.draw_stats()
        self.key = pygame.key.get_pressed()


restart()
drawMaps("1.txt")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    gamelvl()
    clock.tick(FPS)
