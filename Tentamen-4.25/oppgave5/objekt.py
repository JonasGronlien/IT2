import pygame

class Objekt:
    def __init__(self, x: int, y: int, farge: str):
        self.surface = pygame.Surface((75, 25))
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y) 
        self.surface.fill(farge)


    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)



