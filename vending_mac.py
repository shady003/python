x = int(input('How much candies you want '))
i = 1
avl = 10
while i <= x:
    if i <= avl:
        print('Candy')
        i += 1
    else:
        print('out of stock')
        break
input()
