import os
import datetime
from models.Database import Database

class ExportToFile:
    def __init__(self, model):
        self.model = model  # Mudel, et kasutada format_time()
        self.db = Database()  # Loome andmebaasi objekti
        self.data = self.db.for_export()  # Võtame kogu edetabeli sisu

    def export(self):
        if not self.data:
            print("⚠️  Andmebaasis puuduvad edetabeli andmed. Kontrolli, kas tabelis 'ranking' on kirjeid!")
            return

        # Faili nimi vastavalt andmebaasi nimele, kuid .txt laiendiga
        db_filename = os.path.basename(self.db.db_name)
        txt_filename = os.path.splitext(db_filename)[0] + ".txt"

        # Päis (fikseeritud)
        headers = "id;name;score;steps;cheater;game_length;game_time"

        with open(txt_filename, "w", encoding="utf-8") as f:
            f.write(headers + "\n")  # Esimene rida sisaldab veerunimesid

            # Kirjutame iga rea faili
            for row in self.data:
                id_, name, quess, steps, cheater, game_length, game_time = row  # Kogu edetabeli info

                # Vormindame sekundid HH:MM:SS kujule
                formatted_length = self.model.format_time(game_length)

                # Kontrollime, kas `game_time` on juba string ja teisendame õigesse formaati
                if isinstance(game_time, str):
                    # Muudame formaadi: 2025-03-15 13:49:17 → 15.03.2025 13:49:17
                    formatted_time = datetime.datetime.strptime(game_time, "%Y-%m-%d %H:%M:%S").strftime(
                        "%d.%m.%Y %H:%M:%S")
                else:
                    formatted_time = datetime.datetime.fromtimestamp(game_time).strftime("%d.%m.%Y %H:%M:%S")

                # Kirjutame andmed faili
                f.write(f"{id_};{name};{quess};{steps};{cheater};{formatted_length};{formatted_time}\n")

        print(f"Kogu edetabel eksporditi faili: {txt_filename}")
