from resource.node import Solmu
from resource.sokkelo import Sokkelo

def luo_sokkelo(sokkelo, leveys=1):
    #sokkelo on lista aktiivisia ja epäaktiivisia suunniteltuja solmuja sokkelolle
    solmut = []
    linkit = []
    for i in range(len(sokkelo)):
        if sokkelo[i]:
            x = selvita_x(i, leveys)
            y = selvita_y(i+1,leveys,x)
            solmut.append(Solmu(x,y,i+1))
            if x > 1:
                if sokkelo[i-1]:
                    linkit.append((i,i+1))
            if y > 1:
                if sokkelo[i-leveys]:
                    linkit.append((i-leveys+1,i+1))

    return Sokkelo(solmut, linkit)


def selvita_x(i, leveys):
    return (i%leveys) +1

def selvita_y(i, leveys,x):
    return ((i - x) / leveys) +1

testisokkelo = luo_sokkelo([1,1,1,1,1,1,
                1,1,1,1,1,1,
                1,1,1,1,1,1,
                1,1,1,1,0,0,
                1,1,1,1,0,1],6)