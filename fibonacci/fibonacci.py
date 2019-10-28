from functools import lru_cache


@lru_cache(maxsize=2048)
def fibonacci(n):
    if type(n) != int or n < 1:
        raise TypeError("n must be a positive integer")
    if n < 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# test for 1000 fibos:
for i in range(1, 1001):
    print(i, ':', fibonacci(i))


# golden ratio:
for i in range(1, 1001):
    print(fibonacci(i + 1) / fibonacci(i))
