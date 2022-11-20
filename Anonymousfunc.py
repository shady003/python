# lambda : a anonymous function
f = lambda a, b: a + b
result = f(5, 6)
print(result)


# filter() , map() and reduce()

from functools import reduce
nums = [1, 32, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
doubles = list(map(lambda n: n * 2, evens))
sum = reduce(lambda a, b: a+b, doubles)
print(evens)
print(doubles)
print(sum)
