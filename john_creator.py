## Julia Kei Kawano

"""
Something something generating John Mulaney jokes
"""

import random
from random import choice

## define your dict value object
class MulaneyValue(object):
    __slots__ = ["_total", "_counts", "_words"]

    def __init__(self):
        self._total = 0
        self._counts = []
        self._words = []

    def add(self, w, c):
        self._counts.append(c)
        self._words.append(w)
        self._total+=c

    def _next(self):
        r = random(count)


        

if __name__ == "__main__":
    print("can my girlfriend come?")
