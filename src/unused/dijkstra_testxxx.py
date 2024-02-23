import unittest
from luo_verkko import testiverkko
from algorithms.djikstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.dijkstra = Dijkstra(testiverkko, 4, 9)
        self.reitti = self.dijkstra.dijkstra()

    def test_loytaa_lyhimman_reitin_pituuden(self):
        self.assertEqual(self.dijkstra.lyhin_matka(), 7)

    def test_palauttaa_lyhimman_reitin(self):
        self.assertEqual(self.reitti,[1,2,8,14,15,16,17,18])

    def test_muodostaa_oikean_merkkijonon(self):
        self.assertEqual(str(self.dijkstra),"lyhyin löydetty matka: 7\nreitti: [1, 2, 3, 4, 5, 6, 12, 18]")

    def test_reitti_loytyy_alhaalta_ylos(self):
        self.dijkstra.vaihda_alku(9)
        self.dijkstra.vaihda_loppu(4)
        self.assertEqual(self.dijkstra.dijkstra(),[18,17,16,15,14,13,7,1])