# This file was created by Cary Yao on 9/29/23

# import libraries and modules 
import pygame as pg
from pygame.sprite import Sprite
import random 
from random import randint
import os
from settings import *
from sprites import *

vec = pg.math.Vector2

# setup asset folders here
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')



class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        clock = pg.time.Clock()
    def new(self):
        # create a group for all sprites
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)
        plat = Platform(150, 300, 100, 30, "static")
        plat1 = Platform(200, 200, 100, 30, "moving")
        plat2 = Ice_plat(100, 400, 100, 30, "ice")
        # add instances to groups
        self.all_sprites.add(self.player)

        # takes PLATFORM_LIST from settings module and puts in pygame
        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for m in range(0,25):
            m = Mob(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        self.all_sprites.update()

    # this is what prevents the player from falling through the platform when falling down...
    #    if player.vel.y > 0:
    #       hits = pg.sprite.spritecollide(player, all_platforms, False)
    #        if hits:
    #            player.pos.y = hits[0].rect.top
    #            player.vel.y = 0
                
    # this prevents the player from jumping up through a platform
    #   if player.vel.y < 0:
    #        hits = pg.sprite.spritecollide(player, all_platforms, False)
    #       if hits:
    #            print("ouch")
    #            SCORE -= 1
    #            if player.rect.bottom >= hits[0].rect.top - 5:
    #                player.pos.y = hits[0].rect.top - 10
    #                player.rect.top = hits[0].rect.bottom
    #                player.acc.y = 5
    #                player.vel.y = 0

def events(self):
    for event in pg.event.get():
    # check for closed window
        if event.type == pg.QUIT:
            self.running = False
def draw(self):
    ############ Draw ##############
    #draw the background screen
    self.screen.fill(BLACK)
    # draw all sprites 
    self.all_sprites.draw(self.screen)
    self.draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/10)
    # buffer - after drawing everything, flip display
    pg.display.flip()

def draw_text(self, text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    self.screen.blit(text_surface, text_rect)

def show_start_screen(self):
    pass
def show_go_screen(self):
    pass

# g = Game()
# while g.running:
#    g.new()

pg.quit()