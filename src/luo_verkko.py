import random

#Luodaan verkko jossa tiedetään että kaikkiin verkon jäseniin on olemassa linkki ja maksimipituus kahden jäsenen välillä on niiden etäisyys lukusuoralla*2
def luo_verkko(koko,tiiviys = 10):
    solmut = {}
    for i in range (1,koko+1):
        solmut[i] = {(i-1,2),(i+1,2)}
    
    solmut[1].discard((0,2))
    solmut[koko].discard((koko+1,2))
    solmut[0] = koko

    for i in range (0, tiiviys):
        #linkkien määrä random, sillä mahdollista päällekkäisyyttä esiintyy
        bonus_linkitettava_1 = random.randint(1,koko)
        bonus_linkitettava_2 = random.randint(2,koko)
        pituus = random.randint(1,3)
        if bonus_linkitettava_1 != bonus_linkitettava_2:
            solmut[bonus_linkitettava_2].add((bonus_linkitettava_1,pituus))
            solmut[bonus_linkitettava_1].add((bonus_linkitettava_2,pituus))

    return solmut


testiverkko = {0:5,
               1:{(2,2)},
               2:{(1,2),(3,2),(9,1)},
               3:{(2,2),(4,2),(5,3)},
               4:{(3,2),(5,2)},
               5:{(4,2),(6,2),(3,3)},
               6:{(5,2),(7,2)},
               7:{(6,2),(8,2)},
               8:{(7,2),(9,2)},
               9:{(8,2),(2,1)}}