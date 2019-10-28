import time
from functools import lru_cache
cache = {}

#@lru_cache(maxsize=256)
def expensive_function(number):
    print("wait", number, "seconds...")
    if number in cache:
        return cache[number]
    else:

        time.sleep(number)
        value = number * number
        cache[number] = value
        return value



expensive_function(3)
expensive_function(4)
expensive_function(3)
expensive_function(3)
expensive_function(3)
expensive_function(3)
expensive_function(3)
expensive_function(3)
expensive_function(5)
