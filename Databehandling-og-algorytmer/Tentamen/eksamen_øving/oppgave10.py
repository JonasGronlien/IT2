import pygame


pygame.init()

#1 oppsett 
BREDDE = 800
HOYDE = 800

skjerm = pygame.display.set_mode((BREDDE, HOYDE))
pygame.display.set_caption("PacTroll")

clock = pygame.time.Clock()
FPS = 60

#definerer spiller handlinger variabler 
moving_left = False 
moving_right = False
moving_up = False
moving_down = False

#definerer farger 
BG = (0,0,0)
GREEN = (0, 225, 0)

def draw_bg():
    skjerm.fill(BG)

class Troll:
    def __init__(self, direction ):
        self.rect = pygame.draw.rect(skjerm,(GREEN))
        self.fart = 10 
        self.direction = 1
    
    def move(self moving_left, moving_right, moving_up, moving_down):
        dx = 0
        dy = 0 

        if moving_left:
            dx 