from math import sqrt
from resource.keko import Keko
ISO_LUKU = 1000000000000

class Dijkstra:
    def __init__(self, solmut, alku, loppu):
        self.loppu = loppu
        self.alku = alku
        self.edellinen = {}
        self.vieraillut = []
        self.solmut = solmut
        self.keko = Keko()

    def dijkstra(self):
        for solmu_id in range (1,self.solmut[0]):
            self.edellinen[solmu_id] = None
            self.keko.lisaa(solmu_id, ISO_LUKU)
        self.keko.muuta_pituus(self.alku,0)
        while not self.keko.on_tyhja():
            tutki = self.keko.palauta_pienin()
            print("")
            if tutki == self.loppu:
                break
            kohteet = self.solmut[tutki]
            for kohde in kohteet:
                if not kohde == -1:
                    if self.keko.etaisyydet[kohde] > self.keko.etaisyydet[tutki.id] +1:
                        self.keko.muuta_pituus(kohde,self.keko.etaisyydet[tutki.id] +1)
                        self.edellinen[kohde] = tutki
            
            print("")
            tutki.tila = 3
        return self.palauta_reitti()

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