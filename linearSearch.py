
def lin(list,n):
    for i in list:
        if i == n:
            return True
        else:
            pass
    return False


list =[1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 9
if lin(list, num):
    print('Found', num)
else:
    print('Not Found')
