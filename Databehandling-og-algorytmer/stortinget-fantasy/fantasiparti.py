from politiker import Politiker 

class Fantasiparti:
    def __init__(self, n: str, e: str) -> None:
        self.navn: str = n
        self.eier: str = e
        self.poeng: int = 0
        self.saldo: int = 100_000
        self.partileder: Politiker = None 
        self.politikere: list[Politiker] = []

    def print_politikere(self):
        if len(self.politikere) == 0:
            print("Partiet er tomt")
        else: 
            for i in range(len(self.politikere)):
                print(f"{i}: {self.politikere[i]}")

    def kjøp_politikere(self, politiker: Politiker):
        if self.saldo >= politiker.verdi and politiker not in self.politikere:
            self.politikere.append(politiker)
            self.saldo -= politiker.verdi
    
    def selg_politiker(self, politiker: Politiker):
        if politiker in self.politikere:
            self.politikere.remove(politiker)
            self.saldo += politiker.verdi/2