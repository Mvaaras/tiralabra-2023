from resource.node import Solmu

def luo_sokkelo(sokkelo, leveys=1):
    #sokkelo on lista aktiivisia ja epäaktiivisia suunniteltuja solmuja sokkelolle
    solmut = []
    linkit = []
    for i in range(len(sokkelo)):
        if sokkelo[i]:
            x = selvita_x(i, leveys)
            y = selvita_y(i+1,leveys,x)
            solmut.append(Solmu(x,y,i+1))
            print((x,y))
            if x > 1:
                if sokkelo[i-1]:
                    linkit.append((i,i+1))
            if y > 1:
                if sokkelo[i-leveys]:
                    linkit.append((i-leveys+1,i+1))

    return (solmut, linkit)


def selvita_x(i, leveys):
    return (i%leveys) +1

def selvita_y(i, leveys,x):
    return ((i - x) / leveys) +1