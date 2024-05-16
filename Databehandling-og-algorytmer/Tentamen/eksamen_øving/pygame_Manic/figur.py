import pygame 

class Figur:
    def __init__(self, x: int, y: int, farge: str ) -> None:
        self.surface = pygame.Surface((50, 50))#oppretter surface med bredde og høyde 50
        # oppretter en pygame rect  "rundt" surface-en
        self.rect = self.surface.get_rect()
        
        # plasserer figuren i posijonen x, y
        self.rect.center = (x, y)
        
        #fyller surface-en til figuren med en farge 
        self.surface.fill(farge)
    
    def tegn(self, surface: pygame.surface):
        #putter figuren på en annen surface
        surface.blit(self.surface, self.rect)
        