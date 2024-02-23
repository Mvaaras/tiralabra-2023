import math
from resource.keko import Keko
ISO_LUKU = 1000000000000

class Dijkstra:
    def __init__(self, solmut, alku, loppu):
        self.loppu = loppu
        self.alku = alku
        self.edellinen = {}
        self.vieraillut = set()
        self.solmut = solmut
        self.keko = Keko()

    def dijkstra(self):
        for solmu_id in range (1,self.solmut[0]):
            self.edellinen[solmu_id] = None
            self.keko.lisaa(solmu_id)
        self.keko.muuta_pituus(self.alku,0)
        while not self.keko.on_tyhja():
            tutki = self.keko.palauta_pienin()
            print("")
            if tutki == self.loppu:
                break
            kohteet = self.solmut[tutki]
            for kohde in kohteet:
                if self.keko.etaisyydet[kohde[0]] > self.keko.etaisyydet[tutki] +kohde[1]:
                    self.keko.muuta_pituus(kohde[0],self.keko.etaisyydet[tutki] +kohde[1])
                    self.edellinen[kohde] = tutki
            
            print("")
        return self.palauta_reitti()

    def palauta_reitti(self):
        reitti = [self.loppu]
        sijainti = self.edellinen[self.loppu]
        if sijainti == None:
            return []
        while sijainti:
            reitti.append(sijainti)
            sijainti = self.edellinen[sijainti]
        reitti.reverse()
        return reitti

    def lyhin_matka(self):
        """lyhin matka sen jälkeen kun reitti on löydetty"""
        matka = self.keko.etaisyydet[self.loppu]
        if self.keko.etaisyydet[self.loppu] == ISO_LUKU:
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