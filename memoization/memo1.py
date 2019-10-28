import time
from functools import lru_cache
cache = {}


#@lru_cache(maxsize=256)
def funky(number):
    print("wait", number, "seconds...")
    if number in cache:
        return cache[number]
    else:
        time.sleep(number)
        value = number * number
        cache[number] = value
        return value



funky(1)
funky(2)
funky(3)
funky(3)
funky(3)
funky(3)
funky(3)
funky(3)
funky(4)
