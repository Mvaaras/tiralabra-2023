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
    1:".",
    3:"-"
}

    