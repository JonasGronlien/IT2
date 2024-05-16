import pygame 
from figur import Figur
from menneske import Menneske 
from sau import Sau 

#bredde og høyde på vinduet 
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE)) 
klokke = pygame.time.Clock()

#oppsett av spill, spiller, hinder osv 
spiller = Menneske()
sauer: list[Sau] = []
for i in range (3):
    sauer.append( Sau() )


# Gameloop-en
while True:
    #Hendelser 
    hendelser = pygame.event.get() # liste med alle hendelser som has skjedd siden forrige frame
    for hendelse in hendelser: 
        
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    # Input fra tastatur 
    taster = pygame.key.get_pressed()
    
    if taster[pygame.K_UP]:
        spiller.y_fart = -1
        spiller.x_fart = 1

    if taster[pygame.K_DOWN]:
        spiller.y_fart = 1
        spiller.x_fart = 0
    
    if taster[pygame.K_LEFT]:
        spiller.x_fart = -1
        spiller.y_fart = 0
    
    if taster[pygame.K_RIGHT]:
        spiller.x_fart = 1
        spiller.y_fart = 0
    

    
    # Input fra mus 
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()
    print(mus_klikk)
    
    if mus_klikk[0]:
        x_pos = mus_posisjon[0]
        y_pos = mus_posisjon[1]
        print("venstreklikk i posisjon x: {x_pos}, y: {y_pos}")
        
    if mus_klikk[2]:
        x_pos = mus_posisjon[0]
        y_pos = mus_posisjon[1]
        print("høyreklikk i posisjon x: {x_pos}, y: {y_pos}")
        
    
    # Opptater spilllogikk her (opptater fart, sjekk kolisjoner osv)
    spiller.opptater_posisjon()
    
    # Tegn på vinduet 
    vindu.fill("white") # fyller vinduet med bakrunnsfarge, slik at vi fjerner alt fra forrige frame
    spiller.tegn(vindu)
    
    for sau in sauer:
        sau.tegn(vindu)
    
    pygame.display.flip()
    klokke.tick(FPS)