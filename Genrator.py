def topten():
    yield 5
    yield 15
    yield 25


# Genrator

def sqrt():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1


values = topten()
sqrt = sqrt()
print(values.__next__())
print(values.__next__())
# print(values.__next__())


for i in sqrt:
    print(i)
