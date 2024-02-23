class Keko:
    def __init__(self):
        self.sisalto = []
        self.etaisyydet = {}
        self.id = {}

    def lisaa(self, solmu, etaisyys):
        self.sisalto.append(solmu)
        self.etaisyydet[solmu] = etaisyys
        self.tarkista_ylos(len(self.sisalto)-1)
    
    def tarkista_ylos(self, child):
        parent = self.get_parent(child)
        if self.etaisyydet[self.sisalto[child]] < self.etaisyydet[self.sisalto[parent]]:
            self.swap(child, parent)
            child = parent
            self.tarkista_ylos(child)

    def get_parent(self, child):
        return int((child-1)/2)

    def swap(self, child, parent):

        temp = self.sisalto[parent]
        self.sisalto[parent] = self.sisalto[child]
        self.sisalto[child] = temp

    def muuta_pituus(self, solmu, pituus):
        self.sisalto.remove(solmu)
        self.lisaa(solmu, pituus)

    def palauta_pienin(self):
        pienin = self.sisalto[0]
        self.sisalto.remove(pienin)
        self.tarkista_alas(0)
        return pienin

    
    def tarkista_alas(self, parent):
        children = self.get_children(parent)
        for child in children:
            if child < len(self.sisalto):
                if self.etaisyydet[self.sisalto[parent]] > self.etaisyydet[self.sisalto[child]]:
                    self.swap(child, parent)
                    self.tarkista_alas(child)


    def get_children(self, parent):
        return (parent*2+1,parent*2+2)

    def on_tyhja(self):
        return len(self.sisalto) == 0