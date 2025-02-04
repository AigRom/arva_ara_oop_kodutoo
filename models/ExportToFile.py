class ExportToFile:
    def __init__(self, model):
        """
        Konstruktor, mis seadistab mudeli ja hangib andmebaasist vajalikud andmed.
        :param model: Mudel, mis antakse kaasa objekti loomisel
        """
        self.model = model                    # Seadistab mudeli
        self.database = Database()            # Loob ühenduse andmebaasiga
        self.data = self.database.for_export() # Hangib andmed sorteeritult
        self.filename = self.database.ranking.replace('.db', '.txt')  # Failinimi vastavuses andmebaasiga

    def export(self):
        """
        Ekspordib andmebaasi andmed tekstifaili semikooloniga eraldatud kujul.
        Faili esimene rida sisaldab veergude nimesid.
        """
        if not self.data:
            print('Andmeid pole eksportimiseks.')
            return

        try:
            with open(self.filename, mode='w', encoding='utf-8') as file:
                # Kirjutab päise
                file.write('ID;Name;Steps;Guesses;Cheater;Game Length;Game Time\n')

                # Kirjutab kõik andmed vormindatult faili
                for record in self.data:
                    id_, name, steps, guesses, cheater, game_length, game_time = record
                    formatted_game_length = self.model.format_time(game_length)
                    formatted_game_time = datetime.fromtimestamp(game_time).strftime('%d.%m.%Y %H:%M:%S')

                    line = f'{id_};{name};{steps};{guesses};{cheater};{formatted_game_length};{formatted_game_time}\n'
                    file.write(line)

            print(f'Andmed edukalt eksporditud faili: {self.filename}')

        except Exception as e:
            print(f'Tõrge andmete eksportimisel: {e}')
