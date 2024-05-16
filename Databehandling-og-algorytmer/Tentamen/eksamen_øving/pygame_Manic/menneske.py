from figur import Figur 

class Menneske(Figur):
    def __init__(self) -> None:
        super().__init__(25, 300, "green")
        self.x_fart = 0
        self.y_fart = 0 
    
    def opptater_posisjon(self):
        self.rect.x += self.x_fart
        self.rect.x += self.y_fart