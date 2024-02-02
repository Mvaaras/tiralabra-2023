import unittest
import random
from luo_verkko import luo_verkko

class TestLuoVerkko(unittest.TestCase):
    def setUp(self):
        random.seed(1)
        self.verkko = luo_verkko(10,2)

    def test_luo_verkko_palauttaa_dict_olion(self):
        self.assertEqual(type(self.verkko),dict)
    
    def test_verkko_on_linkitetty_oikein(self):
        self.assertEqual(self.verkko[10],{9})
        self.assertEqual(self.verkko[1],{2})
    
    def test_bonus_linkki_verkossa(self):
        self.assertEqual(self.verkko[3],{2,4,5})
