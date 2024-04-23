import copy

from database import meteo_dao
class Model:
    def __init__(self):
        self.umidita_media_mese = {}
        self.umidita_giorno_mese = {}
        self.minimo = 1000000000000000000000000000
        self.sequenza = []

    def get_umidita_media(self, mese):
        self.umidita_media_mese = {}
        lista_umidita = meteo_dao.MeteoDao.get_all_situazioni()
        for situazione in lista_umidita:
            if int(mese) == int(situazione.data.month):
                if mese + "-" + situazione.localita not in self.umidita_media_mese.keys():
                    self.umidita_media_mese[mese + "-" + situazione.localita] = [situazione.umidita, 1]
                else:
                    self.umidita_media_mese[mese+"-"+situazione.localita] = [int(situazione.umidita)+int(self.umidita_media_mese.get(mese+"-"+situazione.localita)[0]), 1 + self.umidita_media_mese.get(mese+"-"+situazione.localita)[1]]
        for (key, val) in self.umidita_media_mese.items():
            self.umidita_media_mese[key] = val[0]/val[1]
        return self.umidita_media_mese

    def get_umidita_giorno(self, mese):
        self.umidita_media_mese = {}
        lista_umidita = meteo_dao.MeteoDao.get_all_situazioni()
        for situazione in lista_umidita:
            if int(mese) == int(situazione.data.month):
                pass


    def calcola_costo(self, parziale):
        pass


    def recursion(self, parziale, situazione):
        if len(parziale) == 15:
            print(parziale)
            costo = self.calcola_costo(parziale)
            if costo <= self.minimo:
                self.sequenza = copy.deepcopy(parziale)
                self.minimo = costo
            else:
                for situazione in self.giorno_successivo():
                    parziale.append(situazione)
                    if self.is_ammissibile(parziale):
                        ricorsione(parziale, situazione)
                    parziale.pop()

    def is_ammissibile(self, parziale):
        #il parziale è la lista dei valori che sono stati aggiunti mentre situazione è il singolo evento che si
        # sta provando ad aggiungere (es. [M] controllo se posso aggiungere Milano alla sequenza)
        pass



