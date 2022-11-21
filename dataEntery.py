# import math as m
# import array as arr
password = int(input('Enter pass. for data entery '))
if password == 12345:
        num = int(input('Enter the number of clints you want'))
        roll_no = []
        name = []
        for i in range(num):
            roll_no.append(int(input('Enter roll_no ')))
            name.append(input('Enter his name '))
data = dict(zip(roll_no, name))
# print(data)
# value = int(input('Enter roll_no to find name'))
# nam = input('Enter name to find roll_no')
# print(data.get(value))
# print(data.items(nam))
evens = list(filter(lambda a: a % 2 == 0, roll_no))
odds = list(filter(lambda a: a % 2 != 0, roll_no))
x = int(input('enter {} for even and {} for odd'.format(1, 2)))
if x == 1:
    print('printing the even candidates :')
    for i in evens:
        print('roll no : {} and name : {}'.format(i, data.get(i)))
if x == 2:
    print('printing the even candidates :')
    for i in odds:
        print('roll no : {} and name : {}'.format(i, data.get(i)))
else :
    print('wrong input')

