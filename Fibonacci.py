from time import time
from functools import lru_cache

class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1}


    def calcola_elemento_cache(self, n):
        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.cache[n] = (self.calcola_elemento_cache(n-1) +
                             self.calcola_elemento_cache(n - 2))
            return self.cache[n]



    def calcola_elemento(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.calcola_elemento(n - 1) + self.calcola_elemento(n - 2)


    @lru_cache(maxsize=None)
    def calcola_elemento_lru(self,n):
        if n == 0 or n == 1:
            return n
        else:
            return (self.calcola_elemento_lru(n - 1) +
                    self.calcola_elemento_lru(n - 2))


if __name__ == "__main__":
    fib = Fibonacci()
    start = time()
    print( fib.calcola_elemento_lru(40) )
    end = time()
    print( f"Tempo impiegato {end - start}" )