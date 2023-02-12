from math import sqrt
from luo_sokkelo import luo_sokkelo
from print_sokkelo import print_sokkelo
ISO_LUKU = 1000000000000

class Dijkstra:
    def __init__(self, sokkelo, alku, loppu):
        self.loppu = loppu
        self.etaisyydet = {}
        self.edellinen = {}
        self.vierailemattomat = []
        self.vieraillut = []
        self.sokkelo = sokkelo
        self.dijkstra(sokkelo,alku,loppu)

    def dijkstra(self, sokkelo, alku, loppu):
        for solmu in sokkelo.solmut:
            self.etaisyydet[solmu.id] = ISO_LUKU
            self.edellinen[solmu.id] = None
            self.vierailemattomat.append(solmu)
        self.etaisyydet[alku.id] = 0
        while self.vierailemattomat:
            tutki = self.hae_pienin_etaisyys()
            print_sokkelo(self.sokkelo.solmut)
            print("")
            if tutki == loppu:
                break
            for linkki in sokkelo.linkit:
                kohde = self.relevantit_linkit(tutki, linkki)
                if not kohde == -1:
                    if self.etaisyydet[kohde] > self.etaisyydet[tutki.id] + 1:
                        self.etaisyydet[kohde] = self.etaisyydet[tutki.id] + 1
                        self.edellinen[kohde] = tutki
            
            print_sokkelo(self.sokkelo.solmut)
            print("")
            tutki.tila = 3
        return self.palauta_reitti()


    def etaisyys_linnuntie(self, piste):
        return sqrt((piste.x - self.loppu.x)**2 + (piste.y - self.loppu.y)**2)
    
    def hae_pienin_etaisyys(self):
        pienin = self.vierailemattomat[0]
        for solmu in self.vierailemattomat:
            if self.etaisyydet[solmu.id] < self.etaisyydet[pienin.id]:
                pienin = solmu
        pienin.tila = 2
        self.vieraillut.append(pienin)
        self.vierailemattomat.remove(pienin)
        return pienin

    def relevantit_linkit(self,tutki,linkki):
        if linkki[0] == tutki.id:
            return linkki[1]
        elif linkki[1] == tutki.id:
            return linkki[0]
        return -1

    def palauta_reitti(self):
        reitti = [self.loppu.id]
        sijainti = self.edellinen[self.loppu.id]
        while sijainti:
            reitti.append(sijainti.id)
            sijainti = self.edellinen[sijainti.id]
        reitti.reverse()
        return reitti





iso_sokkelo = [0,0,1,1,1,0,
1,0,1,0,0,0,
1,1,1,0,0,1,
0,0,0,0,1,0]
luotu_sokkelo = luo_sokkelo(iso_sokkelo,6)
dijkstra_testaus = Dijkstra(luotu_sokkelo,luotu_sokkelo.solmut[2],luotu_sokkelo.solmut[5])