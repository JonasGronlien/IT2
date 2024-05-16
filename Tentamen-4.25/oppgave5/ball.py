import pygame
from objekt import Objekt
import random

class Ball(Objekt):
    def __init__(self) -> None:
        super().__init__(300, 450, "white")
        self.surface = pygame.Surface((15, 15))
        self.rect = self.surface.get_rect()
        self.surface.fill("white")
        self.rect.centerx = 450
        self.rect.centery = 300
        self.vel = 3
        startdir = random.randint(1, 2)
        if startdir == 1:
            self.dirx = 1
        else: 
            self.dirx = -1 
        self.diry = random.triangular(0,1)
    

    
    