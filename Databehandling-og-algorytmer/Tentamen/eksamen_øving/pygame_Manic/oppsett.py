import pygame 

pygame.init()

#bredde og høyde på vinduet 
#STORE bokstaver betyr konstanter
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE)) 
klokke = pygame.time.Clock()


#oppsett av spill, spiller, hinder osv 


# Gameloop-en
while True:
    #Hendelser 
    hendelser = pygame.event.get() # liste med alle hendelser som has skjedd siden forrige frame
    for hendelse in hendelser: 
        
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    # Input fra tastatur 
    taster = pygame.key.get_pressed
    if taster[pygame.K_UP]:
        print("Du trykker på 'Pil opp' ")
    if taster[pygame.K_s]:#bruker if setning og ikke elif fordi da kan man trykke fler taster samtidig 
        print("DU trykker på 's' ")
    
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
    
    # Tegn på vinduet 
    vindu.fill("white") # fyller vinduet med bakrunnsfarge, slik at vi fjerner alt fra forrige frame
    
    pygame.display.flip()
    klokke.tick(FPS)