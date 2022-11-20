def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
lst = []
print('Enter the even and odd values')
n = int(input('nos of values you want'))

for i in range(0, n):
    num = int(input())
    lst.append(num)
# print(lst)
even, odd = count(lst)
print("even nos {} and odd nos {}".format(even, odd))
