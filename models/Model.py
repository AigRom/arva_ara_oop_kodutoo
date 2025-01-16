
from random import randint

from models.Stopwatch import Stopwatch


class Model:
    pc_nr = randint(1,100)
    steps = 0
    game_over = False
    cheater = False
    stopwatch = Stopwatch()

    def __init__(self):
        self.reset_game()
    """Teeb uue mängu."""
    def reset_game(self):
        self.pc_nr = randint(1, 100)  # juhuslik nr
        self.game_over = False #Mäng ei ole läbi
        self.cheater = False #Mängija ei ole petis
        self.stopwatch.reset() #nullib stopperi
        self.stopwatch.start()  # käivitab stopperi
        self.steps = 0 #Käikude arv

    def ask(self):
        user_nr = int(input("Sisesta number: ")) # Küsi kasutajalt numbrit
        self.steps += 1 #Sammude arv kasvab

        if user_nr == 1000: #Tagauks
            self.cheater = True #Sa ooed petja
            self.game_over = True #Mäng sai läbi
            self.stopwatch.stop()   #peata aeg
            print(f'Leidsid mu nõrga koha.Õigen number on {self.pc_nr}')
        elif user_nr > self.pc_nr:
            print('Väiksem')
        elif user_nr < self.pc_nr:
            print('Suurem')
        elif user_nr == self.pc_nr:
            self.game_over = True
            self.stopwatch.stop()
            print(f'Leidsid õige numbri {self.steps} sammuga.')

    def lets_play(self):
        """Mängime mängu - avalik meetod"""
        while not self.game_over:
            self.ask()
        #Näita mängu aega
        print(f'Mäng kestis {self.stopwatch.format_time()}')

