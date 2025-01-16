
from random import randint

from models.Database import Database
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
        #self.stopwatch.start()  # käivitab stopperi
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
        self.stopwatch.start()
        while not self.game_over:
            self.ask()
        #Näita mängu aega
        print(f'Mäng kestis {self.stopwatch.format_time()}')

        self.what_next()
        self.show_menu()

    def what_next(self):
        """küsime mängija nime ja lisame andmebaasi"""
        name = self.ask_name()
        db = Database() #loo andmebaasi objekt
        db.add_record(name, self.steps, self.pc_nr, self.cheater, self.stopwatch.seconds)

    @staticmethod
    def ask_name():
        """Küsib nime ja tagastab korrektse nime"""
        name = input('Kuidas on mängija nimi? ')
        if not name.strip():
            name = 'Teadmata'
        return name.strip()

    def show_menu(self):
        """näita mängu menüü"""
        print('1 - Mängima')
        print('2 - Edetabel')
        print('3 - Välju programmist')
        user_input = int(input('sisesta number [1, 2 või 3]'))
        if 1 <= user_input <= 3:
            if user_input == 1:
                self.reset_game()

                self.lets_play()
            elif user_input == 2:
                self.show_leaderboard() #näita edetabelit
                self.show_menu() #lähmne mängima
            elif user_input == 3:
                print('Ootame Sind tagasi!')
                exit()
        else:
            self.show_menu()

    @staticmethod
    def show_leaderboard():
        """näita edetabelit"""
        db = Database()
        data = db.read_records()
        if data:
            for record in data:
                print(record) # name -> record[1]








