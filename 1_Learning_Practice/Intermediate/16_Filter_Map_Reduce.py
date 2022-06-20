from functools import reduce

nums = [7, 8, 6, 5, 4, 7, 4, 5, 9]

evens = list(filter(lambda n: n % 2 == 0, nums))
doubles = list(map(lambda n: n * 2, evens))
sum1 = reduce(lambda a, b: a + b, doubles)

print(evens)
print(doubles)
print(sum1)
