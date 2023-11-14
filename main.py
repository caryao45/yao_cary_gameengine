# content from kids can code: http://kidscancode.org/blog/
# got inspiration for game over from: https://www.youtube.com/watch?v=QuM-jEQ7fAA&ab_channel=CodingWithRuss 
# import libraries and modules

# Design Goals:
# Make platformer game 
# Allow player to move and collect coins
# Make score go up when coin is collected
# Make hitpoints go down when collide with mobs
# Make player not fall off map
# Make game over screen once hitpoints zero or score is ten
# Make play again - figure out how to respawn coins (Didn't do)
# Add timer to increase difficulty (Didn't do)

import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# need variable first
game_over = False

# this will always run
if game_over == False:
    class Game:
        def __init__(self):
            # init pygame and create a window
            pg.init()
            pg.mixer.init()
            self.screen = pg.display.set_mode((WIDTH, HEIGHT))
            pg.display.set_caption("My Game...")
            self.clock = pg.time.Clock()
            self.running = True

        def new(self): 
            # create a group for all sprites
            self.score = 0
            self.all_sprites = pg.sprite.Group()
            self.all_platforms = pg.sprite.Group()
            self.all_mobs = pg.sprite.Group()
            self.all_coins = pg.sprite.Group()
            # instantiate classes
            self.player = Player(self)
            # add instances to groups
            self.all_sprites.add(self.player)

            # prints platforms
            for p in PLATFORM_LIST:
                # instantiation of the Platform class
                plat = Platform(*p)
                self.all_sprites.add(plat)
                self.all_platforms.add(plat)

            # prints mobs randomly 
            for m in range(0,20):
                m = Mob(randint(0, WIDTH), randint(0, math.floor(HEIGHT-100)), 20, 20, "normal")
                self.all_sprites.add(m)
                self.all_mobs.add(m)

            # prints coins randomly   
            for c in range(0,10):
                c  = Coin(randint(0, WIDTH), randint(0, math.floor(HEIGHT-100)), 20, 20, "normal")
                self.all_sprites.add(c)
                self.all_coins.add(c)

            self.run()


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
            if self.player.vel.y >= 0:
                hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
                if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    self.player.vel.x = hits[0].speed*1.5


            # this prevents the player from jumping up through a platform
            # doesen't work btw
            elif self.player.vel.y <= 0:
                hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
                if hits:
                    self.player.acc.y = 5
                    self.player.vel.y = 0
                    self.score -= 1
                    if self.player.rect.bottom >= hits[0].rect.top - 1:
                        self.player.rect.top = hits[0].rect.bottom

            # When player collides with coin, add 1 to score and remove coin
            if pg.sprite.spritecollide(self.player, self.all_coins, True):
                self.player.score += 1

            # when player collides with mob, minue 1 to hitpoints
            if pg.sprite.spritecollide(self.player, self.all_mobs, False):
                self.player.hitpoints -= 1
                    

        def events(self):
            for event in pg.event.get():
            # check for closed window
                if event.type == pg.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False

        def draw(self):
            ############ Draw ################
            # draw the background screen
            self.screen.fill(LIGHTBLUE)
            # draw all sprites
            self.all_sprites.draw(self.screen)
            # Displays score and hitpoint values
            self.draw_text("Score: " + str(self.player.score), 22, WHITE, 50, HEIGHT/10)
            self.draw_text("Hitpoints: " + str(self.player.hitpoints), 22 , WHITE, 65, HEIGHT/20)
            # buffer - after drawing everything, flip display
            pg.display.flip()
            # Checks if hitpoints is zero; if zero, then prints game over text
            if self.player.hitpoints <= 0:
                self.player.hitpoints = 0
                game_over = True
                if game_over == True:
                    self.draw_text("Game Over!", 22, WHITE, 360, 320)
                    self.draw_text("Score: " + str(self.player.score), 22, WHITE, 360, 360)
                    self.draw_text("Press R to Play Again!", 22, WHITE, 360, 400)
                    pg.display.flip()
            # Checks if score is ten; if ten, then prints you win text
            if self.player.score == 10:
                self.draw_text("You Win!", 22, WHITE, 360, 320)
                self.draw_text("Score: " + str(self.player.score), 22, WHITE, 360, 360)
                self.draw_text("Press R to Play Again!", 22, WHITE, 360, 400)
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


g = Game()
while g.running:
    g.new()


pg.quit()
