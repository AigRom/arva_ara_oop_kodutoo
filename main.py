1


from models.Model import Model


if __name__ == '__main__':


    #db = Database() #andmebaasiga ühenduse testimiseks
    #db.close_connection()  #Uus ühendus andmebaasiga game_leaderboard_v2.db loodud
                            #Ühendus andmebaasiga game_leaderboard_v2.db suletud
    #data = db.read_records()
    #if data:
        #for record in data:
            #print(record)

    model = Model()
    model.show_menu()

    #print(model.pc_nr)
    #time.sleep(2)
    #model.stopwatch.stop()
    #print(model.stopwatch.format_time())
    # TODO järgnev rida oli enne show_menu osa
    #model.lets_play()



