import random
from objekt import Objekt 

class Blokk(Objekt):
    def __init__(self):
        tilfeldig_x = random.randint(0, 100)
        tilfeldig_y = random.randint(500,600 )
        super().__init__(tilfeldig_x, tilfeldig_y, "gray")
    