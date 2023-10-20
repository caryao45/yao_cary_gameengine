import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Player(pg.sprite.Sprite):
    # defines function that prints image in pygame 
    def __init__(self, game):
        Sprite.__init__(self)
        # self.image = pg.Surface((50, 50))
        # self.image.fill(GREEN)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)
    # define function controls that moves image when pressing wasd
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            # print("i can jump")
            self.vel.y = -PLAYER_JUMP
    # define function update that updates the image when the controls are used and if the image collides with somethingx
    def update(self):
        # self.rect.x += 5
        # self.rect.y += 5
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # hits = pg.sprite.spritecollide(self, all_platforms, False)
        # if hits:
            # print("I've collided ...")
        # print(all_platforms)
        # if friction - apply here
        self.acc.x += self.vel.x * -0.2 
        self.acc.y += self.vel.y * -0.2
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        self.rect.midbottom = self.pos

# platforms 

class Platform(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        # self.image = pg.image.load(os.path.join(img_folder, 'scissors.gif')).convert()
        # self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        # self.pos = vec(WIDTH/2, HEIGHT/2)
        # self.vel = vec(0,0)
        # self.acc = vec(0,0)
        print(self.rect.center)

# moving platform
class MPlatform(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        # self.image = pg.image.load(os.path.join(img_folder, 'scissors.gif')).convert()
        # self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)
    def update(self):
        self.pos = self.rect.x
        self.rect.x = self.pos + 2

 # ice platform   
class Ice_plat(Platform):
    def __init__(self, x, y, w, h, kind):
        Platform.__init__(self, x, y, w, h, kind)
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        print("i made an ice plat")
    
class Mob(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
    def update(self):
        pass
