from math import sqrt
from resource.keko import Keko
ISO_LUKU = 1000000000000

class Dijkstra:
    def __init__(self, sokkelo, alku, loppu):
        self.loppu = loppu
        self.alku = alku
        self.edellinen = {}
        self.vieraillut = []
        self.sokkelo = sokkelo
        self.keko = Keko()

    def dijkstra(self):
        for solmu in self.sokkelo.solmut:
            self.edellinen[solmu.id] = None
            self.keko.lisaa(solmu, ISO_LUKU)
        self.keko.muuta_pituus(self.alku.id,0)
        while not self.keko.on_tyhja():
            tutki = self.keko.palauta_pienin()
            print_sokkelo(self.sokkelo.solmut)
            print("")
            if tutki == self.loppu:
                break
            for linkki in self.sokkelo.linkit:
                kohde = self.relevantit_linkit(tutki, linkki)
                if not kohde == -1:
                    if self.keko.etaisyydet[kohde] > self.keko.etaisyydet[tutki.id] +1:
                        self.keko.muuta_pituus(kohde,self.keko.etaisyydet[tutki.id] +1)
                        self.edellinen[kohde] = tutki
            
            print_sokkelo(self.sokkelo.solmut)
            print("")
            tutki.tila = 3
        return self.palauta_reitti()


    """def etaisyys_linnuntie(self, piste):
        return sqrt((piste.x - self.loppu.x)**2 + (piste.y - self.loppu.y)**2)"""

    def relevantit_linkit(self,tutki,linkki):
        if linkki[0] == tutki.id:
            return linkki[1]
        elif linkki[1] == tutki.id:
            return linkki[0]
        return -1

    def palauta_reitti(self):
        reitti = [self.loppu.id]
        sijainti = self.edellinen[self.loppu.id]
        if sijainti == None:
            return []
        while sijainti:
            reitti.append(sijainti.id)
            sijainti = self.edellinen[sijainti.id]
        reitti.reverse()
        return reitti

    def lyhin_matka(self):
        """lyhin matka sen jälkeen kun reitti on löydetty"""
        matka = self.keko.etaisyydet[self.loppu.id]
        if self.keko.etaisyydet[self.loppu.id] == ISO_LUKU:
            return -1
        return matka

    def __str__(self) -> str:
        reitti = str(self.dijkstra())
        if self.lyhin_matka() == -1:
            return "reittiä alun ja lopun välillä ei löydetty"
        return "lyhyin löydetty matka: " + str(self.keko.etaisyydet[self.loppu.id]) + "\nreitti: " + reitti

    def vaihda_loppu(self, uusi):
        self.loppu = uusi

    def vaihda_alku(self, uusi):
        self.alku = uusi