# Määrittelydokumentti

Huom: Kyseessä on jatkettu projekti, koska ensimmäinen suorituskerta keskeytyi. Toisella suorituskerralla tarkoitukseni on toteuttaa nimenomaan ne projektin osat joka ekalla kerralla jäivät kesken, eli Dijkstra oikeanlaiseksi ja IDA* reitinhakualgoritmin toteutus.

_Pikainfo: Reitinhaku, Python, Suomi, TKT_

## Teknisen toteutuksen tiedot
Projektina on toteuttaa kaksi reitinhakualgoritmia - IDA* ja Dijkstra, ja vertailla miten hyvin ne toimivat nopeimman reitin etsimisessä painotetussa verkossa. 

Projekti ollaan toteuttamassa Pythonilla. Ymmärrän myös Javaa siinä määrin että voin vertaisarvioida sillä toteutettuja projekteja.

Aion toteuttaa projektia varten itse yllä mainitut algoritmit. Jotta Dijkstrasta saisi mahdollisimman tehokkaan, aion toteuttaa siihen myös tietorakenteena keon joka päivittyy laskettujen etäisyyksien muuttuessa.

Yritän projektissa selvittää hyviä tapoja löytää lyhyintä reittiä verkossa. Valitsin nämä algoritmit koska minulla oli niistä jo vähän esitietoja ja koska IDA* oli minusta mielenkiintoinen, ja koska ne ovat riittävän erilaisia niin että niiden vertailu keskenään kuulostaa mielekkäältä.

IDA* algoritmin aikakompleksisuus riippuu käsittääkseni käytetystä heuristiikasta ja ongelmasta jota sillä yritetään ratkaista, koska IDA* saattaa käydä samoissa solmuissa vaikka kuinka monta kertaa. Ajatuksena olisi kuitenkin optimoida heuristiikkaa sen verran että se toimii mahdollisimman tehokkaasti. Dijkstra sen sijaan olisi tarkoitus saada päivittyvän keon avulla O((E+V)log(V)) aikakompleksisuuteen. IDA* On tilakompleksisuuden kannalta parempi joten siihen tavoitteena olisi O(d) jossa d on reitin pituus, koska syvyyshakuna IDA* ei tarvitse ikinä tallentaa mitään muuta. Dijkstra tilavaativuus tulisi olla luokkaa O(2V)

Syötteet eivät ole merkittävä osuus projektin suunniteltua toimintaa, mutta saatan toteuttaa aloitus ja lopetuspisteen valinnan niin että ne voi antaa käyttöliittymässä syötteinä.

## Projektin hallintaan liittyvät tiedot
Koulutusohjelmani on tietojenkäsittelytieteen kandidaatti (TKT) ja projektin dokumentaation kieli on suomi.

## Lähteet

[Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), [IDA*](https://en.wikipedia.org/wiki/Iterative_deepening_A*), [Time Complexity of iterative deepening A*](https://www.sciencedirect.com/science/article/pii/S0004370201000947?via%3Dihub)
