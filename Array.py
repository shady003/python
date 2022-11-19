import array as arr
vals = arr.array('i', [5, 9, 8, 4, 2])
newArray = arr.array('u', ['a', 'e', 'i', 'o', 'u'])
cpyArray = arr.array(vals.typecode, (a*a for a in vals))
vals.reverse()
# print(vals)
print(vals.buffer_info())
print(vals.typecode)
for i in range(len(vals)):
    print(cpyArray[i], ' ', end='')
    i += 1
arr = arr.array('i', [])
x = int(input('\nEnter the no of values you want in array\n >>>'))
for j in range(x):
    new = int(input('Enter the value'))
    arr.append(new)
    j += 1
print(arr)
val = input('Enter the value to check')
l = 0
for k in arr:
    if k==val:
        print(k)
        break

    l+=1
print(arr.index(val))