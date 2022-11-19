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
value = int(input('Enter roll_no to find name'))
nam = input('Enter name to find roll_no')
print(data.get(value))
print(data.items(nam))

