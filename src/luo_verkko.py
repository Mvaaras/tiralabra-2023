import random

#Luodaan verkko jossa tiedetään että kaikkiin verkon jäseniin on olemassa linkki ja maksimipituus kahden jäsenen välillä on niiden etäisyys lukusuoralla
def luo_verkko(koko,tiiviys = 10):
    solmut = {}
    for i in range (1,koko+1):
        solmut[i] = {i-1,i+1}
    
    solmut[1].discard(0)
    solmut[koko].discard(koko+1)


    for i in range (0, tiiviys):
        #linkkien määrä random, sillä mahdollista päällekkäisyyttä esiintyy
        bonus_linkitettava_1 = random.randint(1,koko)
        bonus_linkitettava_2 = random.randint(2,koko)
        if bonus_linkitettava_1 != bonus_linkitettava_2:
            solmut[bonus_linkitettava_2].add(bonus_linkitettava_1)
            solmut[bonus_linkitettava_1].add(bonus_linkitettava_2)

    return solmut