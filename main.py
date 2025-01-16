from csv import DictWriter

from models.Database import Database
from models.Stopwatch import Stopwatch

if __name__ == '__main__':
    pass

    db = Database() #andmebaasiga ühenduse testimiseks
    #db.close_connection()  #Uus ühendus andmebaasiga game_leaderboard_v2.db loodud
                            #Ühendus andmebaasiga game_leaderboard_v2.db suletud
    data = db.read_records()
    if data:
        for record in data:
            print(record)
