import threading
import time


class Stopwatch:
    def __init__(self):
        """muutujad (stopperi konstruktor)"""
        self.seconds = 0 #aeg sekundites
        self.running = False #kas aeg käib
        self.thread = None #aeg eraldi threadi(et saaks samaaegselt mängida)

    def start(self):
        """käivita stopper"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run) #lisatud threadi
            self.thread.start() #käivita thread

    def _run(self):
        """AQeg jookseb threadis"""
        while self.running:
            self.seconds += 1  # suurenda ühe sekundi võrra
            time.sleep(1) #oota 1 sekund


    def stop(self):
        """peata stopper"""
        self.running = False

    def reset(self):
        self.stop() #aeg peatada
        self.seconds = 0 #aeg nullida

    def format_time(self):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"
        #return "%02d:%02d:%02d" % (hours, minutes, seconds)