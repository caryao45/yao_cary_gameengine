# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 720
HEIGHT = 720
FPS = 30

# player settings
PLAYER_JUMP = 25
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (102, 178, 255)
YELLOW = (255, 255, 0)


PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 4 / 5, 100, 20,"normal"),
                 (125, 350, 100, 20, "moving"),
                 (222, 210, 100, 20, "normal"),
                 (175, 100, 100, 20, "normal"),
                 (515, 480, 100, 20, "moving"),
                 (575, 150, 100, 20, "normal")]
