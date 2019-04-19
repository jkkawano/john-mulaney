## Julia Kei Kawano

"""
Something something generating John Mulaney jokes
"""

from random import choice
from random import randint

__all__ = ['MulaneyValue']

## define your dict value object
class MulaneyValue(object):
    __slots__ = ["_total", "_wordCounts"]

    def __init__(self):
        self._total = 0
        self._wordCounts = dict()

    def __init__(self, w):
        self._total = 1
        self._wordCounts = {w:1}

    def add(self, w):
        """ Adding a new word """
        self._total+=1

        if w in self._wordCounts:
            self._wordCounts[w]+=1
        else:
            self._wordCounts[w] = 1

    def randNext(self):
        i = randint(0,self._total)
        soFar = 0
        for k in self._wordCounts:
            soFar += self._wordCounts[k]        
            if soFar >= i:
                return k

    def __str__(self):
        """ prints out the dictionary """
        return str(self._wordCounts)

    
class MulaneyGenerator(object):
    """ good documentation """
    ## Keep track of words within []
    ## Keep track of words within ""
    ## Keep track of good starting words

    __slots__ = ['_dist']

    def __init__(self):
        ## maps words (strings) to MulaneyValue
        self._dist = dict()

    def addWord(self, key, val):
        if key in self._dist:
            self._dist[key].add(val)
        else:
            self._dist[key] = MulaneyValue(val)

    def internalize(self, filename):
        dat = []
        with open(filename) as f:
            for line in f:
                for w in line.split():
                    dat.append(w.strip('"'))
                for i in range(len(dat)-1):
                    self.addWord(dat[i], dat[i+1])
                if(len(dat)>0): dat = [dat[-1]]

    def internalizeChar(self, filename, n=3):
        with open(filename) as f:
            for line in f:
                for i in range(len(line)-n):
                    self.addWord(line[i:i+n], line[i+n])

    def randWord(self):
        return choice(list(self._dist.keys()))

    def nextWord(self, key):
        if key not in self._dist:
            return self.randWord()
        return self._dist[key].randNext()

    def produceWords(self, n):
        result = []
        w = self.randWord()
        for _ in range(n):
            result.append(self.nextWord(w))
            w = self.nextWord(w)
        return " ".join(result)

    def _next(self, key):
        return 

if __name__ == "__main__":
    gen = MulaneyGenerator()

    gen.internalize("data/new-in-town")
    gen.internalize("data/radio-city")
    gen.internalize("data/comeback-kid")

    print(gen.produceWords(200))
    
    print("can my girlfriend come?")
