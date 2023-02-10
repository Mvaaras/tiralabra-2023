from luo_sokkelo import luo_sokkelo

def print_sokkelo(sokkelo):
    korkeus = 1
    paikka = 1
    leveys = 1
    rivi = ""
    for solmu in sokkelo:
        if not korkeus == solmu.y:
            rivi += "#" * (leveys - paikka+1)
            print(rivi)
            rivi = ""
            korkeus += 1
            paikka = 1
        if not paikka == solmu.x:
            rivi += "#" * (solmu.x - paikka)
            paikka = solmu.x
        rivi += status[solmu.tila]
        if paikka > leveys:
            leveys = paikka
        paikka += 1
    print(rivi)


status = {
    2:",",
    1:"."
}

iso_sokkelo = [0,0,1,1,1,0,
1,1,1,0,0,0,
1,0,0,0,0,1,
0,0,0,0,1,0]
luotu_sokkelo = luo_sokkelo(iso_sokkelo,6)
print_sokkelo(luotu_sokkelo[0])