import sys

sys.setrecursionlimit(2000)
# set to 2000


def greet(n):
    i = 0
    if i < n:

        print('Hello')
        i += 1
        greet(n-1)
        # only used for 1000 times by default (without condition)


x = int(input('Enter nos greet:'))
greet(x)
print(sys.getrecursionlimit())
