from objekt import Objekt

class Ratchet(Objekt):
    def __init__(self) -> None:
        super().__init__(25, 300, "green")
        self.x_fart = 0
        self.y_fart = 0

    def oppdater_posisjon(self):
        self.rect.x += self.x_fart
        self.rect.y += self.y_fart