from tokenize import String


class Bet:
    u = ''
    f = ''
    mu = 0
    mf = 0
    ubroker = ''
    fbroker = ''
    __sides = set()
    
    def __init__(self, u, f, mu, mf, broker):
        self.u = u
        self.f = f
        self.__sides.add(u)
        self.__sides.add(f)

        self.mu = mu
        self.mf = mf
        self.ubroker = broker
        self.fbroker = broker
        
    def getSides(self):
        return self.__sides     
    
    def updateFavorite(self, mu, broker):
        if ( mu > self.mu ):
            self.mu = mu
            self.ubroker = broker
    
    def updateUnderdog(self, mf, broker):
        if ( mf < self.mf ):
            self.mf = mf
            self.fbroker = broker

    def sameGame(self, b) -> bool:
        if not isinstance(b, Bet) :
            return False
        return self.__sides == b.getSides()
    
    # def __eq__(self, other):
    #     if not isinstance(other, type(self)): return NotImplemented
    #     return self.mac == other.mac and self.port == other.port and self.dpid == other.dpid