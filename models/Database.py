import sqlite3


class Database:
    db_name = 'game_leaderboard_v2.db' #andmebaasi nimi
    tabel = 'ranking' #tabeli nimi
    def __init__(self):
        """Konstruktor"""
        self.conn = None #ühendus
        self.cursor = None
        self.connect() # loo ühendus

    def connect(self):
        """ loob ühenduse andmebaasiga"""
        try:
            if self.conn:
                self.conn.close()
                print('Varasem andmebaasi ühendus suleti.')

            self.conn = sqlite3.connect(self.db_name) #loo ühendus
            self.cursor = self.conn.cursor()
            print(f'Uus ühendus andmebaasiga {self.db_name} loodud.')

        except sqlite3.Error as error:
            print(f'Tõrge andmebaasi ühenduse loomisel: {error}')
            self.conn = None
            self.cursor = None

    def close_connection(self):
        """sulgeb andmebaasi ühenduse"""
        try:
            if self.conn:
                self.conn.close()
                print(f'Ühendus andmebaasiga {self.db_name} suletud.')
        except sqlite3.Error as error:
            print(f'Tõrge ühenduse sulgemisel: {error}')

    def read_records(self):
        """Loeb andmebaasist kogu edetabeli"""
        if self.cursor:
            try:
                sql = f'SELECT * FROM {self.tabel}'
                self.cursor.execute(sql)
                data = self.cursor.fetchall() #kõik kirjed muutujasse data
                return data #tagastab kõik kirjed
            except sqlite3.Error as error:
                print(f'Kirjete lugemisel ilmnes tõrge: {error}')
                return []
            finally:
                self.close_connection()
        else:
            print('Ühendus andmebaasiga puudub. Loo ühendus andmebaasiga.')


    def add_record(self, name, steps, pc_nr, cheater, seconds):
        if self.cursor:
            try:
                sql = f'INSERT INTO {self.tabel} (name, steps, quess, cheater, game_length) VALUES (?, ?, ?, ?, ?);'
                self.cursor.execute(sql,(name, steps, pc_nr, cheater, seconds))
                self.conn.commit()
                print(f'Mängija on lisatud tabelisse')
            except sqlite3.Error as error:
                print(f'Mängija lisamisel tekkis tõrge: {error}')
            finally:
                self.close_connection()
        else:
            print('Ühendus puudub! Palun loo ühendus andmebaasiga.')


