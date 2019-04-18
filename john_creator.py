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
        ## maps words (strings) to MulaneyObject
        self._dist = dict()

    def process(self, filename):
        pass

    def _randomWord(self):
        return choice(self._dist)

    def _next(self, key):
        return 

if __name__ == "__main__":
    print("can my girlfriend come?")
