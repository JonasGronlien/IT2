import pygame 

from ratchet import Ratchet 
from blokk import Blokk 
from objekt import Objekt 
from ball import Ball 
 
#oppset av pygame 
pygame.init()
BREDDE = 600 
HOYDE = 900 
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
font = pygame.freetype.SysFont("Arial", 50)
kjorer = True 
spiller = Ratchet()
ball = Ball()
blokker = []
for i in range(5):
    blokker.append(Blokk())

while kjorer:
    vindu.fill("black") 
    
    #hendelser
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjorer = False
 
    #tastaturtrykk 
    taster = pygame.key.get_pressed()  
    if taster[pygame.K_LEFT]:
        spiller.x_fart = -1
        spiller.y_fart = 0
    
    if taster[pygame.K_RIGHT]:
        spiller.x_fart = 1
        spiller.y_fart = 0  
        
    # opptaterer spilllogikk 
    spiller.oppdater_posisjon()
    
    if ball.rect.centery >= 900: 
        pygame.quit()
        raise SystemExit
    
    if ball.rect.centery <= 900:
        ball.diry = -1
    
    if ball.rect.centerx >= 600:
        ball.dirx = -1
        
    if ball.rect.centerx <= 0:
        ball.dirx = 1
    
    if ball.rect.colliderect(spiller.rect):
        ball.diry = 1 

        
    for blokk in blokker:
        if ball.rect.colliderect(blokk.rect):
            blokker.remove(blokk)
    
    #tegn på viduet
    spiller.tegn(vindu)
    
    ball.tegn(vindu)
    
    for blokk in blokker:
        blokk.tegn(vindu)
    
    
            

    pygame.display.flip()
 
    klokke.tick(60) 
 
pygame.quit()
