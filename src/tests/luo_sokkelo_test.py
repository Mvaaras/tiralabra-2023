import unittest
from luo_sokkelo import luo_sokkelo

class TestLuoSokkelo(unittest.TestCase):
    def setUp(self):
        sokkelo = [0,1,0,
        1,1,1,
        0,1,1]
        iso_sokkelo = [0,0,1,1,1,0,
        1,1,1,0,0,0,
        1,0,0,0,0,1,
        0,0,0,0,1,0]
        self.luotu_sokkelo = luo_sokkelo(iso_sokkelo,6)



    def test_luo_sokkelo_palauttaa_kaksi_listaa(self):
        self.assertEqual(self.luotu_sokkelo[0].__class__, list)
        self.assertEqual(self.luotu_sokkelo[1].__class__, list)

    def test_luo_sokkelo_tekee_oikean_maaran_solmuja(self):
        self.assertEqual(len(self.luotu_sokkelo[0]), 9)

    def test_luodut_solmut_saavat_oikeita_arvoja(self):
        tutkittava_solmu = self.luotu_sokkelo[0][2]
        self.assertEqual(tutkittava_solmu.id,5)
        self.assertEqual(tutkittava_solmu.x,5)
        self.assertEqual(tutkittava_solmu.y,1)

    def test_luo_sokkelo_tekee_oikean_maaran_linkkeja(self):
        self.assertEqual(len(self.luotu_sokkelo[1]), 6)