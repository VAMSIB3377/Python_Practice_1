# Generators Gives Iterators

# yield is a generator which will give us iterator

def topten():  # Generator Function Since we used Yield
    """
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    """

    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1


values = topten()
"""
print(values.__next__())
print(next(values))
print(next(values))
print(next(values))
print(next(values))
"""

for i in values:
    print(i)
