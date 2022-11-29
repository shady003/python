nums = [0, 2, 4, 6, 8]

it = iter(nums)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it))

class topTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = topTen()

for i in values:
    print(i)
